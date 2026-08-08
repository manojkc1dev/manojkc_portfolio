from rest_framework import serializers
from .models import Hero  # Make sure this says Hero, not HeroProfile

class HeroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hero
        fields = '__all__'