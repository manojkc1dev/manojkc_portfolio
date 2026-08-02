# apps/authentication/urls.py
from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    # POST endpoint to submit username/password and receive JWT access/refresh tokens
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    
    # POST endpoint to submit a valid refresh token and get a new access token
    path('refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]