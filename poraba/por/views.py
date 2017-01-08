from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, "por/index.html")
	
def map(request):
	return render(request, "por/map.html")
	
def about(request):
	return render(request, "por/about.html")
	
def izdelek(request):
	return render(request, "por/izdelek.html")

def profile(request):
	return render(request, "por/profile.html")

def register(request):
	return render(request, "por/login.html")