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
	gender = models.CharField(choices=GENDER_CHOICES, max_length=6)
	type = models.CharField(choices=TYPE_CHOICES, max_length=9)

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
	gender = models.CharField(choices=GENDER_CHOICES, max_length=6)
	company = models.CharField(max_length=50,  null=True)
	status = models.CharField(max_length=20,  null=True)
	type = models.CharField(choices=TYPE_CHOICES, max_length=9)

	def _str_(self):
		return self.user.username