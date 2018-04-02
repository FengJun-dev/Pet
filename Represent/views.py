from django.shortcuts import render
from rest_framework.views import APIView
from django.contrib.auth.decorators import login_required
from Represent.models import Owner, Dog, Cat
from rest_framework.response import Response
from rest_framework import status, mixins
from rest_framework.decorators import detail_route
from django.http import Http404
from Represent.serializers import OwnerSerializer, DogSerializer, CatSerializer
from rest_framework.mixins import RetrieveModelMixin, UpdateModelMixin
from rest_framework import generics
from rest_framework.exceptions import ValidationError
from django.contrib import auth
from rest_framework.generics import GenericAPIView as InternalGenericAPIView
from rest_framework.viewsets import ViewSetMixin as InternalViewSetMixin


# Create your views here.
class OwnerViewSet(RetrieveModelMixin, UpdateModelMixin):
    serializer_class = OwnerSerializer
    lookup_field = None

    def get_object(self):
        return self.request.user

    @login_required
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    @login_required
    def update(self, request, *args, **kwargs):
        response = super().update(request, *args, **kwargs)
        self.get_object.update(request)
        return response

    @login_required
    def destroy(self, request, *args, **kwargs):
        owner = self.get_object()
        # delete owner
        owner.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    @detail_route(methods=['post'])
    def signup(self, request, *args, **kwargs):
        email = request.data.get('email')
        password = request.data.get('password')
        first_name = request.data.get('first_name')
        last_name = request.data.get('last_name')
        username = request.data.get('username')
        owner = Owner.objects.filter(username=username)
        try:
            owner = Owner.objects.create_user(
                username=username,
                email=email,
                password=password,
                first_name=first_name,
                last_name=last_name,
            )
        except Exception as e:
            raise ValidationError(str(e))
            # login
        auth.login(request, owner)
        serializer = self.serializer_class(request.owner)
        res = serializer.data
        res['success'] = True
        return Response(res, status=status.HTTP_201_CREATED)

    @detail_route(methods=['post'])
    def login(self, request, *args, **kwargs):
        owner_email = request.data.get('email')
        owner_query_set = Owner.objects.filter('owner_email')
        if owner_email ==
        # login
        auth.login(request, owner)

        serializer = self.serializer_class(request.owner)
        res = serializer.data
        res['success'] = True
        return Response(res)

    @login_required
    @detail_route(methods=['post'])
    def logout(self, request, *args, **kwargs):
        auth.logout(request)
        res = dict(
            success=True,
        )
        return Response(res)

    @detail_route(methods=['get'])
    def authentication(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            serializer = self.serializer_class(self.get_object())
            data = serializer.data
            data['is_authenticated'] = True
            return Response(data)
        return Response(dict(
            is_authenticated=False,
        ))


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