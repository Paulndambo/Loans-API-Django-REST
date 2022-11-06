from django.urls import path, include
from .import views
from rest_framework.routers import DefaultRouter
router = DefaultRouter()
router.register("loans-awarded", views.LoanModelViewSet, basename="loans-awarded")
router.register("loan-applications", views.LoanApplicationModelViewSet, basename="loan-applications")
router.register("payments", views.LoanPaymentModelViewSet, basename="payments")

urlpatterns = [
    path("", include(router.urls)),
]