from .models import Movie, Genre
from .serializers import MovieSerializer, GenreSerializer
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticatedOrReadOnly
# Create your views here.
class GenerViewSet(ModelViewSet):
    """
    API view for searching Movies
    """
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer

class MovieViewSet(ModelViewSet):
    """
    API view for searching Movies
    """
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
