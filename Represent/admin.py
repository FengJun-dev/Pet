from django.contrib import admin

# Register your models here.
from .models import Dog, Cat

Md = (Dog, Cat)
for m in Md:
    admin.site.register(m)