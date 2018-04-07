from Represent.models import Dog, Cat
from Represent.serializers import DogSerializer, CatSerializer, OwnerSerializer
from rest_framework import generics
from django.contrib.auth.models import User
from rest_framework import permissions, viewsets
from Represent.permissions import IsOwnerOrReadOnly
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse

# Create your views here.


class OwnerViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = User.objects.all()
    serializer_class = OwnerSerializer


class DogViewSet(viewsets.ModelViewSet):
    queryset = Dog.objects.all()
    serializer_class = DogSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly,)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class CatViewSet(viewsets.ModelViewSet):
    queryset = Dog.objects.all()
    serializer_class = CatSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly,)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)