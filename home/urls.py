from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name='home'),
    path('jobs/', views.jobs, name='jobs'),
    path('add_Job/', views.add_Job, name='add_Job'),
    path('edit_Job/<int:id>/', views.edit_Job, name='edit_Job'),
    path('delete_Job/<int:id>/', views.delete_Job, name='delete_Job'),
    path('search/', views.search, name='search'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)