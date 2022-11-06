from rest_framework.test import APIClient
from rest_framework import status
from django.contrib.auth.models import User
import pytest



@pytest.mark.django_db
class TestLoanTypeOperation:
    def test_get_loan_types(self, api_client):
        api_client = APIClient()
        resp = api_client.get("/core/loan-types")
        assert resp.status_code == status.HTTP_200_OK