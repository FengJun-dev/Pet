from django.shortcuts import render
from rest_framework.views import APIView
from django.contrib.auth.decorators import login_required
from Represent.models import Owner, Dog, Cat
from rest_framework.response import Response
from Represent.serializers import OwnerSerializer, DogSerializer, CatSerializer
from rest_framework.mixins import RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin
from rest_framework import generics


# Create your views here.
class DogList(APIView):
    def get(self, request, format=None):
        dog = Dog.objects.all()
        serializer = DogSerializer(dog, many=True)
        return Response(serializer.data)

    @login_required
    def post(self, request, format=None):
        serializer = SnippetSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)