from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from drf_spectacular.utils import extend_schema
from .serializers import ProjectInputSerializer, ProjectOutputSerializer
from .models import Project

# THIS MUST MATCH THE IMPORT EXACTLY
class ProjectListApi(APIView):
    
    def get(self, request):
        projects = Project.objects.all() # Or your get_published_projects() selector
        serializer = ProjectOutputSerializer(projects, many=True)
        return Response(serializer.data)

    @extend_schema(
        request=ProjectInputSerializer,
        responses=ProjectOutputSerializer
    )
    def post(self, request):
        serializer = ProjectInputSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        project = serializer.save()
        output_serializer = ProjectOutputSerializer(project)
        return Response(output_serializer.data, status=status.HTTP_201_CREATED)