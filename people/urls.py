from django.urls import path, include
from .import views
from rest_framework.routers import DefaultRouter
router = DefaultRouter()
router.register("borrowers", views.BorrowerModelViewSet, basename="borrowers")
router.register("guarantors", views.GuarantorModelViewSet, basename="gurantors")

urlpatterns = [
    path("", include(router.urls)),
]