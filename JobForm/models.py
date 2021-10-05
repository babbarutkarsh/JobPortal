from django.db import models

# Create your models here.
 
class apply_job(models.Model):
	first_name =models.CharField(max_length=40)
	last_name =models.CharField(max_length=40)
	email =models.CharField(max_length=50)
	age =models.IntegerField()
	PhoneNo = models.IntegerField()
	Address= models.TextField()
	work_experience =models.TextField()
	other_skills =models.TextField()
	hobby =models.TextField()
	college =models.TextField()

	def __str__(self):
		return self.first_name