from django.forms import ModelForm
from .models import apply_job
 
class applyModelForm(ModelForm):
	class meta:
		model = apply_job
		fields=('first_name','last_name','email', 'Age', 'PhoneNo', 'Address','work_experience','other_skills')