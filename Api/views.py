import datetime
from django.conf import settings
from .serializers import *
from .models import *
from rest_framework.views import APIView
from rest_framework import status
import requests
import json
import pytz
from django.http import JsonResponse
from django.core.mail import send_mail
from rest_framework.permissions import AllowAny
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound
from django.views.decorators.http import require_GET
from django.template.loader import render_to_string
#  from django.core.paginator import Paginator
import paho.mqtt.client as mqtt
import boto3


def apiendpoint2(request):
    data2 = json.dumps(request.GET)
    print(data2)

    return render(request, 'template/login01.html')


class CsrfExemptSessionAuthentication(SessionAuthentication):

    def enforce_csrf(self, request):
        return ''


def login(request):
    return render(request, 'template/login01.html')


def pdf_view(request):
    return render(request, 'template/krishna.html')


def pdf_view2(request):
    return render(request, 'template/krishna3.html')


def ios_app_policy(request):
    return render(request, 'template/apple_policy.html')



# def lists3data(request):
#     access_key_id = 'AKIAJGY6KRVNY6LEOI4Q'
#     secret_access_key = '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'
#     s3 = boto3.resource('s3', aws_access_key_id=access_key_id, aws_secret_access_key=secret_access_key)
#     #  response = s3.list_buckets()
#     my_bucket = s3.Bucket('g-think-device-code')
#     lines = '{"request":"http://g-think-device-code.s3.ap-south-1.amazonaws.com/","data":'
#     files = []
#     for my_bucket_object in my_bucket.objects.all():
#         #  print(type(my_bucket_object.key))
#         if '.bin' in my_bucket_object.key:
#             files.append(my_bucket_object.key)
#     fl = str(files)
#     fl = fl.replace('\'', '\"')
#     lines += fl + '}'
#     #  print(lines)
#     return HttpResponse(lines, content_type="text/plain")


def index(request):
    return render(request, 'template/index.html')


def index2(request):
    return render(request, 'home.html')


def sitemap(request):
    print(request)
    print(request)
    print(request)
    lines = [
        "User-Agent: *",
        "Disallow: /private/",
        "Disallow: /junk/",
    ]
    return HttpResponse("\n".join(lines), content_type="text/plain")


def switch(request):
    print(request)
    return render(request, 'template/SmartSwitch.html')


def sensor(request):
    print(request)
    return render(request, 'template/SmartSensors.html')


def lock(request):
    print(request)
    return render(request, 'template/SmartLocks.html')


def threeimg(request):
    print(request)
    img1 = '{"Images":[{"title":"Smart Home Remote","Img":"https://gthink-images-website.s3.ap-south-1.amazonaws.com/prof+(1).png","Info":"Switch Device even when you aren\'t at home"},{"title":"Become The Master","Img":"https://gthink-images-website.s3.ap-south-1.amazonaws.com/prof+(1).png","Info":"Know If Device Is Turned ON or OFF"},{"title":"Take Your Remote Anywhere","Img":"https://gthink-images-website.s3.ap-south-1.amazonaws.com/prof+(1).png","Info":"Switch Device even when you aren\'t at home"}]}'
    json_object = json.loads(img1)
    return JsonResponse(json_object, status=status.HTTP_200_OK)


def curtain(request):
    print(request)
    return render(request, 'template/SmartMotors.html')


def current_data(request):
    print(request)
    return render(request, 'template/current_display.html')


def app_policy(request):
    return render(request, 'template/app.html')



@require_GET
def robots_txt(request):
    print(request)
    lines = [
        "User-Agent: *",
        "Disallow: /private/",
        "Disallow: /junk/",
        "Sitemap: https://www.gthinkinventors.in/sitemap.xml",
    ]
    return HttpResponse("\n".join(lines), content_type="text/plain")


@require_GET
def favicon(request):
    print(request)
    lines = [
        "User-Agent: *",
        "Disallow: /private/",
        "Disallow: /junk/",
    ]
    return HttpResponse("\n".join(lines), content_type="text/plain")


def error_404_view(request, exception):
    email_data_length = str(request.headers)+str(request)+str(request.data)
    try:
        res = send_mail("hello G-Think", email_data_length, "lalithkumargoona@gmail.com", ["lalithkumargoona@gmail.com"], fail_silently=False)
        print('test::::', res)
        return HttpResponseNotFound(render_to_string('template/404.html'))
        # return render(request, 'template/404.html')
    except exception as e:
        print('exception ::::', str(e))
        return render(request, 'template/404.html')


def error_500_view(request):
    email_data_length = str(request.headers)+str(request)+str(request.data)
    try:
        res = send_mail("hello G-Think", email_data_length, "lalithkumargoona@gmail.com", ["lalithkumargoona@gmail.com"], fail_silently=False)
        print('test::::', res)
        return HttpResponseNotFound(render_to_string('template/500.html'))
        # return render(request, 'template/404.html')
    except Exception as e:
        print(e)
        return render(request, 'template/500.html')


class ScheduleDevice(APIView):
    permission_classes = [AllowAny]
    authentication_classes = (CsrfExemptSessionAuthentication, BasicAuthentication)

    # noinspection PyMethodMayBeStatic
    def post(self, request):
        serializer = ScheduleDeviceSerializer(data=request.data, context={'request': request})
        if not(serializer.is_valid()):
            data = {"error": "invalid_request", "error_description": serializer.errors}
            return JsonResponse(data, status=status.HTTP_400_BAD_REQUEST)
        else:
            try:
                acsame = Scheduling.objects.filter(Devicename=serializer.data['Devicename']).filter(Timestamp=serializer.data['Timestamp'])
                if len(acsame) != 0:
                    return JsonResponse({"INFO": "Already Added With Same Values"}, status=status.HTTP_400_BAD_REQUEST)
                dev_data = Scheduling(Devicename=serializer.data['Devicename'], temp=serializer.data['temp'], hum=serializer.data['hum'], ppm=serializer.data['ppm'], bat=serializer.data['bat'], sol=serializer.data['sol'], Timestamp=serializer.data['Timestamp'])
                dev_data.save()
                # os.system('at now < a.txt')
                return JsonResponse({"INFO": "Scheduled successfully"}, status=status.HTTP_201_CREATED)
            except Scheduling.DoesNotExist:
                return JsonResponse({"INFO": "Exception"}, status=status.HTTP_400_BAD_REQUEST)

 # Checking