from django.shortcuts import render
from .models import Guarantor, Borrower
from .serializers import GuarantorSerializer, BorrowerSerializer, ProfileSerializer
from rest_framework.viewsets import ModelViewSet
from django.contrib.auth.models import User
from rest_framework.permissions import IsAuthenticated
# Create your views here.
class BorrowerModelViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Borrower.objects.all()
    serializer_class = BorrowerSerializer


class GuarantorModelViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Guarantor.objects.all()
    serializer_class = GuarantorSerializer


class ProfileModelViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated]
    http_method_names = ['get']
    #queryset = Borrower.objects.all()
    serializer_class = ProfileSerializer

    def get_queryset(self):
        user = self.request.user
        return Borrower.objects.filter(user=user)