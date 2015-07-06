from django.db import models
from django.utils import timezone
from datetime import datetime

# Create your models here.
class Movie(models.Model):
	title = models.CharField(max_length=200)
	summary = models.TextField()
	release_date = models.DateField(default=datetime.now)
	rating = models.IntegerField(default=0)
	copies = models.IntegerField(default=0, null=True, blank=True)
	def in_stock(self):
		return self.copies > 0
	in_stock.boolean = True
	in_stock.short_description = 'In Stock?'
	def __str__(self):
		return self.title

class Person(models.Model):
	name = models.CharField(max_length=200)
	GENDER_CHOICES=[('M','Male'),('F','Female'),('U','Unknown')]
	gender = models.CharField(max_length=1, choices=GENDER_CHOICES, default='U')
	movies = models.ForeignKey(Movie, blank=True, null=True)
	def __str__(self):
		return self.name

