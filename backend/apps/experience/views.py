from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from drf_spectacular.utils import extend_schema
from .selectors import get_all_experiences
from .serializers import ExperienceOutputSerializer

class ExperienceListApi(APIView):
    permission_classes = [AllowAny]

    @extend_schema(responses=ExperienceOutputSerializer(many=True))
    def get(self, request):
        experiences = get_all_experiences()
        serializer = ExperienceOutputSerializer(experiences, many=True)
        return Response(serializer.data)