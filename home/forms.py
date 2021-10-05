from django import forms
from .models import Job
#this form is for adding data in the table
class JobForm(forms.ModelForm):
	class Meta:
		model = Job
		fields = ('title', 'details', 'date_posted', 'job_description','gform_link')