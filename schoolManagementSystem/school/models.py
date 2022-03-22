from django.db import models
from django.contrib.auth.models import User
from django.forms import IntegerField
# Create your models here.

class Teacher(models.Model):
	name = models.CharField(max_length=60)
	contact = models.CharField(max_length=20)
	specialization = models.CharField(max_length=50)
	qualification = models.CharField(max_length=50,null=True)
	teachingLevel = models.CharField(max_length=50,null=True)

	def __str__(self):
		return self.name




class Student(models.Model):
	name = models.CharField(max_length=60)
	gender = models.CharField(max_length=10)
	age    = models.IntegerField(null=True)
	contact = models.CharField(max_length=20)
	address = models.CharField(max_length=200)
	studyClass = models.IntegerField(null=True)

	def __str__(self):
		return self.name

