from django.db import models
from datetime import datetime
# Create your models here.

class Work(models.Model):
	title   = models.CharField(max_length=120)
	date = models.DateTimeField(default=datetime.now)
	description = models.TextField()
	file = models.FileField(null=True,blank=True,upload_to='documents')
	submitted = models.BooleanField(default=False)

	def __repr__(self):
		return self.title

	def __str__(self):
		return self.title