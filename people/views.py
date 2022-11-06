from django.shortcuts import render
from .models import Guarantor, Borrower
from .serializers import GuarantorSerializer, BorrowerSerializer
from rest_framework.viewsets import ModelViewSet

# Create your views here.
class BorrowerModelViewSet(ModelViewSet):
    queryset = Borrower.objects.all()
    serializer_class = BorrowerSerializer


class GuarantorModelViewSet(ModelViewSet):
    queryset = Guarantor.objects.all()
    serializer_class = GuarantorSerializer