from django.db import models
from datetime import datetime
# Create your models here.

class Work(models.Model):
	subject   = models.CharField(max_length=120)
	assignment_date = models.DateField(default=datetime.now)
	assignment_description = models.TextField()
	file = models.FileField(null=True,blank=True,upload_to='documents')
	report = models.FileField(null=True,blank=True,upload_to='reports')
	report_submission = models.BooleanField(default=False)
	submission_date = models.DateField(null=True,blank=True)
	remarks = models.TextField(null=True,blank=True)

	def __repr__(self):
		return self.subject

	def __str__(self):
		return self.subject


# title - Subject
# assignment date
# assignment description
# report submission
# submission date