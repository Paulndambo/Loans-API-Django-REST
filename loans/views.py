from django.shortcuts import render
from .models import LoanPayment, LoanApplication, Loan
from .serializers import LoanApplicationSerializer, LoanPaymentSerializer, LoanSerializer, BankStatementSerializer
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from rest_framework import generics, status
from rest_framework.response import Response
import io
import csv
import pandas as pd
from django.db import transaction
from decimal import Decimal
# Create your views here.
class LoanModelViewSet(ModelViewSet):
    #permission_classes = [IsAuthenticated]
    #http_method_names = ['get', 'put', 'patch', 'delete']
    queryset = Loan.objects.all()
    serializer_class = LoanSerializer


class LoanPaymentModelViewSet(ModelViewSet):
    #permission_classes = [IsAuthenticated]
    http_method_names = ['get', 'post']
    queryset = LoanPayment.objects.all()
    serializer_class = LoanPaymentSerializer


class LoanApplicationModelViewSet(ModelViewSet):
    #permission_classes = [IsAuthenticated]
    queryset = LoanApplication.objects.all()
    serializer_class = LoanApplicationSerializer


class BankStatementUploadAPIView(generics.CreateAPIView):
    serializer_class = BankStatementSerializer

    @transaction.atomic
    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        file = serializer.validated_data['file']
        reader = pd.read_csv(file)
        for _, row in reader.iterrows():
            new_payment = LoanPayment(
                borrower_id=row["borrower"],
                loan_id=row['loan'],
                amount=row["amount"]
            )
            loan = Loan.objects.get(id=row['loan'])
            loan.amount_repaid += Decimal(row['amount'])
            loan.balance -= Decimal(row['amount'])
            loan.save()
            new_payment.save()
        return Response({"status": "success"}, status.HTTP_201_CREATED)
