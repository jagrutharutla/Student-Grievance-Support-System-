from django.forms import Form, CharField,PasswordInput


class FacultyForm(Form):
    username=CharField(max_length=50)
    password=CharField(max_length=50)
    name=CharField(max_length=50)
    email=CharField(max_length=50)
    mobile=CharField(max_length=50)
    branch=CharField(max_length=50)
    complainttype = CharField(max_length=50)

class LoginForm(Form):
    username = CharField(max_length=100)
    password = CharField(widget=PasswordInput())
    usertype = CharField(max_length=50)
