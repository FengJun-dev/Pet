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
"""class OwnerViewSet(RetrieveModelMixin, UpdateModelMixin):
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
        owner_query = Owner.objects.get(email__exact=owner_email)
        if owner_query
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
        ))"""


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