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
    birth_date = models.DateField(blank=True, null=True)
    owner = models.ForeignKey('auth.User', related_name='dog', on_delete=models.CASCADE)

    class Meta:
        ordering = ('id',)

    def __str__(self):
        return 'id="{id}" name="{name}"'.format(
            id=self.id,
            name=self.name,
        )


class Cat(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(unique=True, max_length=100)
    birth_date = models.DateField(blank=True, null=True)
    owner = models.ForeignKey('auth.User', related_name='cat', on_delete=models.CASCADE)

    class Meta:
        ordering = ('id',)

    def __str__(self):
        return 'id="{id}" name="{name}"'.format(
            id=self.id,
            name=self.name,
        )