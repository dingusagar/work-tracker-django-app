from django.contrib import admin
from daterange_filter.filter import DateRangeFilter
# Register your models here.
from .models import Work

class WorkAdmin(admin.ModelAdmin):
	fields = ['date','title','description','file','submitted']
	list_display = ('date','title', 'description', 'submitted', )
	list_filter = (('date',DateRangeFilter), 'submitted', )

admin.site.site_header = "Work Scheduler ";
admin.site.site_title = "Work Scheduler ";

admin.site.register(Work,WorkAdmin)