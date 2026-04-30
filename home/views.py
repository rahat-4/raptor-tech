from django.shortcuts import get_object_or_404
from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.response import Response

from .models import (
    Home,
    Hero,
    Projects,
    Review,
    ProjectImage
)
from .serializers import (
    HomeSerializer,
    HeroSerializer,
    ProjectsSerializer,
    ReviewSerializer,
    ProjectImageSerializer
)
from rest_framework.exceptions import ValidationError
from .models import Home, Hero, Projects, Review, Contact
from .serializers import HomeSerializer, HeroSerializer, ProjectsSerializer, ReviewSerializer, ContactSerializer


# Generic views for Home
class HomeListCreateView(generics.ListCreateAPIView):
    queryset = Home.objects.all()
    serializer_class = HomeSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

class HomeRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Home.objects.all()
    serializer_class = HomeSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

# Generic views for Hero
class HeroListCreateView(generics.ListCreateAPIView):
    queryset = Hero.objects.all()
    serializer_class = HeroSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

class HeroRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Hero.objects.all()
    serializer_class = HeroSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

# Generic views for Projects
class ProjectsListCreateView(generics.ListCreateAPIView):
    queryset = Projects.objects.all().order_by("-id")
    serializer_class = ProjectsSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

class ProjectsRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Projects.objects.all()
    serializer_class = ProjectsSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    lookup_field = 'slug'


# Generic views for Review
class ReviewListCreateView(generics.ListCreateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

class ReviewRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

class ContactListCreateView(generics.ListCreateAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer


class ContactRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

