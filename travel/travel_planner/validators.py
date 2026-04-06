from rest_framework.exceptions import ValidationError

def validate_places_limit(project):
    if project.places.count() >= 10:
        raise ValidationError("Max 10 places per project")

def validate_no_visited(project):
    if project.places.filter(visited=True).exists():
        raise ValidationError("Cannot delete project with visited places")
