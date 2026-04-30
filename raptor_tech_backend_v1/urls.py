"""
URL configuration for raptor_tech_backend_v1 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularRedocView,
    SpectacularSwaggerView,
)
from rest_framework import permissions

import home
from authentication.views import (
    CustomTokenObtainPairView,
    UserListCreateAPIView,
    UserRetrieveUpdateDestroyAPIView
)

urlpatterns = [
    path("admin/raptor/v1/", admin.site.urls),
    path("auth/", include("djoser.urls")),
    path("user/list/", UserListCreateAPIView.as_view(), name="user-list-create-api"),
    path("user/list/<int:pk>/", UserRetrieveUpdateDestroyAPIView.as_view(), name="user-retrieve-update-api"),
    path("auth/", include("djoser.urls.jwt")),
    path("auth/jwt/custom/create/", CustomTokenObtainPairView.as_view(), name="custom_token_obtain_pair"),
    path("blog/", include("blog.urls")),
    path("", include("home.urls")),

    path("root/update/", include("home.urls")),
]

if settings.DEBUG:
    import debug_toolbar

    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

    urlpatterns = [
        path("__debug__/", include(debug_toolbar.urls)),
        path("silk/", include("silk.urls", namespace="silk")),
    ] + urlpatterns

    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    # drf yasg api documentation
    from drf_yasg.views import get_schema_view
    from drf_yasg import openapi

    schema_view = get_schema_view(
        openapi.Info(
            title="CRM API",  # Replace with your API title
            default_version="v1",  # Replace with your API version
            description="API documentation for the CRM Backend",  # Optional description
            terms_of_service="https://www.example.com/terms/",  # Optional terms URL
            contact=openapi.Contact(
                email="support@example.com"
            ),  # Optional contact email
            license=openapi.License(name="MIT License"),  # Optional license info
        ),
        public=True,
        permission_classes=[
            permissions.AllowAny,
        ],
    )
    urlpatterns += [
        path(
            "swagger<format>/",
            schema_view.without_ui(cache_timeout=0),
            name="schema-json",
        ),
        path(
            "api/docs",
            schema_view.with_ui("swagger", cache_timeout=0),
            name="schema-swagger-ui",
        ),
        path(
            "redoc/", schema_view.with_ui("redoc", cache_timeout=0), name="schema-redoc"
        ),
    ]
