from django.contrib import admin

# Register your models here.
from ComplaintManagement.models import StudentModel, ComplaintModel, FacultyModel

admin.site.register(StudentModel)
admin.site.register(ComplaintModel)
admin.site.register(FacultyModel)