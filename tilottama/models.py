from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Notices(models.Model):
    notice_by = models.CharField(max_length=50, null=True, default=None)
    notice_title = models.CharField(max_length=50, null=True, default=None)
    notice_description = models.TextField()
    notice_image = models.ImageField(upload_to='image', null=True , blank=True , default=None)


    def __str__(self):
    	return self.notice_title
