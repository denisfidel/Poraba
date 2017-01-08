from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
	url(r'^map', views.map, name='map'),	
	url(r'^about', views.about, name='about'),
	url(r'^register', views.register, name='register'),
	url(r'^izdelek/', views.izdelek, name='izdelek'),
	url(r'^profil/', views.profile, name='profile'),
]	