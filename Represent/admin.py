from django.contrib import admin

# Register your models here.
from .models import Dog, Cat, Owner

Md = [Dog, Cat, Owner]
for m in Md:
    admin.site.register(m)