"""
URL configuration for collage project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  ('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from tilottama import views
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home , name='home'),
    path('login/' , views.login_page , name='login'),
    path('signup/' , views.signup_page , name='signup'),
    path('contact/' , views.contact , name='contact'),
    path('footer/' , views.footer , name='footer'),
    path('gallery/' , views.gallery , name='gallery'),
    path('notice/' , views.notice , name='notice'),
    path('update_notice/<id>/',views.update_notice, name='update_notice'),
    path('delete_notice/<id>/',views.delete_notice, name='delete_notice'),
    path('user-notice/' , views.user_notice , name='user-notice'),
    path('logout/' , views.logout_page , name='logout'),
    path('student/' , views.get_student , name='student'),
    path('see_marks/<student_id>/', views.see_marks, name='see_marks'),

]










if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)



urlpatterns += staticfiles_urlpatterns()