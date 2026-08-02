from django.urls import path
from .views import ExperienceListApi

urlpatterns = [
    path('', ExperienceListApi.as_view(), name='experience-list'),
]