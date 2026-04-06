from rest_framework import serializers
from .models import Travel_Project, Place
from .services import get_place_from_api


class PlaceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Place
        fields = ["id", "project", "external_id", "title", "notes", "visited"]
        read_only_fields = ("project", "title")


class TravelProjectSerializer(serializers.ModelSerializer):
    places = PlaceSerializer(many=True, read_only=True)

    class Meta:
        model = Travel_Project
        fields = ["id", "name", "description", "start_date", "is_completed"]


class ProjectCreateSerializer(serializers.ModelSerializer):
    places = serializers.ListField(write_only=True)

    class Meta:
        model = Travel_Project
        fields = ["id", "name", "description", "start_date", "is_completed"]
    
    def create(self, validated_data):
        places_data = validated_data.pop("places")

        if len(places_data) > 10:
            raise serializers.ValidationError("Max 10 places")
        
        project = Travel_Project.objects.create(**validated_data)

        for place in places_data:
            api_data = get_place_from_api(place["external_id"])

            Place.objects.create(
                project=project,
                external_id = place["external_id"],
                title = api_data["title"]
            )
        return project