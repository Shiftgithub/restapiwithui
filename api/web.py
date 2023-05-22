from django.shortcuts import render
from . import views


def index(request):
    users = views.getAllUsers(request)
    return render(request, 'app/viewdata.html', {'users': users})


def createForm(request):
    return render(request, 'app/forms.html')


def store(request):
    return views.addUser(request)
