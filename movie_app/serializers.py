from rest_framework import serializers
from .models import Movie, Genre

from rest_framework.permissions import AllowAny, IsAdminUser

class GenreSerializer(serializers.ModelSerializer):
    """
    Serializer for Genre model
    """
    class Meta:
        model = Genre
        fields = '__all__'

class MovieSerializer(serializers.ModelSerializer):
    """
    Serializer for Movie model
    """
    class Meta:
        model = Movie
        fields = '__all__'

    