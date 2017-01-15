from django.contrib import admin

# Register your models here.
from .models import Car,Profile, Comments

admin.site.register(Car)
admin.site.register(Profile)
admin.site.register(Comments)