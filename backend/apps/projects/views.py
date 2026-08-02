from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from drf_spectacular.utils import extend_schema
from .selectors import get_published_projects
from .serializers import ProjectOutputSerializer

class ProjectListApi(APIView):
    permission_classes = [AllowAny] # The frontend needs public access to read this

    @extend_schema(responses=ProjectOutputSerializer(many=True))
    def get(self, request):
        projects = get_published_projects()
        serializer = ProjectOutputSerializer(projects, many=True)
        return Response(serializer.data)