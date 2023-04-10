from django.urls import path
from django.urls.resolvers import URLPattern
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

from job.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    
    path('', index, name='index'),
    
    path('admin_login/', admin_login, name='admin_login'),
    path('jobseeker_login/', jobseeker_login, name='jobseeker_login'),   
    path('recruiter_login/', recruiter_login, name='recruiter_login'),
    
    path('jobseeker_signup/', jobseeker_signup, name='jobseeker_signup'),
    path('recruiter_signup/', recruiter_signup, name='recruiter_signup'),

    path('jobseeker_home/', jobseeker_home, name='jobseeker_home'),
    path('recruiter_home/', recruiter_home, name='recruiter_home'),
    path('admin_home/', admin_home, name='admin_home'),

    path('Logout/', logout, name='Logout'),
    
    path('view_jobseeker/', view_jobseeker, name='view_jobseeker'),
    path('view_recruiter/', view_recruiter, name='view_recruiter'),
    
    path('delete_jobseeker/<int:pid>', delete_jobseeker, name='delete_jobseeker'),
    path('delete_recruiter<int:pid>', delete_recruiter, name='delete_recruiter'),

    path('change_password_admin/', change_password_admin, name='change_password_admin'),
    path('change_password_jobseeker/', change_password_jobseeker, name='change_password_jobseeker'),
    path('change_password_recruiter/', change_password_recruiter, name='change_password_recruiter'),

    path('post_job/', post_job, name='post_job'),
    path('job_list/', job_list, name='job_list'),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)