from django.shortcuts import render,redirect, HttpResponse
from django.db.models import Q
from .models import Job
from .forms import JobForm
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required

# from django.http import FileResponse
# from django.utils.text import slugify
# Create your views here.

# for jobs
def jobs(request):
    posts = Job.objects.all()

    paginator = Paginator(posts, 3)
    page = request.GET.get('page')
    posts = paginator.get_page(page)

    return render(request,
                  'home/jobs.html',
                  {'posts': posts})


# for home view
def home(request):
	return render(request, 'home/home.html', {'title':'home'})


#for search

def search(request):
	if request.method == "GET":
		query = request.GET.get('q')
		jobs = get_data_queryset(str(query))
		return render(request,'home/jobs.html',context={'posts':jobs})
	else:
		return redirect('jobs')

def get_data_queryset(query=None):
    queryset = []
    queries = query.split(" ")
    for query in queries:
        jobs = Job.objects.filter(
            Q(title__icontains=query)
        )
        for job in jobs:
            queryset.append(job)

    return list(set(queryset))



# for adding jobs
@login_required
def add_Job(request):
	if request.method == "POST":
		form = JobForm(request.POST, request.FILES)
		print(request.FILES)
		if form.is_valid():
			#handle_uploaded_file(request.FILES['file'])
			form.save()
			return redirect('jobs')
		else:
			return HttpResponse('error')	
	else:
		form = JobForm()#object of Job as 'form'
		return render(request, 'home/add.html', {'form':form})


#for editing
def edit_Job(request, id):#to identify specific element we need to give pk as prameter
	item = Job.objects.get(id=id)
	form = JobForm(request.POST or None, instance=item)

	if form.is_valid():
		form.save()
		return redirect('jobs')

	return render(request, 'home/edit.html', {'form' : form, 'item' : item})	



# for deleting
def delete_Job(request, id):

	Job.objects.filter(id=id).delete()

	items = Job.objects.all()

	context = {
		'items' : items
	}

	return render(request, 'home/delete.html', context)		
