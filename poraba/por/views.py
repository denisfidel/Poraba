from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse

from django.contrib.auth import authenticate, login, logout

from .models import Car, Profile, Comments
from .forms import LoginForm, UserForm, ProfileForm, CarAddForm, CommentAddForm

from django.db.models import Q

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Create your views here.
def index(request):
	context = {}
	car_list = Car.objects.order_by('brand')
	paginator=Paginator(car_list, 5)
	page = request.GET.get('page')
	
	#prijava
	if request.method=='POST':
		form = LoginForm(request.POST)
		if form.is_valid():
			user = authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['password'] )
			if user is not None:
				login(request, user)
	
	
	if request.method=='GET':
		#srearch
		search_query=request.GET.get("q", None)
		results=Car.objects.all().filter(Q(brand=search_query) | Q(car_model=search_query))
		context['results']=results
		
		#kalkulator stroskov
		trenutna_poraba=request.GET.get("tmp_poraba", None)
		st_kilom2=request.GET.get("st_kilometrov", None)
		cena=1.2
		if trenutna_poraba and st_kilom2:
			trenutna_poraba_num=float(trenutna_poraba)
			st_kilom2_num=int(st_kilom2)
			stroski2=trenutna_poraba_num*(st_kilom2_num/100)*cena
			context['stroski2']=stroski2
			
		#kalkulator porabe
		gorivo=request.GET.get("kolicina_goriva", None)
		st_kilom=request.GET.get("kilometri", None)
		if gorivo and st_kilom:
			gorivo_num=int(gorivo)
			st_kilom_num=int(st_kilom)
			kolicik=st_kilom_num/100
			
			context['avg_poraba']=gorivo_num/kolicik

	#ostranjevanje
	try:
		cars = paginator.page(page)
	except PageNotAnInteger:
        # If page is not an integer, deliver first page.
		cars = paginator.page(1)
	except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
		cars = paginator.page(paginator.num_pages)
	
	context['car_list'] = car_list
	context['loginForm'] = LoginForm()	
	context['cars']=cars
	
	return render(request,"por/index.html",context)
	
def map(request):
	return render(request, "por/map.html")
	
def about(request):
	return render(request, "por/about.html")
	
def izdelek(request, car_id):
	context = {'loginForm':LoginForm()}
	
	c=Car.objects.get(pk=car_id)
	context['car']=c
	#seznam komentarjev
	comment_list=Comments.objects.all().filter(car=c)
	context['comment_list']=comment_list
	#ostranjevanje
	paginator=Paginator(comment_list, 5)
	page = request.GET.get('page')
	
	#dodajanje komentarja
	if request.method=='POST':
		form=CommentAddForm(request.POST)
		if form.is_valid():
			com=form.save(commit=False)
			com.car=c
			com.author=c.owner
			com.save()
	else:
		form=CommentAddForm()
	
	#ostranjevanje
	try:
		comments = paginator.page(page)
	except PageNotAnInteger:
        # If page is not an integer, deliver first page.
		comments = paginator.page(1)
	except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
		comments = paginator.page(paginator.num_pages)
		
	context['form']=form
	context['comments']=comments
	return render(request, "por/izdelek.html", context)

def profile(request, profile_id):	
	context = {'loginForm':LoginForm()}
	
	profile=Profile.objects.get(pk=profile_id)
	context['profile']=profile
	
	car_list=Car.objects.all().filter(owner=profile)
	context['car_list']=car_list
	
	return render(request, "por/profile.html", context)
	
def carAdd(request, profile_id):
	context={}
	
	profile=Profile.objects.get(pk=profile_id)
	context['profile']=profile
	
	if request.method=='POST':
		form=CarAddForm(request.POST, request.FILES)
		if form.is_valid():
			car=form.save(commit=False)
			car.owner=profile
			car.save()
			return HttpResponseRedirect(reverse('index'))
				
	else:
		form=CarAddForm()
		
	context['form']=form
	return render(request, "por/carAdd.html", context)

def register(request):
	context={}
	if request.method=='POST':
		uf = UserForm(request.POST, prefix='user')
		pf = ProfileForm(request.POST, prefix='profile')
		#form=UserForm(request.POST)
		#if form.is_valid():
			#todo
		if uf.is_valid() * pf.is_valid():
			user=uf.save()
			profile=pf.save(commit=False)
			profile.user=user
			profile.save()
			return HttpResponseRedirect(reverse('index'))
		#if form.is_valid:
			#form.save()
			#return HttpResponseRedirect(reverse('index'))
			
	else:
		uf = UserForm(prefix='user')
		pf = ProfileForm(prefix='profile')
		#form=UserForm()
	
	context['user']=uf
	context['profile'] = pf
	#context['form']=form
	return render(request, "por/login.html", context)
	
def logout_user(request):
	logout(request)
	return HttpResponseRedirect(reverse('index'))