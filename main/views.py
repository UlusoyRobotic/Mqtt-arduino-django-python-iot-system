from django.shortcuts import render,HttpResponse
from django.http import JsonResponse
from . import models

# Create your views here.
def post_view(request):
	return render(request,'post.html')
	#return render(request,'post.html',JsonResponse(context))

def home_view(request):
	return render(request,'home.html')

def database_view(request):
	datalar = models.Data_database.objects.all()
	#vericek = models.Data_database.objects.filter(system_name='Esp')
	#vericek = models.Data_database.objects.filter(system_name='Computer')
	return render(request,'database.html',{'datalar':datalar})

