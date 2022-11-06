from django.shortcuts import render
from .models import LoanPayment, LoanApplication, Loan
from .serializers import LoanApplicationSerializer, LoanPaymentSerializer, LoanSerializer
from rest_framework.viewsets import ModelViewSet
# Create your views here.
class LoanModelViewSet(ModelViewSet):
    http_method_names = ['get', 'put', 'patch', 'delete']
    queryset = Loan.objects.all()
    serializer_class = LoanSerializer


class LoanPaymentModelViewSet(ModelViewSet):
    queryset = LoanPayment.objects.all()
    serializer_class = LoanPaymentSerializer


class LoanApplicationModelViewSet(ModelViewSet):
    queryset = LoanApplication.objects.all()
    serializer_class = LoanApplicationSerializer