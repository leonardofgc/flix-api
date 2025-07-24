from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework import generics
from movies.models import Movie
from movies.serializers import MovieModelSerializer

class MovieCreateListView(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated, IsAdminUser)
    queryset = Movie.objects.all()
    serializer_class = MovieModelSerializer

class MovieRetriveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated, IsAdminUser)
    queryset = Movie.objects.all()
    serializer_class = MovieModelSerializer