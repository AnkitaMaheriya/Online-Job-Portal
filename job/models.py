from django.db import models
from django.contrib.auth.models import User
# from django import forms 

# Create your models here.

class JobseekerUser(models.Model):
	GENDER_CHOICES = (
   		('Male', 'Male'),
   		('Female', 'Female'),
		('Other', 'Other')
	)

	TYPE_CHOICES = (
   		('Jobseeker', 'Jobseeker'),
   		('Recruiter', 'Recruiter')
	)
	
	"""docstring for JobseekerUser"""
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	mobile = models.IntegerField(null=True)
	image = models.FileField(null=True)
	gender = models.CharField(choices=GENDER_CHOICES, max_length=6, default="Male")
	type = models.CharField(choices=TYPE_CHOICES, max_length=9, default="Jobseeker")

	def _str_(self):
		return self.user.username

	
class Recruiter(models.Model):
	GENDER_CHOICES = (
   		('Male', 'Male'),
   		('Female', 'Female'),
		('Other', 'Other')
	)

	TYPE_CHOICES = (
   		('Jobseeker', 'Jobseeker'),
   		('Recruiter', 'Recruiter')
	)
	
	"""docstring for Recruiter"""
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	mobile = models.IntegerField(null=True)
	image = models.FileField(null=True)
	gender = models.CharField(choices=GENDER_CHOICES, max_length=6, default="Male")
	company = models.CharField(max_length=50,  null=True)
	type = models.CharField(choices=TYPE_CHOICES, max_length=9, default="Recruiter")

	def _str_(self):
		return self.user.username

class Job(models.Model):
	
	"""docstring for Job"""
	recruiter = models.ForeignKey(Recruiter, on_delete=models.CASCADE)
	start_date = models.DateField()
	end_date = models.DateField()
	title = models.CharField(max_length=100, null=True)
	salary = models.IntegerField()
	image = models.FileField()
	description = models.CharField(max_length=300)
	experience = models.CharField(max_length=3)
	location = models.CharField(max_length=100)
	skills = models.CharField(max_length=100)
	creation_date = models.DateField()

	def _str_(self):
		return self.title