# views.py
from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login , logout
from django.contrib import messages
from .models import *
from django.core.paginator import Paginator
from .client import report
from django.db.models import *
from django.core.mail import EmailMultiAlternatives
from django.contrib.auth.decorators import login_required

def home(request):
    return render(request, 'index.html')



def signup_page(request):

    if request.method == 'POST':

        email=request.POST.get('email')
        username=request.POST.get('username')
        password=request.POST.get('password')

        user=User.objects.filter(username=username)

        if user.exists():
            messages.error(request, "Username already exists!!")

            return redirect('/signup')

        user=User.objects.create(
            email=email,
            username=username,
            password=password,
            

            )


        user.set_password(password)
        user.save()
        messages.info(request, "Account Created Successfully")

        return redirect('/login/')


    return render(request , 'signup.html')

def login_page(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Check for specific username and password
        if username == 'shankar11' and password == '1122':
            return redirect('/notice/')
        else:
            user = authenticate(username=username, password=password)

            if user is None:
                messages.error(request, "Invalid username or password")
                return redirect("/login/")
            else:
                login(request, user)  
                return redirect('/user-notice/')
    return render(request, 'login.html')


def contact(request):
    email=''

    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        contact_details.objects.create(
            name = name,
            email = email,
            subject = subject,
            message = message
            )

        subject , from_email, to = "Welcome Email", "p1ashok36@gmail.com", email
        text_content = "This is an important message."
        html_content = "<b>Thanks u! for Reaching us and <strong>Welcome to Tilottama Collage</strong>.</b>"
        
        msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
        msg.attach_alternative(html_content, "text/html")
        msg.send()


    
    return render(request, 'contact.html')

@login_required(login_url="/login/")
def footer(request):
    return render(request, 'footer.html')


def gallery(request):
    return render(request, 'gallery.html')




def Aboutus(request):
    return render(request, 'about.html')

def notice(request):

    if request.method == 'POST':
        notice_by = request.POST.get('notice_by')
        notice_title = request.POST.get('notice_title')
        notice_description = request.POST.get('notice_description')
        notice_image = request.FILES.get('notice_by')
        
        Notices.objects.create(
            notice_by=notice_by,
            notice_title=notice_title,
            notice_description=notice_description,
            notice_image=notice_image,
        )

        return redirect('/notice')

    notices = Notices.objects.all()  

    context = {'notices': notices}

    return render(request, 'main.html', context)


def delete_notice(request,id):
    try:
        notice = get_object_or_404(Notices, id=id)
        notice.delete()
        messages.success(request, "Notice deleted successfully.")
    except Notices.DoesNotExist:
        messages.error(request, "Notice not found.")
    
    return redirect('/notice')




def update_notice(request,id):
	update_notice=Notices.objects.get(id=id)



	if request.method=='POST':
		notice_by=request.POST.get('notice_by')
		notice_title=request.POST.get('notice_title')
		notice_description=request.POST.get('notice_description')
		notice_image=request.FILES.get('notice_image')
		

		update_notice.notice_by = notice_by
		update_notice.notice_title = notice_title
		update_notice.notice_description = notice_description


		if notice_image:
			update_notice.notice_image = notice_image

		update_notice.save()



		return redirect('/notice')

	context = {'update':update_notice}

	return render(request , 'update.html' , context)



def user_notice(request):
    notices = Notices.objects.all()
    context = {'notices': notices}
    return render(request, 'notice.html', context)


def logout_page(request):
	logout(request)
	return redirect('/')



def get_student(request):


    student_obj = Student.objects.all()

    if request.GET.get('search'):
        search = request.GET.get('search')

        student_obj = student_obj.filter(
            Q(student_name__icontains = search) |
            Q(department__department__icontains = search)   |
            Q(student_id__student_id__icontains = search)   |
            Q(student_email__icontains = search)    |
            Q(student_age__icontains = search)
        
        )


    paginator = Paginator(student_obj, 25)  # Show 25 contacts per page.

    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    context = {'students': page_obj}


    return render(request , 'student.html' , context)


def see_marks(request, student_id):
    
    mark = StudentsMarks.objects.filter(student__student_id__student_id=student_id)
    total_marks = mark.aggregate(total=Sum('marks'))
    context = {'marks': mark, 'total': total_marks}
    return render(request, 'see_marks.html', context)
