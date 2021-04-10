from django.shortcuts import render
from django.conf import settings
from driver.driver_leave.models import DriverLeaves
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from rest_framework.parsers import JSONParser
from driver import messages
import json
from django.http import JsonResponse

@csrf_exempt
def insert_driver_leave_details(request):
    try:
        driver_leaves_dict = json.loads(request.body)
        flag = DriverLeaves.create_driver_leave(driver_leaves_dict)  
        if flag == True:
            return_object = {
            "status" : messages.SUCCESS,
            "message" : messages.DRIVER_LEAVES_CREATION_SUCCESS,
            }
        else:
            return_object = {
            "status" : messages.FAIL,
            "message" : messages.DRIVER_LEAVES_CREATION_FAIL,
            }
    except (Exception) as error:
        print("error in insert_driver_leave_details ",error)
        return_object = {
            "status" : messages.FAIL,
            "message" : messages.DRIVER_LEAVES_CREATION_FAIL,
        } 
    return JsonResponse(return_object, safe=False)