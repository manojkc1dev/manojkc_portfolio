from django.urls import path
from .views import HeroDetailApi

urlpatterns = [
    path('', HeroDetailApi.as_view(), name='hero-detail'),
]