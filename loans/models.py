from django.db import models
from people.models import Borrower
from core.models import LoanType
# Create your models here.
LOAN_APPLICATION_STATUS_CHOICES = (
    ("approved", "Approved"),
    ("declined", "Declined"),
)

LOAN_STATUS_CHOICES = (
    ("in_grace_period", "In Grace Period"),
    ("still_paying", "Still Paying"),
    ("fully_paid", "Full Paid"),
    ("default_pending", "Default Pending"),
    ("defaulted", "Defaulted"),
)

class LoanApplication(models.Model):
    borrower = models.ForeignKey(Borrower, on_delete=models.CASCADE, related_name="loan_applications")
    loan_type = models.ForeignKey(LoanType, on_delete=models.SET_NULL, null=True)
    amount_applying = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=255, choices=LOAN_APPLICATION_STATUS_CHOICES)
    decline_reason = models.TextField(null=True, blank=True)
    date_applied = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    note = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.borrower.id_number


class Loan(models.Model):
    borrower = models.ForeignKey(Borrower, on_delete=models.CASCADE, related_name="loans")
    amount_applied = models.DecimalField(max_digits=10, decimal_places=2)
    amount_awarded = models.DecimalField(max_digits=10, decimal_places=2)
    total_interest = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    amount_to_repay = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    amount_repaid = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    balance = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    status = models.CharField(max_length=255, choices=LOAN_STATUS_CHOICES, default='in_grace_period')
    loan_type = models.ForeignKey(
        LoanType, on_delete=models.SET_NULL, null=True)
    date_applied = models.DateTimeField(null=True, blank=True)
    date_updated = models.DateTimeField(auto_now=True)

    
    def __str__(self):
        return self.borrower.id_number


class LoanPayment(models.Model):
    borrower = models.ForeignKey(Borrower, on_delete=models.CASCADE, related_name="loans_payments")
    loan = models.ForeignKey(Loan, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment = models.JSONField(null=True, blank=True)
    date_paid = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.borrower.id_number
