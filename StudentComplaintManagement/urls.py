
from django.contrib import admin
from django.urls import path
from django.views.generic import TemplateView

from ComplaintManagement.views import login, logout,  \
     getcomplaints, addfaculty, getfacultys, deletefaculty

urlpatterns = [

    path('admin/', admin.site.urls),

    path('',TemplateView.as_view(template_name = 'index.html'),name='login'),
    path('login/',TemplateView.as_view(template_name = 'index.html'),name='login'),
    path('loginaction/',login,name='loginaction'),
    path('logout/', logout, name='logout'),

    
    path('getcomplaintes/',getcomplaints,name='view'),
    

    path('addfaculty/',TemplateView.as_view(template_name ='addfaculty.html'),name='apply'),
    path('addfacultyaction/',addfaculty,name='add'),
    path('getfacultyes/',getfacultys,name='view'),
    path('deletefaculty/',deletefaculty,name='delete'),

]
