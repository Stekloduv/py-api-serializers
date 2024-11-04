from rest_framework import viewsets

from cinema.models import Movie, CinemaHall, Genre, Actor, MovieSession
from cinema.serializers import MovieSerializer, CinemaHallSerializer, GenreSerializer, ActorSerializer, \
    MovieListSerializer, MovieRetrieveSerializer, \
    MovieSessionListSerializer, MovieSessionSerializer, MovieSessionRetrieveSerializer


class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieListSerializer

    def get_serializer_class(self):
        if self.action == 'list':
            return MovieListSerializer
        elif self.action == 'retrieve':
            return MovieRetrieveSerializer

        return MovieSerializer

    def get_queryset(self):
        queryset = self.queryset
        if self.action == 'list':
            return queryset.prefetch_related('genres')

        return queryset


class CinemaHallViewSet(viewsets.ModelViewSet):
    queryset = CinemaHall.objects.all()
    serializer_class = CinemaHallSerializer


class GenreViewSet(viewsets.ModelViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer


class ActorViewSet(viewsets.ModelViewSet):
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer


class MovieSessionViewSet(viewsets.ModelViewSet):
    queryset = MovieSession.objects.all()

    def get_serializer_class(self):
        if self.action == 'list':
            return MovieSessionListSerializer
        elif self.action == 'retrieve':
            return MovieSessionRetrieveSerializer
        return MovieSessionSerializer
