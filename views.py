from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.db import connection
from datetime import date
from django.core.mail import send_mail
import re
import random
from .forms import *
from django.core.mail import EmailMessage
from .models import Registration,Registration1,Hotel,Marks,Enrollment
def home(request):
    return render(request,'home1.html')
def log(request):
    return render(request,'login.html')
def sign(request):
    if request.method=='POST':
        r=Registration()
        r.fname=request.POST['fname']
        r.clgname=request.POST['clg']
        r.branch=request.POST['branch']
        r.password=request.POST['pwd']
        r.year=request.POST['year']
        r.save()
        return render(request,'signupsuccess.html')
    else:
        return render(request,'signup.html')
def admin(request):
    return render(request,'admin.html')
def signupsuccess(request):
    if request.method=='POST':
        r=Registration()
        r.fname=request.POST['fname']
        r.lname=request.POST['lname']
        r.clgname=request.POST['clg']
        r.branch=request.POST['branch']
        r.password=request.POST['pwd']
        r.year=request.POST['year']
        r.emailid=request.POST['email']
        r.save()
    data=Registration.objects.all()

    stu = {
        "student_number": data
    }

    return render(request,'signupsuccess.html',{'vamsi':stu})
def loginsuccess(request):
    if request.method=='POST':
        a=request.POST['username']
        b=request.POST['pwd']
        r=Registration.objects.all()
        c=r.count()
        x=[]
        for i in r:
            if(i.emailid==a and i.password==b):
                return render(request,"loginsuccess.html")
        return HttpResponse("invalid")
def register(request):
    if request.method=='POST':
        q=Registration1.objects.all()
        r=Registration1()
        a=request.POST['email']
        b=request.POST['pwd']
        k=0
        for i in q:
            if(i.emailid==a):
                k=1
                break
        if(k==0):
            r.emailid=a
            r.password=b
            r.save()
            from_email='sriharshanagulakonda@gmail.com'
            to_email=['suryavamsi66666@gmail.com']
            #email=EmailMessage("ONLINE EXAM PORTAL","successfully registered",from_email,to_email)
            #email.send()
            send_mail(
                'Online Exam Portal',
                'Your Registration is successfully done',
                'suryavamsi66666@gmail.com',
                [a],
                fail_silently=False,
            )
            return render(request,'loginsuccess.html',{'name10':a})
        else:
            return render(request,"home1.html",{'vamsi':True})
    #return render(request,"home1.html")
def loginn(request):
    if request.method=='POST':
        a=request.POST['email']
        b=request.POST['pwd']
        r=Registration1.objects.all()
        for i in r:
            if(i.emailid==a and i.password==b):
                return render(request,"loginsuccess.html",{'name10':a})
        return render(request,"home1.html",{'vamsii':True})
def logout(request):
    return render(request,'home1.html')
def adminn(request):
    if request.method=='POST':
        a=request.POST['username']
        b=request.POST['pwd']
        if(a=='admin' and b=='admin'):
            return render(request,'admin.html')
    return HttpResponse("Invalid")
def students(request):
    data = Registration1.objects.all()
    p=[]
    for i in data:
        r=''
        r+i.emailid+' '+i.password
        p.append(r)
    stu = {
        "student_number": p
    }

    return render(request, 'students.html', {'vamsi': data})
def questions(request):
    return render(request,'addquestions.html')
def subjects(request):
    return HttpResponse('hi')
def addsubjects(request):
    return render(request,'addsub.html')
def addquestions(request):
    return render(request,'addquestions.html')
def subadd(request):
    if request.method=='POST':
        '''k=Subjectnames()
        k.sname=request.POST['subjectname']
        k.image=request.POST['upload']
        k.save()'''
        return HttpResponse("succesfully uploaded")
    return HttpResponse('sry')


# Create your views here.
def hotel_image_view(request):
    if request.method == 'POST':
        form = HotelForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            return HttpResponse('successfully uploaded')
    else:
        form = HotelForm()
    return render(request, 'hotel_image_form.html', {'form': form})


def success(request):
    return HttpResponse('successfuly uploaded')
