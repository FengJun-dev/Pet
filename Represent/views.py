from django.shortcuts import render
from rest_framework.views import APIView
from django.contrib.auth.decorators import login_required
from Represent.models import Owner, Dog, Cat
from rest_framework.response import Response
from rest_framework import status, mixins
from django.http import Http404
from Represent.serializers import OwnerSerializer, DogSerializer, CatSerializer
from rest_framework import generics


# Create your views here.
class DogList(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
    queryset = Dog.objects.all()
    serializer_class = DogSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    @login_required
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class DogDetail(mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin, generics.GenericAPIView):
    queryset = Cat.objects.all()
    serializer_class = DogSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    @login_required
    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    @login_required
    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


class CatList(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
    queryset = Cat.objects.all()
    serializer_class = CatSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    @login_required
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class CatDetail(mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin, generics.GenericAPIView):
    queryset = Cat.objects.all()
    serializer_class = CatSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    @login_required
    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    @login_required
    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)