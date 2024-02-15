#models.py

from django.db import models
from django.core.validators import MaxValueValidator

# Create your models here.
class Profile(models.Model):
    name=models.CharField(max_length=25)
    intro=models.CharField(max_length=255)
    profile_picture = models.ImageField(upload_to='profile_pics/')
    resume = models.FileField(upload_to='resumes/')


class AboutMe(models.Model):
    content = models.TextField()

class Projects (models.Model):
    title = models.CharField(max_length=255)
    project_image=models.ImageField(upload_to='proj_pics/')
    project_image1=models.ImageField(upload_to='proj_pics/')
    project_image2=models.ImageField(upload_to='proj_pics/')    
    github_url = models.URLField()
    lifecycle=models.CharField(max_length=500)
    technologies=models.CharField(max_length=500)
    versionControl=models.CharField(max_length=500)
    
    
    

class Skill(models.Model):
    name = models.TextField() 
    percentage =  models.PositiveIntegerField(validators=[MaxValueValidator(100)]) 

class Education(models.Model):
    institution = models.CharField(max_length=100)
    degree = models.CharField(max_length=100)
    graduation_year = models.CharField(max_length=25)
class Experience(models.Model):
    company = models.CharField(max_length=100)
    role = models.CharField(max_length=100)
    period = models.CharField(max_length=25)

class Contact (models.Model):
    email = models.EmailField()
    linkedin = models.URLField()


