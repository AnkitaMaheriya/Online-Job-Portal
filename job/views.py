# from django.http.response import HttpResponse
from django.shortcuts import render, redirect
# from django.http import HttpResponse
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from datetime import date

# Create your views here.
def index(request):
	return render(request, 'index.html')

def admin_login(request):
	error = ""

	if request.method == "POST":
		uname = request.POST['uname']
		pwd = request.POST['pwd']
		user = authenticate(username = uname, password = pwd)

		if user.is_staff:
			login(request,user)
			error="no"
		else:
			error="yes"

	else:
		error="yes"

	d = {'error' : error}
	return render(request, 'admin_login.html', d)

def jobseeker_login(request):
	error = ""

	if request.method == "POST":
		uname = request.POST['uname']
		pwd = request.POST['pwd']
		user = authenticate(username = uname, password = pwd)

		if user:
			user1 = JobseekerUser.objects.get(user=user)

			if user1.type == "Jobseeker":
				login(request,user)
				error="no"
			else:
				error="yes"
		else:
			error="yes"


	d = {'error' : error}
	return render(request, 'jobseeker_login.html', d)

def recruiter_login(request):
	error = ""

	if request.method == "POST":
		uname = request.POST['uname']
		pwd = request.POST['pwd']
		user = authenticate(username = uname, password = pwd)

		if user:
			user1 = Recruiter.objects.get(user=user)

			if user1.type == "Recruiter":
				login(request,user)
				error="no"
			else:
				error="yes"
		else:
			error="yes"

	d = {'error' : error}
	return render(request, 'recruiter_login.html', d)

def jobseeker_signup(request):
	error=""

	if request.method == 'POST':
		fname = request.POST['fname']
		lname = request.POST['lname']
		image = request.FILES['img']
		pwd = request.POST['pwd']
		email = request.POST['email']
		contact = request.POST['contact']
		gender = request.POST['gender']

		try:
			user = User.objects.create_user(first_name=fname, last_name=lname, username=email, password=pwd)
			JobseekerUser.objects.create(user=user, mobile=contact, image=image, gender=gender, type="Jobseeker")
			error="no"

		except:
			error="yes"
		
	d = {'error' : error} # dictionary

	return render(request, 'jobseeker_signup.html', d)

def recruiter_signup(request):
	error=""

	if request.method == 'POST':
		fname = request.POST['fname']
		lname = request.POST['lname']
		image = request.FILES['img']
		pwd = request.POST['pwd']
		email = request.POST['email']
		contact = request.POST['contact']
		gender = request.POST['gender']
		company = request.POST['company']

		
		user = User.objects.create_user(first_name=fname, last_name=lname, username=email, password=pwd)
		Recruiter.objects.create(user=user, mobile=contact, image=image, gender=gender, company=company, type="Recruiter")
		error="no"

	else:
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

	data = Recruiter.objects.all()

	d = {'data' : data}
	return render(request, 'view_recruiter.html', d)

def delete_jobseeker(request, pid):	
	jobseeker = User.objects.get(id=pid)
	jobseeker.delete()

	return redirect('view_jobseeker')

def delete_recruiter(request, pid):	
	recruiter = User.objects.get(id=pid)
	recruiter.delete()

	return redirect('view_recruiter')

def change_password_admin(request):
	if not request.user.is_authenticated:
		return redirect('admin_login')

	error=""

	if request.method == 'POST':
		currentpwd = request.POST['currentpwd']
		newpwd = request.POST['newpwd']

		try:
			user = User.objects.get(id = request.user.id)

			if user.check_password(currentpwd):
				user.set_password(newpwd)
				user.save()

				error="no"
			
			else:
				error="not"

		except:
			error="yes"

	d = {'error' : error} # dictionary

	return render(request, 'change_password_admin.html', d)

def change_password_jobseeker(request):
	if not request.user.is_authenticated:
		return redirect('jobseeker_login')

	error=""

	if request.method == 'POST':
		currentpwd = request.POST['currentpwd']
		newpwd = request.POST['newpwd']

		try:
			user = User.objects.get(id = request.user.id)

			if user.check_password(currentpwd):
				user.set_password(newpwd)
				user.save()

				error="no"
			
			else:
				error="not"

		except:
			error="yes"

	d = {'error' : error} # dictionary

	return render(request, 'change_password_jobseeker.html', d)

def change_password_recruiter(request):
	if not request.user.is_authenticated:
		return redirect('recruiter_login')

	error=""

	if request.method == 'POST':
		currentpwd = request.POST['currentpwd']
		newpwd = request.POST['newpwd']

		try:
			user = User.objects.get(id = request.user.id)

			if user.check_password(currentpwd):
				user.set_password(newpwd)
				user.save()

				error="no"
			
			else:
				error="not"

		except:
			error="yes"

	d = {'error' : error} # dictionary

	return render(request, 'change_password_recruiter.html', d)

def post_job(request):
	if not request.user.is_authenticated:
		return redirect('recruiter_login')

	error=""

	if request.method == 'POST':
		job_title = request.POST.get('job_title')
		start_date = request.POST.get('start_date')
		end_date = request.POST.get('end_date')
		salary = request.POST.get('salary')
		img = request.FILES.get('logo')
		experience = request.POST.get('experience')
		location = request.POST.get('location')
		skills = request.POST.get('skills')
		description = request.POST.get('description')

		recruiter = Recruiter.objects.get(user=request.user)

		
		Job.objects.create(recruiter=recruiter, start_date=start_date, end_date=end_date, title=job_title, salary=salary, image=img, experience=experience, location=location, skills=skills, description=description, creation_date=date.today() )
		error="no"
	else:
		error="yes"

	d = {'error' : error} # dictionary
	return render(request, 'post_job.html', d)

def job_list(request):
	if not request.user.is_authenticated:
		return redirect('recruiter_login')

	user = request.user
	recruiter = Recruiter.objects.get(user=user)
	job = Job.objects.filter(recruiter=recruiter)
	d = {'job' : job}
	return render(request, 'job_list.html',)