from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

from django.contrib.postgres.fields import ArrayField

from datetime import datetime

# Create your models here.

	

class Profile(models.Model):
	user=models.OneToOneField(User, on_delete=models.CASCADE)
	pic=models.ImageField(upload_to='profiles/', null=True, blank=True)
	

class Car(models.Model):
	owner=models.ForeignKey(Profile, on_delete=models.SET_NULL, null=True)
	fuel_consumption=models.DecimalField(max_digits=3, decimal_places=1)
	brand=models.CharField(max_length=20)
	car_model=models.CharField(max_length=20)
	year=models.IntegerField(null=True, blank=True)
	kilometers=models.IntegerField(null=True, blank=True)
	rotation_speed=models.IntegerField(blank=True, null=True)
	image=models.ImageField(upload_to='cars/', null=True, blank=True)
	
class Comments(models.Model):
	comment=models.TextField()
	author=models.ForeignKey(Profile, on_delete=models.SET_NULL, null=True)
	pub_date=models.DateTimeField( default=datetime.now )
	car=models.ForeignKey( Car, on_delete=models.CASCADE )
	