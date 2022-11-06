from rest_framework import serializers
from .models import Borrower, Guarantor

class GuarantorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Guarantor
        fields = "__all__"
        

class BorrowerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Borrower
        fields = "__all__"