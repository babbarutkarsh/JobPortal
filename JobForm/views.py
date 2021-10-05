from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User, auth
from .forms import applyModelForm
from .models import apply_job
from django.contrib import messages
 

def applyJob(request):
	return render(request, 'home/applyJob.html',)
 

def applyJob_detail(request):
	if request.method == 'POST':
		first_name = request.POST['first_name']
		last_name = request.POST['last_name']
		email = request.POST['email']
		age = request.POST['age']
		PhoneNo = request.POST['PhoneNo']
		Address = request.POST['Address']
		workexperience = request.POST['workexperience']
		otherskills = request.POST['otherskills']
		hobby = request.POST['hobby']
		if User.objects.filter(email=email).exists(): 
			messages.info(request,'Invalid email or taken!')
			return redirect('/applyjob')
		else:
			job = apply_job(email=email, first_name=first_name, last_name=last_name, work_experience=workexperience, age=age, PhoneNo=PhoneNo, Address=Address, other_skills=otherskills, hobby=hobby)
			job.save()


	return render(request, 'home/home.html')