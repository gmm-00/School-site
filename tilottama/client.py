from django.db.models import Sum

import random
from .models import *

from faker import Faker

fake = Faker()


def client(n=10) -> None:
	try:
	    department_obj = Department.objects.all()

	    for _ in range(n):
	        department_index = random.randint(0, len(department_obj) - 1)
	        department = department_obj[department_index]

	        student_id = f'SM-0{random.randint(50, 250)}'
	        student_name = fake.name()
	        student_email = fake.email()
	        student_age = random.randint(18, 25)
	        student_address = fake.address()

	        studentid_obj = StudentID.objects.create(student_id=student_id)

	        student_obj = Student.objects.create(
	            department=department,
	            student_id=studentid_obj,
	            student_name=student_name,
	            student_email=student_email,
	            student_age=student_age,
	            student_address=student_address,
	        )
	except Exception as e:
		print(e)

	
def marks(n):
	try:

		student_obj = Student.objects.all()

		for student in student_obj:
			subject_obj = Subject.objects.all()
			for subject in subject_obj:
				StudentsMarks.objects.create(
					student = student,
					subject = subject,
					marks = random.randint(30 , 100)
					)
	except Exception as e:
		print(e)
def report():
    current_rank = 1
    rank = Student.objects.annotate(marks=Sum('student_mark__marks')).order_by('-marks', '-student_age')
    i = 1
    for ranks in rank:
        Result_student.objects.create(
            student=ranks,
            rank=i
        )
        i = i + 1
