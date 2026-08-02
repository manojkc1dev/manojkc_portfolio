from rest_framework import serializers
from .models import Experience

class ExperienceOutputSerializer(serializers.ModelSerializer):
    class Meta:
        model = Experience
        fields = [
            'id', 'company_name', 'role_title', 'location', 
            'start_date', 'end_date', 'is_current', 
            'description', 'technologies_used', 'display_order'
        ]