from django.urls import path
from .views import SkillListApi

urlpatterns = [
    path('', SkillListApi.as_view(), name='skill-list'),
]