from rest_framework import serializers
from .models import Hero

class HeroOutputSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hero
        fields = [
            'id', 'full_name', 'professional_title', 'headline',
            'short_introduction', 'profile_photo', 'resume_pdf',
            'github_url', 'linkedin_url', 'email'
        ]