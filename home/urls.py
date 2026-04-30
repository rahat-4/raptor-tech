from django.urls import path
from .views import (
    HomeListCreateView, HomeRetrieveUpdateDestroyView,
    HeroListCreateView, HeroRetrieveUpdateDestroyView,
    ProjectsListCreateView, ProjectsRetrieveUpdateDestroyView,
    ReviewListCreateView, ReviewRetrieveUpdateDestroyView,ReviewListCreateView,
    ReviewRetrieveUpdateDestroyView, ContactListCreateView, ContactRetrieveUpdateDestroyView

)

urlpatterns = [
    # URLs for Home
    path('home/', HomeListCreateView.as_view(), name='home-list-create'),
    path('home/<int:pk>/', HomeRetrieveUpdateDestroyView.as_view(), name='home-retrieve-update-destroy'),

    # URLs for Hero
    path('hero/', HeroListCreateView.as_view(), name='hero-list-create'),
    path('hero/<int:pk>/', HeroRetrieveUpdateDestroyView.as_view(), name='hero-retrieve-update-destroy'),

    # URLs for Projects
    path('portfolios/', ProjectsListCreateView.as_view(), name='projects-list-create'),
    path('portfolios/<slug:slug>/', ProjectsRetrieveUpdateDestroyView.as_view(), name='projects-retrieve-update-destroy'),

    # URLs for Review
    path('review/', ReviewListCreateView.as_view(), name='review-list-create'),
    path('review/<int:pk>/', ReviewRetrieveUpdateDestroyView.as_view(), name='review-retrieve-update-destroy'),
    path('contact/', ContactListCreateView.as_view(), name='contact-list-create'),
    path('contact/<int:pk>/', ContactRetrieveUpdateDestroyView.as_view(), name='contact-retrieve-update-destroy'),
]
