from django.urls import path
from .views import ProjectListApi

urlpatterns = [
    path('', ProjectListApi.as_view(), name='project-list'),
]