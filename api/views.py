from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated
from django.http import HttpResponse,JsonResponse
from app.models import *
from app.forms import *
from .serializers import *


def index(request):
    return render(request, 'app/main.html')


@api_view(['POST'])
def addUser(request):
    if dataSave(request.data):
        return HttpResponse('result')
    else:
        return HttpResponse('error')

    # return HttpResponse(data)
    # return render(request, 'app/viewdata.html', {'data': serializer.data})


# getting data ...
def dataSave(data):
    serializer = SignupSerializer(data=data)
    print(serializer)

    if serializer.is_valid():
        if serializer.save():
            return True

    return False


# @api_view(['GET'])
def getAllUsers(request):
    return Signup.objects.all()


@api_view(['POST'])
def CreateDoctorProfile(request):
    if request.method == 'POST':
        doctorSerializer = DoctorSerializer(data=request.data)
        if doctorSerializer.is_valid():
            doctorSerializer.save()
            data = {'key': 'null'}
            message = 'Success'
            return JsonResponse({'data': data, 'message': message}, status=200)
        else:
            data = {'key': '403 Forbidden'}
            message = 'Error: Invalid request. Permission denied (e.g. invalid API key).'
            return JsonResponse({'data': data, 'message': message}, status=403)


def DoctorForm(request):
    return render(request, 'app/doctor_form.html')
