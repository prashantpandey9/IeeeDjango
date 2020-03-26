from django.db import models
from django.contrib.auth.models import User
# Create your models here.
from django.db.models.signals import pre_save
	
class Member(models.Model):
	image_mem = models.ImageField(upload_to='static/persons')	
	name_member = models.CharField(max_length=100)
	title = models.CharField(max_length=100)
	def __str__(self):
		return self.name_member

class Society(models.Model):
	image_so = models.ImageField(upload_to='static/images')	
	name_so = models.CharField(max_length=120)
	discription=models.TextField(max_length=145)
	def __str__(self):
		return self.name_so

class Event(models.Model):
	year=models.IntegerField()
	activity=models.CharField(max_length=100)
	topic=models.CharField(max_length=100)
	about_event=models.TextField()
	def __str__(self):
		return str(self.year)

class Xtreme(models.Model):
	version=models.IntegerField(default=9)
	team_no=models.IntegerField(default=1)
	def __str__(self):
		return str(self.version)


class Team(models.Model):
	version=models.ForeignKey(Xtreme,on_delete=models.CASCADE)
	team_name=models.CharField(max_length=50)
	def __str__(self):
		return str(self.version)