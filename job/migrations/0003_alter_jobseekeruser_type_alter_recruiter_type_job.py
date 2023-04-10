# Generated by Django 4.1.5 on 2023-04-09 23:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0002_alter_jobseekeruser_gender_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jobseekeruser',
            name='type',
            field=models.CharField(choices=[('Jobseeker', 'Jobseeker'), ('Recruiter', 'Recruiter')], default='Jobseeker', max_length=9),
        ),
        migrations.AlterField(
            model_name='recruiter',
            name='type',
            field=models.CharField(choices=[('Jobseeker', 'Jobseeker'), ('Recruiter', 'Recruiter')], default='Recruiter', max_length=9),
        ),
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('title', models.CharField(max_length=100)),
                ('salary', models.FloatField(max_length=20)),
                ('image', models.FileField(upload_to='')),
                ('description', models.CharField(max_length=300)),
                ('experience', models.CharField(max_length=50)),
                ('skills', models.CharField(max_length=100)),
                ('creation_date', models.CharField(max_length=50)),
                ('location', models.DateField()),
                ('recruiter', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='job.recruiter')),
            ],
        ),
    ]
