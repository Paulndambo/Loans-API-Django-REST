from email.policy import default
from django.db import models

# Create your models here.
class LoanType(models.Model):
    name = models.CharField(max_length=255)
    grace_period = models.IntegerField()
    days_to_repay = models.IntegerField()
    number_of_guarantors = models.IntegerField(default=0)
    minimum_amount = models.DecimalField(max_digits=10, decimal_places=2)
    maximum_amount = models.DecimalField(max_digits=10, decimal_places=2)
    interest_rate = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name