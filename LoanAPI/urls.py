from django.contrib import admin
from django.urls import path, include

from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="Loans API",
        default_version='v1',
        description="This is a Loan Management platform Backend Service",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="paulkadabo@gmail.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path("core/", include("core.urls")),
    path("people/", include("people.urls")),
    path("loans/", include("loans.urls")),
    path("auth/", include('djoser.urls')),
    path("auth/", include('djoser.urls.jwt')),
    path("", schema_view.with_ui('swagger',
            cache_timeout=0), name='schema-swagger-ui'),
    path("redoc/", schema_view.with_ui('redoc',
            cache_timeout=0), name='schema-redoc'),
]
