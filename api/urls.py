from django.urls import path
from . import views
from . import web

urlpatterns = [
    path('api/index/', views.addUser, name="api/index"),

    # forntend  paths
    path('frontend/all/users/', web.index),
    path('frontend/forms/', web.createForm),
    path('frontend/store/', web.store),

    path('add-doctor/', views.CreateDoctorProfile, name="add_doctor"),
    path('add-doctor-form/', views.DoctorForm, name="add-doctor-form"),
]
