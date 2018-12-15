from django.contrib import admin
from daterange_filter.filter import DateRangeFilter
# Register your models here.
from .models import Work






def export_xls(modeladmin, request, queryset):
	import xlwt
	from django.http import HttpResponse

	response = HttpResponse(content_type='application/ms-excel')
	response['Content-Disposition'] = 'attachment; filename=Work_Report.xls'
	wb = xlwt.Workbook(encoding='utf-8')
	ws = wb.add_sheet("MyModel")

	row_num = 0
	col_width = 8000

	columns = [
	    (u"ASSIGNMENT DATE", col_width),
	    (u"SUBJECT", col_width),
	    (u"ASSIGNMENT DESCRIPTION", col_width),
	    (u"REPORT SUBMISSION", col_width),
	    (u"SUBMISSION DATE", col_width),
	    (u"REMARKS", col_width),
	]

	font_style = xlwt.XFStyle()
	font_style.font.bold = True

	for col_num in range(len(columns)):
	    ws.write(row_num, col_num, columns[col_num][0], font_style)
	    # set column width
	    ws.col(col_num).width = columns[col_num][1]

	font_style = xlwt.XFStyle()
	font_style.alignment.wrap = 1

	for obj in queryset:
	    row_num += 1
	    submitted = u'YES' if obj.report_submission else u'NO'
	    row = [
	        obj.assignment_date.strftime('%d/%m/%Y'),
	        obj.subject,
	        obj.assignment_description,
	        submitted,
	        obj.submission_date.strftime('%d/%m/%Y') if obj.submission_date else '', 
	        obj.remarks,
	    ]
	    for col_num in range(len(row)):
	        ws.write(row_num, col_num, row[col_num], font_style)
	        
	wb.save(response)
	return response
    
export_xls.short_description = u"Export to Excel"



class WorkAdmin(admin.ModelAdmin):
	fields = ['assignment_date','subject','assignment_description','file','report','report_submission','submission_date','remarks']
	list_display = ('assignment_date','subject','assignment_description','report_submission','submission_date','remarks')
	list_filter = (('assignment_date',DateRangeFilter), 'report_submission',('submission_date',DateRangeFilter), )
	actions = [export_xls,]

admin.site.site_header = "Work Scheduler ";
admin.site.site_title = "Work Scheduler ";

admin.site.register(Work,WorkAdmin)




