from django.conf.urls import url
from django.contrib.staticfiles.urls import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
	url(r'^map', views.map, name='map'),	
	url(r'^about', views.about, name='about'),
	url(r'^register', views.register, name='register'),
	#url(r'^izdelek/', views.izdelek, name='izdelek'),
	url(r'^izdelek/(?P<car_id>[0-9]+)/$', views.izdelek, name='izdelek'),
	#url(r'^profil/', views.profile, name='profile'),
	url(r'^profile/(?P<profile_id>[0-9]+)/$', views.profile, name='profile'),	
	url(r'^profile/(?P<profile_id>[0-9]+)/add/$', views.carAdd, name='carAdd'),
	url(r'^logout/', views.logout_user, name='logout'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)