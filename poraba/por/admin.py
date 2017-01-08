from django.contrib import admin

# Register your models here.
from .models import Car,Profile

admin.site.register(Car)
admin.site.register(Profile)