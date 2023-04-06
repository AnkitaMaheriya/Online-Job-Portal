# from django.http.response import HttpResponse
from django.shortcuts import render, redirect
# from django.http import HttpResponse
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

# Create your views here.
def index(request):
	return render(request, 'index.html')

def admin_login(request):
	error = ""

	if request.method == "POST":
		uname = request.POST['uname'];
		pwd = request.POST['pwd'];
		user = authenticate(username = uname, password = pwd)

		try:
			if user.is_staff:
				login(request,user)
				error="no"
			else:
				error="yes"

		except:
			error="yes"
	else:
		error="yes"


	d = {'error' : error}
	return render(request, 'admin_login.html', d)

def jobseeker_login(request):
	error = ""

	if request.method == "POST":
		uname = request.POST['uname'];
		pwd = request.POST['pwd'];
		user = authenticate(username = uname, password = pwd)

		if user:
			try:
				user1 = JobseekerUser.objects.get(user=user)

				if user1.type == "Jobseeker":
					login(request,user)
					error="no"
				else:
					error="yes"

			except:
				error="yes"
		else:
			error="yes"


	d = {'error' : error}
	return render(request, 'jobseeker_login.html', d)

def recruiter_login(request):
	error = ""

	if request.method == "POST":
		uname = request.POST['uname'];
		pwd = request.POST['pwd'];
		user = authenticate(username = uname, password = pwd)

		if user:
			try:
				user1 = Recruiter.objects.get(user=user)

				if user1.type == "Recruiter":
					login(request,user)
					error="no"
				else:
					error="not"

			except:
				error="yes"
		else:
			error="yes"


	d = {'error' : error}
	return render(request, 'recruiter_login.html', d)

def jobseeker_signup(request):
	error=""

	if request.method == 'POST':
		fname = request.POST['fname'];
		lname = request.POST['lname'];
		image = request.FILES['img'];
		pwd = request.POST['pwd'];
		email = request.POST['email'];
		contact = request.POST['contact'];
		gender = request.POST['gender'];

		try:
			user = User.objects.create_user(first_name=fname, last_name=lname, username=email, password=pwd)
			JobseekerUser.objects.create(user=user, mobile=contact, image=image, gender=gender, type="Jobseeker")
			error="no"

		except:
			error="yes"

		# if error == "no":
		# 	user.save()
		# 	messages.success(request, "Signed Up Successfully...!!")
		# 	return redirect('jobseeker_login')	
		# elif error == "yes":
		# 	messages.success("Something went Wrong, Try Again...!!")
		
	d = {'error' : error} # dictionary

	return render(request, 'jobseeker_signup.html', d)

def recruiter_signup(request):
	error=""

	if request.method == 'POST':
		fname = request.POST['fname'];
		lname = request.POST['lname'];
		image = request.FILES['img'];
		pwd = request.POST['pwd'];
		email = request.POST['email'];
		contact = request.POST['contact'];
		gender = request.POST['gender'];
		company = request.POST['company'];

		try:
			user = User.objects.create_user(first_name=fname, last_name=lname, username=email, password=pwd)
			Recruiter.objects.create(user=user, mobile=contact, image=image, gender=gender, company=company, type="Recruiter")
			error="no"

		except:
			error="yes"

	d = {'error' : error} # dictionary

	return render(request, 'recruiter_signup.html', d)

def jobseeker_home(request):
	if not request.user.is_authenticated:
		return redirect('jobseeker_login')
	return render(request, 'jobseeker_home.html')

def recruiter_home(request):
	if not request.user.is_authenticated:
		return redirect('recruiter_login')
	return render(request, 'recruiter_home.html')

def admin_home(request):
	if not request.user.is_authenticated:
		return redirect('admin_login')
	return render(request, 'admin_home.html')

def Logout(request):
	logout(request)
	return redirect('index')

def view_jobseeker(request):
	if not request.user.is_authenticated:
		return redirect('jobseeker_login')
	
	data = JobseekerUser.objects.all()

	d = {'data' : data}
	return render(request, 'view_jobseeker.html', d)

def view_recruiter(request):
	if not request.user.is_authenticated:
		return redirect('recruiter_login')
	return render(request, 'recruiter_home.html')

def delete_jobseeker(request, pid):	
	jobseeker = JobseekerUser.objects.get(id=pid)
	jobseeker.delete()

	return redirect('view_jobseeker')