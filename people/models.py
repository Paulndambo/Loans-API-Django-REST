from django.db import models
from django.conf import settings
from core.models import LoanType
# Create your models here.
MARITAL_STATUS_CHOICES = (
    ("married", "Married"),
    ("single", "Single"),
    ("divorced", "Divorced"),
    ("widowed", "Widowed"),
)

GENDER_CHOICES = (
    ("male", "Male"),
    ("female", "Female"),
    ("binary", "Binary"),
    ("other", "Other"),
)

RELATIONSHIP_CHOICES = (
    ("brother_sister", "Brother/Sister"),
    ("mother_father", "Mother/Father"),
    ("cousin", "Cousin"),
    ("aunt_uncle", "Aunt/Uncle"),
    ("friend", "Friend"),
    ("grandparent", "Grand Parent"),
)

class Borrower(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    id_number = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=255)
    kra_pin = models.CharField(max_length=255, null=True, blank=True)
    gender = models.CharField(max_length=255, choices=GENDER_CHOICES)
    marital_status = models.CharField(max_length=255, choices=MARITAL_STATUS_CHOICES)
    birth_date = models.DateField()
    employment = models.JSONField(null=True, blank=True)
    education = models.JSONField(null=True, blank=True)
    postal_code = models.CharField(max_length=255, null=True, blank=True)
    zip_code = models.CharField(max_length=255, null=True, blank=True)
    city = models.CharField(max_length=255)
    country = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.first_name


class Guarantor(models.Model):
    borrower = models.ForeignKey(Borrower, on_delete=models.CASCADE, related_name="guarantors")
    name = models.CharField(max_length=255)
    id_number = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=255)
    email = models.EmailField(null=True, blank=True)
    kra_pin = models.CharField(max_length=255, null=True, blank=True)
    gender = models.CharField(max_length=255, choices=GENDER_CHOICES)
    marital_status = models.CharField(max_length=255, choices=MARITAL_STATUS_CHOICES)
    birth_date = models.DateField()
    relationship = models.CharField(max_length=255, choices=RELATIONSHIP_CHOICES)
    employment = models.JSONField(null=True, blank=True)
    education = models.JSONField(null=True, blank=True)
    postal_code = models.CharField(max_length=255, null=True, blank=True)
    zip_code = models.CharField(max_length=255, null=True, blank=True)
    city = models.CharField(max_length=255)
    country = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
