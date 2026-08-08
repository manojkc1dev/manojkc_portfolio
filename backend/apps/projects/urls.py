from django.urls import path
from .views import ProjectListApi

urlpatterns = [
    # Don't forget .as_view() for class-based views!
    path('', ProjectListApi.as_view(), name='project-list'), 
]