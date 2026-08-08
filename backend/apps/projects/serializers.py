from rest_framework import serializers
from .models import Project

# 1. The Input Serializer (MUST match the spelling in views.py)
class ProjectInputSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        # Explicitly define fields allowed for POST requests
        fields = ['title', 'description', 'repo_url', 'live_url', 'image'] 

# 2. The Output Serializer
class ProjectOutputSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = '__all__'