def display_hotel_images(request):
    if request.method == 'GET':
        # getting all the objects of hotel.
        Hotels = Hotel.objects.all()
        return render(request, 'display_hotel_images.html',
                       {'hotel_images': Hotels})
def uploadque(request):
    if request.method=='POST':
        r=Questions()
        r.subname=request.POST['subname']
        r.marks=request.POST['marks']
        r.question=request.POST['text']
        r.option1=request.POST['op1']
        r.option2 = request.POST['op2']
        r.option3= request.POST['op3']
        r.option4= request.POST['op4']
        r.answer=request.POST['op5']
        r.save()
        return HttpResponse("successfull...")
    return render(request,"start.html")
def profile(request):
    return HttpResponse('welcome to profile')
def search(request):
    if request.method=='POST':
        r=Hotel.objects.all()
        email=request.POST['emailid']
        p=request.POST['search']
        q=[]
        for i in r:
            str=i.name.find(p)
            if(str>=0):
                q.append(i.name)
        return render(request,'loginsuccess.html',{'available':q,'data':r,'emailid':email})
    return  render(request,'loginsuccess.html')

def gotosub(request,test,email):
    r=Hotel.objects.all()
    e=Enrollment.objects.all()
    p='false'
    for i in e:
        print(i.subjectname,i.emailid)
        if i.subjectname==test and i.emailid==email:
            p='true'
    return render(request,'enroll.html',{'data':r,'string':test,'emailid':email,'check':p})
def aboutus(request):
    return render(request,'aboutus.html')
def enroll(request):
    if request.method=='POST':
        e=Enrollment()
        a=request.POST['email']
        e.subjectname=request.POST['sub']
        e.emailid=request.POST['email']
        e.date=str(date.today())
        e.save()
        sendornot=request.POST['store']
        if(sendornot=='true'):
            send_mail(
                'Online Exam Portal',
                'You are enrolled for '+request.POST['sub']+" course on date "+str(date.today())+" and for free course certification, you should complete course with 30 days",
                'suryavamsi66666@gmail.com',
                [a],
                fail_silently=False,
            )
        return render(request,'afterenroll.html',{'sname1':request.POST['sub'],'email':request.POST['email']})
def questionsshow(request):
    if request.method=='POST':
        sub=request.POST['subname']
        ee=request.POST['emailid']
        mm=request.POST['marks']
        q=Questions.objects.all()
        items = sorted(Questions.objects.all(), key=lambda x: random.random())
        return render(request,'afterenroll.html',{'data':items,'subject':sub,'marks':mm,'email':ee})
def marksevaluation(request):
    if request.method=='POST':
        subject=request.POST['subject']
        marks=request.POST['marks']
        email=request.POST['emailid']
        q=Questions.objects.all()
        g=0
        c=0
        m=Marks.objects.all()

        for i in m:
            if(i.emailid==email and i.subname==subject and i.marksvalue==marks):
                return render(request,'afterenroll.html',{'info':'Sorry, you previously attempted this quiz.'})
        for i in q:
            if(i.marks==marks and i.subname==subject):
                try:
                    m=request.POST[i.question]
                    if(m==i.answer):
                        if(i.marks=='one'):
                            g=g+1
                        elif(i.marks=='two'):
                            g=g+2
                        elif(i.marks=='three'):
                            g=g+3
                except:
                    g=g+0
        m=Marks()
        m.emailid=email
        m.subname=subject
        m.marksvalue=marks
        m.marks=g
        m.save()
        return HttpResponse(c)
def showquestions(request):
    return render(request,"showquestions.html")
def show(request):
    if request.method=='POST':
        q=Questions.objects.all()
        c=request.POST['course']
        m=request.POST['marks']
        return render(request,"showquestions.html",{'questions':q,'course':c,'marks':m})
def aboutstudents(request):
    return render(request,"aboutstu.html")
def showstudents(request):
    if request.method=='POST':
        e=request.POST['email']
        en=Enrollment.objects.all()
        return render(request,"aboutstu.html",{'data':en,'email':e})


