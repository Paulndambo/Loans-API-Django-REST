from rest_framework import serializers
from .models import LoanApplication, Loan, LoanPayment
from django.db import transaction


class LoanApplicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = LoanApplication
        fields = "__all__"

    def create(self, validated_data):
        amount_applying = validated_data.get('amount_applying')
        loan_type = validated_data.get('loan_type')
        minimum_amount = loan_type.minimum_amount
        maximum_amount = loan_type.maximum_amount

        if amount_applying < minimum_amount or amount_applying > maximum_amount:
            raise serializers.ValidationError(f"Amount Applying should be between {minimum_amount} and {maximum_amount}")
        return LoanApplication.objects.create(**validated_data)


    @transaction.atomic
    def update(self, instance, validated_data):
        approval_status = validated_data.get('status')
        decline_reason = validated_data.get('decline_reason')
        if approval_status == 'approved':
            instance.status = 'approved'
            """
            => Create A Loan Instance
            """
            interest = instance.amount_applying * instance.loan_type.interest_rate
            loan = Loan()
            loan.borrower = instance.borrower
            loan.amount_applied = instance.amount_applying
            loan.amount_awarded = instance.amount_applying
            loan.total_interest = interest
            loan.amount_to_repay = instance.amount_applying + interest
            loan.loan_type = instance.loan_type
            loan.balance = instance.amount_applying + interest
            loan.date_applied = instance.date_applied
            loan.save()

        instance.status = approval_status
        instance.decline_reason = decline_reason
        instance.save()
        return instance


class LoanSerializer(serializers.ModelSerializer):
    class Meta:
        model = Loan
        fields = "__all__"


class LoanPaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = LoanPayment
        fields = "__all__"

    @transaction.atomic
    def create(self, validated_data):
        amount = validated_data.get('amount')
        loan = validated_data.get('loan')
        loan.amount_repaid += amount
        loan.balance -= amount
        loan.save()
        return LoanPayment.objects.create(**validated_data)