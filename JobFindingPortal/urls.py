from django.contrib import admin
from django.urls import path, include #for including home.urls
from Accounts.views import register, login, logout
from JobForm.views import applyJob_detail, applyJob

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls')),
	path('register/', register, name='register'),
    path('login/', login, name='login'),
    path('logout/', logout, name='logout'),
    path('applyjob/', applyJob, name='applyJob'),
    path('applyJob_detail/', applyJob_detail ,name="applyJob_detail"),
]
