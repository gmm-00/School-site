# views.py
from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login , logout
from django.contrib import messages
from .models import *


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

        user = authenticate(username=username, password=password)

        if user is None:
            messages.error(request, "Invalid username or password")
            return redirect("/login/")
        else:
            # Check for specific username and password
            if username == 'shankar11' and password == '1122':
                return redirect('/notice/')
            else:
                login(request, user)  # Assuming you want to log in the user here.
                return redirect('/user-notice/')
    return render(request , 'login.html')

def contact(request):
    return render(request, 'contact.html')


def footer(request):
    return render(request, 'footer.html')


def gallery(request):
    return render(request, 'gallery.html')


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

    notices = Notices.objects.all()  # Renamed the variable 'notice' to 'notices'

    context = {'notices': notices}  # Renamed the context variable to 'notices'

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