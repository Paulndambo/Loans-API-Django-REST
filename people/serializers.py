from rest_framework import serializers
from .models import Borrower, Guarantor
from django.contrib.auth.models import User

class GuarantorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Guarantor
        fields = "__all__"

class BorrowerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Borrower
        fields = "__all__"        

class ProfileSerializer(serializers.ModelSerializer):
    guarantors = serializers.SerializerMethodField(read_only=True)
    loans = serializers.SerializerMethodField(read_only=True)
    loan_applications = serializers.SerializerMethodField(read_only=True)
    loan_payments = serializers.SerializerMethodField(read_only=True)
    user_details = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = Borrower
        # "loan_applications", "loans", "loan_payments"]
        
        fields = ["id", "id_number", "phone_number", "kra_pin", "gender", "marital_status", "birth_date", "employment", "education", "postal_code",
                  "city", "country", "created_at", "updated_at", "guarantors", "loan_applications", "loans", "loan_payments", "user_details"]


    def get_guarantors(self, obj):
        return obj.guarantors.values()

    
    def get_loans(self, obj):
        return obj.loans.values()

    def get_loan_applications(self, obj):
        return obj.loan_applications.values()
    
    def get_loan_payments(self, obj):
        return obj.loans_payments.values()

    def get_user_details(self, obj):
        return User.objects.filter(id=obj.user.id).values("id", "last_login", "is_superuser", 
            "username","first_name","last_name","email","is_staff","is_active","date_joined"
        )
    