from django.urls import path
from . import views
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from .views import *
app_name='online'
urlpatterns=[
    path('',views.home,name='home'),
    path('add',views.log,name='log'),
    path('sign',views.sign,name='sign'),
    path('admin',views.admin,name='admin'),
    path('signupsuccess',views.signupsuccess,name='success'),
    path('loginsuccess',views.loginsuccess,name='loginsuc'),
    path('register',views.register,name='register'),
    path('login2',views.loginn,name='loginn'),
    path('logout',views.logout,name='logout'),
    path('admin',views.adminn,name='admin'),
    path('addquestions',views.addquestions,name='addque'),
    path('showquestions',views.showquestions,name='showque'),
    path('showstudents',views.showstudents,name="shotstu"),
    path('aboutstudents',views.aboutstudents,name='astu'),
    path('show',views.show,name='show'),
    path('addsubjects',views.addsubjects,name='addsub'),
    path('students',views.students,name='students'),
    path('subjects',views.subjects,name='subjects'),
    path('subadd',views.subadd,name='subadd'),
    path('image_upload', hotel_image_view, name = 'image_upload'),
    path('success', success, name = 'success'),
    path('hotel_images', display_hotel_images, name = 'hotel_images'),
    path('uploadque',views.uploadque,name='uploadque'),
    path('profile',views.profile,name='profile'),
    path('search',views.search,name='search'),
    path('gotosub/<str:test> <str:email>',views.gotosub,name='gotosub'),
    path('aboutus',views.aboutus,name='aboutus'),
    path('gotosub/enroll',views.enroll,name='enroll'),
    path('gotosub/onemark',views.questionsshow,name='questionshow'),
    path('gotosub/twomark',views.questionsshow,name='questionshow'),
    path('gotosub/threemark',views.questionsshow,name='questionshow'),
    path('gotosub/marksevaluation',views.marksevaluation,name='marksevaluation'),
]
if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)