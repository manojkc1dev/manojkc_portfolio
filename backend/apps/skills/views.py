from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from drf_spectacular.utils import extend_schema
from .selectors import get_all_skills
from .serializers import SkillOutputSerializer

class SkillListApi(APIView):
    permission_classes = [AllowAny]

    @extend_schema(responses=SkillOutputSerializer(many=True))
    def get(self, request):
        skills = get_all_skills()
        serializer = SkillOutputSerializer(skills, many=True)
        return Response(serializer.data)