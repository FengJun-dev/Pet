from rest_framework import serializers
from Represent.models import Owner, Dog, Cat
from django.contrib.auth.models import User


class OwnerSerializer(serializers.HyperlinkedModelSerializer):
    dog = serializers.PrimaryKeyRelatedField(many=True, queryset=Dog.objects.all())
    cat = serializers.PrimaryKeyRelatedField(many=True, queryset=Cat.objects.all())

    class Meta:
        model = User
        fields = ('id', 'username', 'dog', 'cat')


class DogSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Dog
        fields = ('id', 'name', 'birth_date', 'owner')


class CatSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Cat
        fields = ('id', 'name', 'birth_date', 'owner')
