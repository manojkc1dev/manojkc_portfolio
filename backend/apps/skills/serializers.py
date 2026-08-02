from rest_framework import serializers
from .models import Skill

class SkillOutputSerializer(serializers.ModelSerializer):
    category_display = serializers.CharField(source='get_category_display', read_only=True)

    class Meta:
        model = Skill
        fields = [
            'id', 'name', 'category', 'category_display', 
            'percentage', 'experience_years', 'is_featured', 'display_order'
        ]