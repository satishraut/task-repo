from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter

from .views import (GenerViewSet, MovieViewSet,)

# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'gener', GenerViewSet)
router.register(r'movie', MovieViewSet)

# The API URLs are now determined automatically by the router.
# Additionally, we include the login URLs for the browseable API.
urlpatterns = [
    url(r'^', include(router.urls)),
]