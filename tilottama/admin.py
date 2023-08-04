from django.contrib import admin
from .models import *
# Register your models here.

class MemberAdmin(admin.ModelAdmin):
	pass


admin.site.register(Notices, MemberAdmin) 
admin.site.register(Department, MemberAdmin) 
admin.site.register(StudentID, MemberAdmin) 
admin.site.register(Student, MemberAdmin) 
admin.site.register(Subject, MemberAdmin)

class marks(admin.ModelAdmin):


	list_display = ['student' , 'subject' , 'marks']

admin.site.register(StudentsMarks, marks) 


