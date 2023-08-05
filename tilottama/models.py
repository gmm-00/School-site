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





class Department(models.Model):
    department=models.CharField(max_length=50)



    class Meta:
        ordering = ['department']




    def __str__(self):
        return self.department




class StudentID(models.Model):
    student_id=models.CharField(max_length=20)


    class Meta:
        ordering = ['student_id']

    def __str__(self):
        return self.student_id




class Student(models.Model):
    department=models.ForeignKey(Department, related_name ='depart' ,on_delete=models.CASCADE)
    student_id=models.OneToOneField(StudentID,related_name='studentid',on_delete=models.CASCADE)

    student_name=models.CharField(max_length=20)
    student_email=models.EmailField(unique=True)
    student_age=models.IntegerField(default=18)
    student_address=models.TextField()



    class Meta:
        ordering = ['student_name']
        verbose_name='student'



    def __str__(self):
        return self.student_name


class Subject(models.Model):
    subject = models.CharField(max_length=50)

    def __str__(self):
        return(self.subject)

class StudentsMarks(models.Model):
    student = models.ForeignKey(Student, related_name="student_mark", on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    marks = models.IntegerField()

    class Meta:
        unique_together = ['student', 'subject']

    def __str__(self):
        return f'{self.student} {self.subject} {self.marks}'






class Result_student(models.Model):
    student = models.ForeignKey(Student, related_name="result", on_delete=models.CASCADE)
    rank=models.IntegerField()
    Date_of_time = models.DateField(auto_now_add=True)


    class Meta:
        ordering = ['rank']


    class Meta:
        unique_together = ['rank', 'Date_of_time']




class contact_details(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()



    def __str__(self):
        return self.email