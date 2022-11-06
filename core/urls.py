from django.urls import path, include
from .import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register("loan-types", views.LoanTypeModelViewSet, basename="loan-types")

urlpatterns = [
    path("", include(router.urls)),
]