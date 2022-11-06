from django.shortcuts import render
from .models import LoanPayment, LoanApplication, Loan
from .serializers import LoanApplicationSerializer, LoanPaymentSerializer, LoanSerializer
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
# Create your views here.
class LoanModelViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated]
    http_method_names = ['get', 'put', 'patch', 'delete']
    queryset = Loan.objects.all()
    serializer_class = LoanSerializer


class LoanPaymentModelViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated]
    http_method_names = ['get', 'post']
    queryset = LoanPayment.objects.all()
    serializer_class = LoanPaymentSerializer


class LoanApplicationModelViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = LoanApplication.objects.all()
    serializer_class = LoanApplicationSerializer