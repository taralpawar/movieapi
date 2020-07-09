from django.shortcuts import render
from .models import MovieList
from .serializers import movieSerializers
from rest_framework import viewsets, permissions


class movieView(viewsets.ModelViewSet):
    queryset = MovieList.objects.all()
    serializer_class = movieSerializers


# class watchView(viewsets.ModelViewSet):
#     queryset = Watch.objects.all()
#     serializer_class = watchSerializers

# class polularView(viewsets.ModelViewSet):
#     queryset = PopularList.objects.all()
#     serializer_class = popularSerializers
#     #permission_classes = (permissions.IsAdminUser,)


# class latestView(viewsets.ModelViewSet):
#     queryset = LatestList.objects.all()
#     serializer_class = latestSerializers
