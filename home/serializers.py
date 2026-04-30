from rest_framework import serializers
from common.enums import TechChoices
from .models import Home, Hero, Projects, Review, ProjectImage, Contact


class HomeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Home
        fields = ['id', 'tag_line', 'logo', 'description', 'title', 'banner_image']

class HeroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hero
        fields = ['id', 'caption', 'image']

# Project image Serializers.
class ProjectImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjectImage
        fields = ['id', 'project_image']

class ProjectsSerializer(serializers.ModelSerializer):
    images = ProjectImageSerializer(many=True, read_only=True)

    project_images = serializers.ListField(
        child=serializers.ImageField(),
        write_only=True,
        required=False
    )

    technologies = serializers.ListField(
        child=serializers.ChoiceField(choices=TechChoices.choices),
        required=False
    )

    class Meta:
        model = Projects
        fields = [
            "id", "alias", "slug", "title", "categories", "description",
            "logo", "images", "link", "notes", "project_images", "technologies",
            "status", "duration",
        ]

    def create(self, validated_data):
        project_images = validated_data.pop("project_images", [])
        techs_data = validated_data.pop("technologies", [])

        project = Projects.objects.create(**validated_data)

        if techs_data:
            project.technologies = techs_data
            project.save()

        for img in project_images:
            ProjectImage.objects.create(project=project, project_image=img)

        return project

    def update(self, instance, validated_data):
        project_images = validated_data.pop("project_images", [])
        techs_data = validated_data.pop("technologies", None)

        for k, v in validated_data.items():
            setattr(instance, k, v)
        instance.save()

        if techs_data is not None:
            instance.technologies = techs_data
            instance.save()

        for img in project_images:
            ProjectImage.objects.create(project=instance, project_image=img)

        return instance

    def to_representation(self, instance):
        rep = super().to_representation(instance)
        rep["categories"] = instance.categories
        rep["technologies"] = instance.technologies
        return rep

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ['id', 'user_name', "role", 'image', 'description', 'rating']

# Contact Serializer
class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = [
            'id',
            'name',
            'email',
            'phone',
            'contact_purpose',
            'address',
            'created_at',
            'updated_at'
        ]
        read_only_fields = [
            'id',
            'created_at',
            'updated_at'
        ]