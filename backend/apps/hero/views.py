from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from .models import Hero
from .serializers import HeroSerializer # or your corresponding serializer

class HeroProfileView(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        profile = Hero.objects.first()
        if not profile:
            profile = Hero.objects.create()
        serializer = HeroSerializer(profile)
        return Response(serializer.data)