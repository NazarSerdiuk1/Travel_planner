from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProjectViewSet, PlaceViewSet

app_name = "travel_planner"
router = DefaultRouter()
router.register("projects", ProjectViewSet, basename="projects")

urlpatterns = [
    path("", include(router.urls)),
    path("projects/<int:project_id>/places/", PlaceViewSet.as_view({"get": "list", "post": "create"})),
    path("projects/<int:project_id>/places/<int:pk>/", PlaceViewSet.as_view({"get": "retrieve", "patch": "partial_update"})),

]
