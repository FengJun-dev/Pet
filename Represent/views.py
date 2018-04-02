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
class GenericAPIView(InternalGenericAPIView, APIView):
    lookup_field = 'id'

    @classmethod
    def as_view(cls, **initkwargs):
        return APIView.as_view(**initkwargs)


class ViewSetMixin(InternalViewSetMixin):

    @classmethod
    def as_view(cls, actions=None, **initkwargs):
        view = super(ViewSetMixin, cls).as_view(actions=actions, **initkwargs)
        view.cls = cls
        view.initkwargs = initkwargs
        view.suffix = initkwargs.get('suffix', None)
        view.actions = actions
        for decorator in cls.decorators:
            view = decorator(view)
        return view


class GenericViewSet(ViewSetMixin, GenericAPIView):
    pass


class OwnerViewSet(RetrieveModelMixin, UpdateModelMixin, GenericViewSet):
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
        self.send_user_update_notification(request)
        return response

    @login_required
    def destroy(self, request, *args, **kwargs):
        owner = self.get_object()
        # delete owner
        owner.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    @detail_route(methods=['post'])
    def signup(self, request, *args, **kwargs):
        email, password = self.validate_email_and_password_submitted(request)
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
        owner = self.validate_user_credentials(request)
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