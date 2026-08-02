from rest_framework import serializers
from .models import Project

class ProjectOutputSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = [
            'id', 'title', 'slug', 'short_description', 
            'thumbnail', 'github_url', 'live_demo_url', 'is_featured'
        ]