from django.urls import path
from .views import HeroProfileView

urlpatterns = [
    path('profile/', HeroProfileView.as_view(), name='hero-profile'),
]