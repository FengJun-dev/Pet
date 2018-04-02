from rest_framework import serializers
from Represent.models import Owner, Dog, Cat


class OwnerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Owner
        fields = ('id', 'username', 'first_name', 'last_name', 'email')
        read_only_fields = ('id',)


class DogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dog
        fields = ('id', 'name', 'birthday_year', 'birthday_month', 'birthday_day', 'owner')


class CatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cat
        fields = ('id', 'name', 'birthday_year', 'birthday_month', 'birthday_day', 'owner')