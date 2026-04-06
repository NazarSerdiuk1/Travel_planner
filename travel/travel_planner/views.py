from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework import status
from drf_spectacular.utils import extend_schema, extend_schema_view 

from .models import Travel_Project, Place
from .serializers import(
    TravelProjectSerializer,
    ProjectCreateSerializer,
    PlaceSerializer
)
from .services import get_place_from_api
from .validators import validate_no_visited, validate_places_limit

@extend_schema_view(
    list=extend_schema(
        summary="List travel projects",
        description="Get all travel projects"
    ),
    retrieve=extend_schema(
        summary="Retrieve project",
        description="Get a single travel project by ID"
    ),
    create=extend_schema(
        summary="Create project",
        description="Create a new travel project with optional places"
    ),
    update=extend_schema(
        summary="Update project",
        description="Update project details"
    ),
    destroy=extend_schema(
        summary="Delete project",
        description="Delete project (not allowed if any place is visited)"
    ),
)

class ProjectViewSet(ModelViewSet):
    queryset = Travel_Project.objects.all()

    def get_serializer_class(self):
        if self.action == "create":
            return ProjectCreateSerializer
        return TravelProjectSerializer

    def destroy(self, request, *args, **kwargs):
        project = self.get_object()

        try:
            validate_no_visited(project)
        except Exception as e:
            return Response({"error": str(e)})
        
        return super().destroy(request, *args, **kwargs)

@extend_schema_view(
    list=extend_schema(
        summary="List places in project",
        description="Get all places for a specific project"
    ),
    retrieve=extend_schema(
        summary="Retrieve place",
        description="Get a specific place from a project"
    ),
    create=extend_schema(
        summary="Add place to project",
        description="Add a place from external API to a project (validated)"
    ),
    update=extend_schema(
        summary="Update place",
        description="Update notes or mark place as visited"
    ),
)

class PlaceViewSet(ModelViewSet):
    serializer_class = PlaceSerializer

    def get_queryset(self):
        return Place.objects.filter(project_id=self.kwargs["project_id"])
    
    def perform_create(self, serializer):
        project = Travel_Project.objects.get(id=self.kwargs["project_id"])

        validate_places_limit(project)

        external_id = self.request.data.get("external_id")
        api_data = get_place_from_api(external_id)

        serializer.save(
            project=project,
            title = api_data["title"]
        )
    
    def perform_update(self, serializer):
        place = serializer.save()

        project = place.project

        if project.places.count() > 0 and not project.places.filter(visited=False).exists():
            project.is_completed = True
            project.save()