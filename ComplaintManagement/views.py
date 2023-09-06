from django.shortcuts import render

from ComplaintManagement.forms import  FacultyForm, LoginForm
from ComplaintManagement.models import ComplaintModel,FacultyModel
from datetime import datetime

import smtplib
import random


def login(request):

    if request.method == "GET":
        # Get the posted form
        loginForm = LoginForm(request.GET)

        if loginForm.is_valid():

            uname = loginForm.cleaned_data["username"]
            upass = loginForm.cleaned_data["password"]
            usertype = loginForm.cleaned_data["usertype"]

            if usertype=="admin":
                if uname == "admin" and upass == "admin":
                    request.session['role'] = "admin"
                else:
                    return render(request, 'index.html', {"message": "Invalid Credentials"})
            
            elif usertype=="faculty":
                faculty = FacultyModel.objects.filter(username=uname, password=upass).first()
                if faculty is not None:
                    request.session['role'] = "faculty"
                   
                else:
                    return render(request, 'index.html', {"message": "Invalid Credentials"})

            request.session['username'] = uname

            if request.session['role'] in "admin":
                return render(request, "addfaculty.html", {"complaints": FacultyModel.objects.all()})
            
            elif request.session['role'] in "faculty":
                
                return render(request, "viewcomplaints.html",{"complaints": ComplaintModel.objects.all()})
            else:
                return render(request, 'index.html', {"message": "Invalid Credentials"})

        return render(request, 'index.html', {"message": "Invalid From"})

    return render(request, 'index.html', {"message": "Invalid Request"})

def logout(request):
    try:
        del request.session['username']
    except:
        pass
    return render(request, 'index.html', {})


#============================================================================

def getcomplaints(request):

    if request.session['role'] in "admin":
        return render(request, "viewcomplaints.html", {"complaints":ComplaintModel.objects.all()})
   
    elif request.session['role'] in "faculty":
        complainttype=request.session['complainttype']
        return render(request, "viewcomplaints.html", {"complaints": ComplaintModel.objects.filter(complainttype=complainttype)})


#=======================================================================================================================

def addfaculty(request):

    facultyForm = FacultyForm(request.POST)

    if facultyForm.is_valid():

        name = facultyForm.cleaned_data["name"]
        email = facultyForm.cleaned_data["email"]
        mobile = facultyForm.cleaned_data["mobile"]
        username = facultyForm.cleaned_data["username"]
        password = facultyForm.cleaned_data["password"]
        complainttype = facultyForm.cleaned_data["complainttype"]
        branch = facultyForm.cleaned_data["branch"]

        FacultyModel(name=name,email=email,mobile=mobile,username=username,password=password,complainttype=complainttype,branch=branch).save()

        return render(request, 'addfaculty.html', {"message": "Faculty Posted SuccessFully"})

    return render(request, 'addfaculty.html', {"message": "Faculty Request Failed"})

def getfacultys(request):
    return render(request, "viewfacultyes.html", {"facultys":FacultyModel.objects.all()})

def deletefaculty(request):

    facultyid= request.GET['facultyid']
    FacultyModel.objects.get(id=facultyid).delete()

    return render(request, "viewfacultyes.html", {"facultys": FacultyModel.objects.all()})