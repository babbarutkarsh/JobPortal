from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User, auth
from django.http import HttpResponse, JsonResponse
import json


def register(request):
	if request.method == 'POST':
		first_name= request.POST['first_name']
		last_name= request.POST['last_name']
		username= request.POST['username']
		email= request.POST['email']
		password1= request.POST['password1']
		password2= request.POST['password2']
		if password1==password2:
			if User.objects.filter(username=username).exists():
				messages.info(request,'Invalid Username!')
				return redirect('/register')
			elif User.objects.filter(email=email).exists(): 
				messages.info(request,'Invalid Email!')
				return redirect('/register')
			else:
				user= User.objects.create_user(username=username, password=password1, email=email, first_name=first_name, last_name=last_name)
				user.save()
				messages.success(request, 'Your account have been created. Now you can login !!')
				return redirect('login')
		else:
			messages.info(request,'Password didn\'t match')
			return redirect('/register')
	else:
		return render(request, 'home/register.html')

def login(request):
	if request.method == 'POST':
		username= request.POST['username']
		password= request.POST['password']

		user = auth.authenticate(username=username, password=password)
		if user is not None:
			auth.login(request,user)
			return redirect('/')
		else:
			messages.info(request, 'Wrong user name or password')
			return redirect('/login')

	else:
		return render(request, 'home/login.html')

def logout(request):
    auth.logout(request)
    return redirect("/")