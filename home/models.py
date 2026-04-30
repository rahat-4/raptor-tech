from django.contrib.postgres.fields import ArrayField
from django.db import models

from common.enums import (
    ProjectStatusChoices,
    TechChoices,
    DurationsChoice, CategoriesChoices,
)
from common.models import NameSlugDescriptionBaseModel


class Home(models.Model):
    tag_line = models.CharField(max_length=300, null=True, blank=True)
    logo = models.ImageField(null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    title = models.CharField(max_length=255, null=True, blank=True)
    banner_image = models.ImageField(null=True, blank=True)

class Hero(models.Model):
    caption = models.CharField(max_length=255, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)

class Projects(NameSlugDescriptionBaseModel):
    title = models.CharField(max_length=255, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    logo = models.ImageField(null=True, blank=True)
    link = models.URLField(null=True, blank=True)
    notes = models.CharField(max_length=255, null=True, blank=True)
    status = models.CharField(
        max_length=20,
        choices=ProjectStatusChoices.choices,
        null=True,
        blank=True,
    )
    categories = models.CharField(
        max_length=50,
        choices=CategoriesChoices.choices,
        null=True,
        blank=True,
    )
    technologies = ArrayField(
        models.CharField(
            max_length=50,
            choices=TechChoices.choices
        ), blank=True,
        default=list
    )
    duration = models.CharField(
        max_length=20,
        choices=DurationsChoice,
        default=DurationsChoice.W8
    )

    def __str__(self):
        return f'{self.title}'


# Model for multiple image create.
class ProjectImage(models.Model):
    project = models.ForeignKey(Projects, on_delete=models.CASCADE, related_name="images")
    project_image = models.ImageField(null=True, blank=True)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ["order", "id"]


class Review(models.Model):
    user_name = models.CharField(max_length=255, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    rating = models.FloatField(null=True, blank=True)
    role = models.CharField(max_length=255, null=True, blank=True)

# Contact Model
class Contact(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=15, null=True, blank=True)
    contact_purpose = models.TextField(null=True, blank=True)
    address = models.CharField(max_length=255, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        ordering = ["-created_at"]