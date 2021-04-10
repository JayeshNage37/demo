from django.contrib import admin
from django.urls import path
from . import views
from django.conf.urls import url


urlpatterns = [
    path('apply-leave', views.insert_driver_leave_details)
]