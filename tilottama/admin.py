from django.contrib import admin
from .models import *
# Register your models here.

class MemberAdmin(admin.ModelAdmin):
	pass


admin.site.register(Notices, MemberAdmin) 