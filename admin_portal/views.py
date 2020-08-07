from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from django.contrib.auth.models import User,auth
#from .models import Destination
from django.core import serializers
# Create your views here.
def admin_portal(request):
	return render(request,"budget_item.html")

def table(request):
	return render(request,"chief.html")

def login(request):
	if request.method == 'POST':
		username=request.POST['username']
		password=request.POST['password']
		user=auth.authenticate(username=username,password=password)
		if user is not None:
			auth.login(request,user)
			return redirect("/")
		else:
			messages.info(request,'invalid credentials')
			return redirect("/")
	else:
		return render(request,'deputy_chief.html')

		 


	