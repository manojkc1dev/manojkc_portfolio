from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from drf_spectacular.utils import extend_schema
from .selectors import get_active_hero
from .serializers import HeroOutputSerializer

class HeroDetailApi(APIView):
    permission_classes = [AllowAny]

    @extend_schema(responses=HeroOutputSerializer)
    def get(self, request):
        hero = get_active_hero()
        if not hero:
            return Response({"detail": "Hero section not configured yet."}, status=404)
        serializer = HeroOutputSerializer(hero)
        return Response(serializer.data)