from django.db import models

# Create your models here.


class Owner(models.Model):
    id = models.AutoField(primary_key=True)
    email = models.EmailField(unique=True)
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    password = models.CharField(max_length=128, null=True, blank=True, default=None)

    @property
    def full_name(self):
        return '{0} {1}'.format(self.first_name, self.last_name)

    def __str__(self):
        return 'id="{id}" email="{email}" name="{name}"'.format(
            id=self.id,
            email=self.email,
            name=self.full_name,
        )


class Dog(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(unique=True, max_length=100)
    birthday_year = models.IntegerField(max_length=4)
    birthday_month = models.IntegerField(max_length=2)
    birthday_day = models.IntegerField(max_length=2)
    owner = models.ForeignKey(Owner, on_delete=models.CASCADE)

    @property
    def birthday(self):
        return '{0}-{1}-{2}'.format(self.birthday_year, self.birthday_month, self.birthday_day)

    def __str__(self):
        return 'id="{id}" name="{name}"'.format(
            id=self.id,
            name=self.name,
        )


class Cat(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(unique=True, max_length=100)
    birthday_year = models.IntegerField(max_length=4)
    birthday_month = models.IntegerField(max_length=2)
    birthday_day = models.IntegerField(max_length=2)
    owner = models.ForeignKey(Owner, on_delete=models.CASCADE)

    @property
    def birthday(self):
        return '{0}-{1}-{2}'.format(self.birthday_year, self.birthday_month, self.birthday_day)

    def __str__(self):
        return 'id="{id}" name="{name}"'.format(
            id=self.id,
            name=self.name,
        )