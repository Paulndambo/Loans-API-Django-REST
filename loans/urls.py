from django.urls import path, include
from .import views
from rest_framework.routers import DefaultRouter
router = DefaultRouter()
router.register("loan-applications", views.LoanApplicationModelViewSet, basename="loan-applications")
router.register("", views.LoanModelViewSet, basename="loans")
router.register("loan-payments", views.LoanPaymentModelViewSet, basename="loan-payments")

urlpatterns = [
    path("", include(router.urls)),
]