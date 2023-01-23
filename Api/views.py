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


class ListS3Files(APIView):
    permission_classes = [AllowAny]
    authentication_classes = (CsrfExemptSessionAuthentication, BasicAuthentication)

    # noinspection PyMethodMayBeStatic
    def post(self, request):
        serializer = KeySerializer(data=request.data, context={'request': request})
        if not serializer.is_valid():
            data = {"INFO": serializer.errors}
            return JsonResponse(data, status=status.HTTP_400_BAD_REQUEST)
        else:
            if serializer.data['auth_key'] == settings.AUTH_KEY:
                s3 = boto3.resource('s3', aws_access_key_id=settings.ACCESS_KEY, aws_secret_access_key=settings.SECRET_ACCESS_KEY)
                my_bucket = s3.Bucket('g-think-device-code')
                lines = '{"request":"http://g-think-device-code.s3.ap-south-1.amazonaws.com/","data":'
                files = []
                for my_bucket_object in my_bucket.objects.all():
                    #  print(type(my_bucket_object.key))
                    if '.bin' in my_bucket_object.key:
                        files.append(my_bucket_object.key)
                fl = str(files)
                fl = fl.replace('\'', '\"')
                lines += fl + '}'
                lines = json.loads(lines)
                print(lines)
                return JsonResponse(lines, status=status.HTTP_200_OK)
            else:
                return JsonResponse({"INFO": "Please check the Auth-Key provided."}, status=status.HTTP_400_BAD_REQUEST)


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


class alexacallback(APIView):
    permission_classes = [AllowAny]
    authentication_classes = (CsrfExemptSessionAuthentication, BasicAuthentication)

    # noinspection PyMethodMayBeStatic
    def post(self, request):
        serializer = SendOTPSerializer(data=request.data, context={'request': request})
        res = send_mail("image upload problem problem", str(serializer), "lalithkumargoona@gmail.com", ["lalithkumargoona@gmail.com"], fail_silently=False)
        print(res)
        if not serializer.is_valid():
            data = {"ERROR": serializer.errors}
            return JsonResponse(data, status=status.HTTP_400_BAD_REQUEST)
        else:
            apiend = "http://control.msg91.com/api/sendotp.php"
            data = {'authkey': '241566AzbypoaVSBZB5bb9ec50', 'sender': 'GTIPIN', 'mobile': serializer.data['phone']}
            # , 'email':serializer.data['email']}
            if 'email' in serializer.data:
                data['email'] = serializer.data['email']
            if serializer.data['req_type'] == 'signup':
                data['message'] = 'Your One Time Password for GThink Inventors Registration is ##OTP##.'
            else:
                data['message'] = 'Your One Time Password for GThink Inventors Login is ##OTP##.'

            r = requests.post(url=apiend, data=data)
            paste_bin_url = json.loads(r.text)
            return JsonResponse({"INFO": paste_bin_url}, status=status.HTTP_200_OK)

    # noinspection PyMethodMayBeStatic
    def get(self, request):
        print(request)
        ist = pytz.timezone('Asia/Calcutta')
        current_date = datetime.datetime.now(ist)
        year = current_date.date().year
        month = current_date.date().month
        day = current_date.date().day
        hours = current_date.time().hour
        minutes = current_date.time().minute
        seconds = current_date.time().second
        res = send_mail("image upload problem problem", str(request), "lalithkumargoona@gmail.com", ["lalithkumargoona@gmail.com"], fail_silently=False)
        print('test::::', res)
        return JsonResponse({"y": year, "m": month, "d": day, "h": hours, "min": minutes, "s": seconds}, status=status.HTTP_200_OK)


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


class Google(APIView):
    permission_classes = [AllowAny]
    authentication_classes = (CsrfExemptSessionAuthentication, BasicAuthentication)

    # noinspection PyMethodMayBeStatic
    def get(self, request):
        print(request)
        client = mqtt.Client()
        # parent_records = Userdata.objects.filter(Usernumber=device_records[0].Parentid)
        client.username_pw_set('lalith', password='lalith56')
        client.connect(settings.IP)
        lalith = '919908799084/840D8ED6A094G/just'
        client.publish(lalith, str(request))
        ist = pytz.timezone('Asia/Calcutta')
        current_date = datetime.datetime.now(ist)

        year = current_date.date().year
        month = current_date.date().month
        day = current_date.date().day

        hours = current_date.time().hour
        minutes = current_date.time().minute
        seconds = current_date.time().second

        return JsonResponse({"y": year, "m": month, "d": day, "h": hours, "min": minutes, "s": seconds}, status=status.HTTP_200_OK)

    # noinspection PyMethodMayBeStatic
    def post(self, request):
        serializer = GoogleSerializer(data=request.data, context={'request': request})
        client = mqtt.Client()
        # parent_records = Userdata.objects.filter(Usernumber=device_records[0].Parentid)
        client.username_pw_set('lalith', password='lalith56')
        client.connect(settings.IP)
        lalith = '919908799084/840D8ED6A094G/just'
        client.publish(lalith, str(serializer))
        if not serializer.is_valid():
            data = {"INFO": serializer.errors}
            return JsonResponse(data, status=status.HTTP_400_BAD_REQUEST)
        else:
            # noinspection PyBroadException
            try:
                dealer_rec = DealerDevice.objects.get(DeviceName=serializer.data['device_no'])
                print(serializer.data['device_no'])
                print(dealer_rec.DeviceName)
                if dealer_rec.DeviceName == serializer.data['device_no']:
                    print('all okay')
                else:
                    return JsonResponse({"INFO": "UnAuthorized Access."}, status=status.HTTP_400_BAD_REQUEST)
            # noinspection PyBroadException
            except Exception as e:
                return JsonResponse({"INFO": "Not Authorized To This Device."}, status=status.HTTP_400_BAD_REQUEST)
            try:
                child_rec = Device.objects.get(Devicecompanyname=serializer.data['device_no'])
                child_rec.Parentid = serializer.data['client_phone']
                child_rec.save()
                return JsonResponse({"INFO": "Successfully added"}, status=status.HTTP_200_OK)
            except Exception as e:
                return JsonResponse({"INFO": "Contact Customer Support."}, status=status.HTTP_400_BAD_REQUEST)


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


class Email(APIView):
    permission_classes = [AllowAny]
    authentication_classes = (CsrfExemptSessionAuthentication, BasicAuthentication)

    # noinspection PyMethodMayBeStatic
    def post(self, request):
        serializer = MailSerializer(data=request.data, context={'request': request})
        if not serializer.is_valid():
            data = {"INFO": serializer.errors}
            return JsonResponse(data, status=status.HTTP_400_BAD_REQUEST)
        else:
            # noinspection PyBroadException
            try:
                res = send_mail("Customer Data G-Think", str(serializer.data), "lalithkumargoona@gmail.com", ["lalithkumargoona@gmail.com"], fail_silently=False)
                print('test::::', res)
                return JsonResponse({"INFO": "successfully updated"}, status=status.HTTP_200_OK)
            except Exception as e:
                print(e)
                return JsonResponse({"INFO": "something Went Wrong"}, status=status.HTTP_200_OK)


class UserList(APIView):
    permission_classes = [AllowAny]
    authentication_classes = (CsrfExemptSessionAuthentication, BasicAuthentication)

    # noinspection PyMethodMayBeStatic
    def post(self, request):
        serializer = UsersupSerializer(data=request.data)
        if serializer.is_valid():
            parent = Userdata.objects.filter(Usernumber=serializer.data['phone'])
            if parent.exists():
                return JsonResponse({"INFO": "number already exists"})
            parent_rec = Userdata(Usernumber=serializer.data['phone'], Is_authenticated=True)
            if 'name' in serializer.data:
                parent_rec.Username = serializer.data['name']
            if 'email' in serializer.data:
                parent_rec.Useremail = serializer.data['email']
            if 'device_id' in serializer.data:
                parent_rec.Userdeviceid = serializer.data['device_id']
            if 'created_by' in serializer.data:
                parent_rec.Createdby = serializer.data['created_by']
            parent_rec.Is_parent = True
            parent_rec.save()
            parent_rec_serialised = ParentSerializer(parent_rec, context={'request': request})
            otp_sent = False
            try:
                api = "http://control.msg91.com/api/sendotp.php"
                data = {'authkey': '241566AzbypoaVSBZB5bb9ec50', 'message': 'Your One Time Password for GThink Inventors Registration is ##OTP##.', 'sender': 'GTIPIN', 'mobile': serializer.data['phone']}
                # , 'email':serializer.data['email']}
                if 'email' in serializer.data:
                    data['email'] = serializer.data['email']
                r = requests.post(url=api, data=data)
                resp = json.loads(r.text)
                if r.status_code == 200 and resp["type"] == 'success':
                    otp_sent = True
            except ImportError:
                otp_sent = False
            return JsonResponse({"INFO": "User created successfully", "user_info": {"id": parent_rec_serialised.data['phone'], "phone": parent_rec_serialised.data['phone'], "is_authorised": parent_rec_serialised.data['is_authorised']}, "OTP_Sent": otp_sent}, status=status.HTTP_201_CREATED)
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserLogin(APIView):
    permission_classes = [AllowAny]
    authentication_classes = (CsrfExemptSessionAuthentication, BasicAuthentication)

    # noinspection PyMethodMayBeStatic
    def post(self, request):
        serializer = SendOTPSerializer(data=request.data, context={'request': request})
        if not serializer.is_valid():
            data = {"INFO": serializer.errors}
            return JsonResponse(data, status=status.HTTP_400_BAD_REQUEST)
        else:
            otp_sent = False
            try:
                try:
                    parent_rec = Userdata.objects.get(Usernumber=serializer.data['phone'])
                    print(parent_rec)
                    parent_exists = True
                except Userdata.DoesNotExist:
                    parent_exists = False
                if parent_exists is True:
                    api = "http://control.msg91.com/api/sendotp.php"
                    data = {'authkey': '241566AzbypoaVSBZB5bb9ec50', 'DLT_TE_ID': '1307164733567529230', 'sender': 'GTIPIN', 'mobile': serializer.data['phone'], 'message': 'Your One Time Password for GThink Inventors Login is ##OTP##.'}
                    if 'email' in serializer.data:
                        data['email'] = serializer.data['email']
                    if serializer.data['phone'] == '918008182410':
                        data['otp'] = '1234'
                        data['message'] = 'Your One Time Password for GThink Inventors Login is 1234.'
                        return JsonResponse({"OTP_Sent": True, "INFO": "OTP sent successfully"}, status=status.HTTP_200_OK)
                    if serializer.data['phone'] == '918885387686':
                        data['otp'] = '1234'
                        data['message'] = 'Your One Time Password for GThink Inventors Login is 1234.'
                        return JsonResponse({"OTP_Sent": True, "INFO": "OTP sent successfully"}, status=status.HTTP_200_OK)
                    if serializer.data['phone'] == '919908299089':
                        data['otp'] = '1234'
                        data['message'] = 'Your One Time Password for GThink Inventors Login is 1234.'
                        return JsonResponse({"OTP_Sent": True, "INFO": "OTP sent successfully"}, status=status.HTTP_200_OK)
                    if serializer.data['phone'] == '917989042208':
                        data['otp'] = '1234'
                        data['message'] = 'Your One Time Password for GThink Inventors Login is 1234.'
                        return JsonResponse({"OTP_Sent": True, "INFO": "OTP sent successfully"}, status=status.HTTP_200_OK)
                    if serializer.data['phone'] == '919908799084':
                        data['otp'] = '1234'
                        data['message'] = 'Your One Time Password for GThink Inventors Login is 1234.'
                        return JsonResponse({"OTP_Sent": True, "INFO": "OTP sent successfully"}, status=status.HTTP_200_OK)
                    r = requests.post(url=api, data=data)
                    resp = json.loads(r.text)
                    if r.status_code == 200 and resp["type"] == 'success':
                        otp_sent = True
                    else:
                        return JsonResponse({"OTP_Sent": otp_sent, "INFO": resp}, status=status.HTTP_200_OK)
                else:
                    return JsonResponse({"OTP_Sent": otp_sent, "INFO": "No User exists with this Phone Number."}, status=status.HTTP_400_BAD_REQUEST)
            except ImportError:
                otp_sent = False
            return JsonResponse({"OTP_Sent": otp_sent, "INFO": "OTP sent successfully"}, status=status.HTTP_200_OK)


class UserLoginalexa(APIView):
    permission_classes = [AllowAny]
    authentication_classes = (CsrfExemptSessionAuthentication, BasicAuthentication)

    # noinspection PyMethodMayBeStatic
    def post(self, request):
        print(request.data)
        serializer = SendOTPSerializer2(data=request.data, context={'request': request})
        if not serializer.is_valid():
            data = {"INFO": serializer.errors}
            return JsonResponse(data, status=status.HTTP_400_BAD_REQUEST)
        else:
            otp_sent = False
            try:
                try:
                    parent_rec = Userdata.objects.get(Usernumber=serializer.data['phone'])
                    print(parent_rec)
                    parent_exists = True
                except Userdata.DoesNotExist:
                    parent_exists = False
                if parent_exists is True:
                    api = "http://control.msg91.com/api/sendotp.php"
                    data = {'authkey': '241566AzbypoaVSBZB5bb9ec50', 'DLT_TE_ID': '1307164733567529230', 'sender': 'GTIPIN', 'mobile': serializer.data['phone'], 'message': 'Your One Time Password for GThink Inventors Login is ##OTP##.'}
                    if 'email' in serializer.data:
                        data['email'] = serializer.data['email']
                    if serializer.data['phone'] == '918008182410':
                        data['otp'] = '1234'
                        data['message'] = 'Your One Time Password for GThink Inventors Login is 1234.'
                        return JsonResponse({"OTP_Sent": True, "INFO": "OTP sent successfully"}, status=status.HTTP_200_OK)
                    if serializer.data['phone'] == '918885387686':
                        data['otp'] = '1234'
                        data['message'] = 'Your One Time Password for GThink Inventors Login is 1234.'
                        return JsonResponse({"OTP_Sent": True, "INFO": "OTP sent successfully"}, status=status.HTTP_200_OK)
                    if serializer.data['phone'] == '919908299089':
                        data['otp'] = '1234'
                        data['message'] = 'Your One Time Password for GThink Inventors Login is 1234.'
                        return JsonResponse({"OTP_Sent": True, "INFO": "OTP sent successfully"}, status=status.HTTP_200_OK)
                    if serializer.data['phone'] == '917989042208':
                        data['otp'] = '1234'
                        data['message'] = 'Your One Time Password for GThink Inventors Login is 1234.'
                        return JsonResponse({"OTP_Sent": True, "INFO": "OTP sent successfully"}, status=status.HTTP_200_OK)
                    if serializer.data['phone'] == '919908799084':
                        data['otp'] = '1234'
                        data['message'] = 'Your One Time Password for GThink Inventors Login is 1234.'
                        return JsonResponse({"OTP_Sent": True, "INFO": "OTP sent successfully"}, status=status.HTTP_200_OK)
                    r = requests.post(url=api, data=data)
                    resp = json.loads(r.text)
                    if r.status_code == 200 and resp["type"] == 'success':
                        otp_sent = True
                    else:
                        return JsonResponse({"OTP_Sent": otp_sent, "INFO": resp}, status=status.HTTP_200_OK)
                else:
                    return JsonResponse({"OTP_Sent": otp_sent, "INFO": "No User exists with this Phone Number."}, status=status.HTTP_400_BAD_REQUEST)
            except ImportError:
                otp_sent = False
            return JsonResponse({"OTP_Sent": otp_sent, "INFO": "OTP sent successfully"}, status=status.HTTP_200_OK)


class Otp2(APIView):
    permission_classes = [AllowAny]
    authentication_classes = (CsrfExemptSessionAuthentication, BasicAuthentication)

    # noinspection PyMethodMayBeStatic
    def post(self, request):
        resp = ''
        serializer = OtpSerializer(data=request.data, context={'request': request})
        if not serializer.is_valid():
            data = {"INFO": serializer.errors}
            return JsonResponse(data, status=status.HTTP_400_BAD_REQUEST)
        else:
            if serializer.data['phone'] == '918008182410' or serializer.data['phone'] == '918885387686' or serializer.data['phone'] == '919908799084' or serializer.data['phone'] == '919902999089' or serializer.data['phone'] == '917989042208':
                parent_rec = Userdata.objects.get(Usernumber=serializer.data['phone'])
                parent_rec_serialised = ParentSerializer(parent_rec, context={'request': request})
                return JsonResponse({"INFO": "User Authorised successfully", "rooms_info_available": True, "auth_key": settings.AUTH_KEY, "user_info": {"id": parent_rec_serialised.data['phone'], "name": parent_rec_serialised.data['name'], "phone": parent_rec_serialised.data['phone'], "is_authorised": parent_rec_serialised.data['is_authorised']}}, status=status.HTTP_202_ACCEPTED)
            else:
                try:
                    api = "http://control.msg91.com/api/verifyRequestOTP.php"
                    data = {'authkey': '241566AzbypoaVSBZB5bb9ec50', 'mobile': serializer.data['phone'], 'otp': serializer.data['otp']}
                    r = requests.post(url=api, data=data)
                    resp = json.loads(r.text)
                    if r.status_code == 200:
                        if resp["type"] == 'success' and resp["message"] == 'otp_verified':
                            parent_rec = Userdata.objects.get(Usernumber=serializer.data['phone'])
                            if serializer.data['req_type'] == 'signup':
                                parent_rec.is_authorised = True
                                parent_rec.is_activated = True
                            if parent_rec.BacgroundImg is None:
                                parent_rec.BacgroundImg = 'https://gthink-images-website.s3.ap-south-1.amazonaws.com/bg1+(1).png'
                            if parent_rec.ProfileImg is None:
                                parent_rec.ProfileImg = 'https://gthink-images-website.s3.ap-south-1.amazonaws.com/prof+(1).png'
                            parent_rec.device_id = serializer.data['device_id']
                            parent_rec.save()
                            parent_rec_serialised = ParentSerializer(parent_rec, context={'request': request})
                            if serializer.data['req_type'] == 'login':
                                return JsonResponse({"INFO": "User Authorised successfully", "rooms_info_available": True, "auth_key": settings.AUTH_KEY, "user_info": {"id": parent_rec_serialised.data['phone'], "name": parent_rec_serialised.data['name'], "phone": parent_rec_serialised.data['phone'], "is_authorised": parent_rec_serialised.data['is_authorised']}}, status=status.HTTP_202_ACCEPTED)
                            else:
                                return JsonResponse({"INFO": "User Authorised successfully", "rooms_info_available": False, "auth_key": settings.AUTH_KEY, "user_info": {"id": parent_rec_serialised.data['phone'], "name": parent_rec_serialised.data['name'], "phone": parent_rec_serialised.data['phone'], "is_authorised": parent_rec_serialised.data['is_authorised']}}, status=status.HTTP_202_ACCEPTED)
                        else:
                            return JsonResponse({"INFO": "Got bad response from msg91", "error": resp}, status=status.HTTP_400_BAD_REQUEST)
                    else:
                        return JsonResponse({"INFO": "Unable to authorise with the given OTP", "error": resp}, status=status.HTTP_406_NOT_ACCEPTABLE)
                except ImportError:
                    return JsonResponse({"INFO": "Unable to request msg91", "error": resp}, status=status.HTTP_400_BAD_REQUEST)


class Otp(APIView):
    permission_classes = [AllowAny]
    authentication_classes = (CsrfExemptSessionAuthentication, BasicAuthentication)

    # noinspection PyMethodMayBeStatic
    def post(self, request):
        resp = ''
        serializer = OtpSerializer(data=request.data, context={'request': request})
        if not serializer.is_valid():
            data = {"INFO": serializer.errors}
            return JsonResponse(data, status=status.HTTP_400_BAD_REQUEST)
        else:
            if serializer.data['phone'] == '918008182410' or serializer.data['phone'] == '918885387686' or serializer.data['phone'] == '919908799084' or serializer.data['phone'] == '919902999089' or serializer.data['phone'] == '917989042208':
                parent_rec = Userdata.objects.get(Usernumber=serializer.data['phone'])
                parent_rec_serialised = ParentSerializer(parent_rec, context={'request': request})
                return JsonResponse({"INFO": "User Authorised successfully", "rooms_info_available": True, "auth_key": settings.AUTH_KEY, "user_info": {"id": parent_rec_serialised.data['phone'], "name": parent_rec_serialised.data['name'], "phone": parent_rec_serialised.data['phone'], "is_authorised": parent_rec_serialised.data['is_authorised']}}, status=status.HTTP_202_ACCEPTED)
            else:
                try:
                    api = "http://control.msg91.com/api/verifyRequestOTP.php"
                    data = {'authkey': '241566AzbypoaVSBZB5bb9ec50', 'mobile': serializer.data['phone'], 'otp': serializer.data['otp']}
                    r = requests.post(url=api, data=data)
                    resp = json.loads(r.text)
                    if r.status_code == 200:
                        if resp["type"] == 'success' and resp["message"] == 'otp_verified':
                            parent_rec = Userdata.objects.get(Usernumber=serializer.data['phone'])
                            if serializer.data['req_type'] == 'signup':
                                parent_rec.is_authorised = True
                                parent_rec.is_activated = True
                            if parent_rec.BacgroundImg is None:
                                parent_rec.BacgroundImg = 'https://gthink-images-website.s3.ap-south-1.amazonaws.com/bg1+(1).png'
                            if parent_rec.ProfileImg is None:
                                parent_rec.ProfileImg = 'https://gthink-images-website.s3.ap-south-1.amazonaws.com/prof+(1).png'
                            parent_rec.device_id = serializer.data['device_id']
                            parent_rec.save()
                            parent_rec_serialised = ParentSerializer(parent_rec, context={'request': request})
                            if serializer.data['req_type'] == 'login':
                                return JsonResponse({"INFO": "User Authorised successfully", "rooms_info_available": True, "auth_key": settings.AUTH_KEY, "user_info": {"id": parent_rec_serialised.data['phone'], "name": parent_rec_serialised.data['name'], "phone": parent_rec_serialised.data['phone'], "is_authorised": parent_rec_serialised.data['is_authorised']}}, status=status.HTTP_202_ACCEPTED)
                            else:
                                return JsonResponse({"INFO": "User Authorised successfully", "rooms_info_available": False, "auth_key": settings.AUTH_KEY, "user_info": {"id": parent_rec_serialised.data['phone'], "name": parent_rec_serialised.data['name'], "phone": parent_rec_serialised.data['phone'], "is_authorised": parent_rec_serialised.data['is_authorised']}}, status=status.HTTP_202_ACCEPTED)
                        else:
                            return JsonResponse({"INFO": "Got bad response from msg91", "error": resp}, status=status.HTTP_400_BAD_REQUEST)
                    else:
                        return JsonResponse({"INFO": "Unable to authorise with the given OTP", "error": resp}, status=status.HTTP_406_NOT_ACCEPTABLE)
                except ImportError:
                    return JsonResponse({"INFO": "Unable to request msg91", "error": resp}, status=status.HTTP_400_BAD_REQUEST)


class SendOTP(APIView):
    permission_classes = [AllowAny]
    authentication_classes = (CsrfExemptSessionAuthentication, BasicAuthentication)

    # noinspection PyMethodMayBeStatic
    def post(self, request):
        serializer = SendOTPSerializer(data=request.data, context={'request': request})
        if not serializer.is_valid():
            data = {"ERROR": serializer.errors}
            return JsonResponse(data, status=status.HTTP_400_BAD_REQUEST)
        else:
            apiend = "http://control.msg91.com/api/sendotp.php"
            data = {'authkey': '241566AzbypoaVSBZB5bb9ec50', 'DLT_TE_ID': '1307164733567529230', 'sender': 'GTIPIN', 'mobile': serializer.data['phone']}
            # , 'email':serializer.data['email']}
            if 'email' in serializer.data:
                data['email'] = serializer.data['email']
            if serializer.data['req_type'] == 'signup':
                data['message'] = 'Your One Time Password for GThink Inventors Registration is ##OTP##.'
            else:
                data['message'] = 'Your One Time Password for GThink Inventors Login is ##OTP##.'

            r = requests.post(url=apiend, data=data)
            paste_bin_url = json.loads(r.text)
            return JsonResponse({"INFO": paste_bin_url}, status=status.HTTP_200_OK)


class UpdateUser(APIView):
    permission_classes = [AllowAny]
    authentication_classes = (CsrfExemptSessionAuthentication, BasicAuthentication)

    # noinspection PyMethodMayBeStatic
    def post(self, request):
        serializer = UpdateParentSerializer(data=request.data, context={'request': request})
        if not serializer.is_valid():
            data = {"INFO": serializer.errors}
            return JsonResponse(data, status=status.HTTP_400_BAD_REQUEST)
        else:
            if serializer.data['auth_key'] == settings.AUTH_KEY:
                # noinspection PyBroadException
                try:
                    parent_r = Userdata.objects.get(id=serializer.data['user_id'])
                    if 'name' in serializer.data and serializer.data['name'] != "":
                        parent_r.Username = serializer.data['name']
                    if 'email' in serializer.data and serializer.data['email'] != "":
                        parent_r.Useremail = serializer.data['email']
                    parent_r.save()
                    parent_r_serialised = ParentSerializer(parent_r, context={'request': request})
                    return JsonResponse({"INFO": "User updated successfully", "user_info": parent_r_serialised.data}, status=status.HTTP_200_OK)
                except Userdata.DoesNotExist:
                    return JsonResponse({"INFO": "No User exists with the given ID."}, status=status.HTTP_400_BAD_REQUEST)
            else:
                return JsonResponse({"INFO": "Please check the Auth-Key provided."}, status=status.HTTP_400_BAD_REQUEST)

#
# class AddChildUser(APIView):
#     permission_classes = [AllowAny]
#     authentication_classes = (CsrfExemptSessionAuthentication, BasicAuthentication)
#
#     # noinspection PyMethodMayBeStatic
#     def post(self, request):
#         serializer = ChildSignupSerializer(data=request.data, context={'request': request})
#         if not serializer.is_valid():
#             data = {"INFO": serializer.errors}
#             return JsonResponse(data, status=status.HTTP_400_BAD_REQUEST)
#         else:
#             check = Userdata.objects.filter(Usernumber=serializer.data['phone'])
#             parentkey = Userdata.objects.get(Usernumber=serializer.data['parent_id'])
#             if len(check) == 0:
#                 child_rec = Userdata(Usernumber=serializer.data['phone'], Is_authenticated=False)
#                 if 'name' in serializer.data:
#                     child_rec.Username = serializer.data['name']
#                 if 'email' in serializer.data:
#                     child_rec.Useremail = serializer.data['email']
#                 if 'device_id' in serializer.data:
#                     child_rec.Userdeviceid = serializer.data['device_id']
#                 if 'parent_id' in serializer.data:
#                     child_rec.Createdby = serializer.data['parent_id']
#                 if 'rooms' in serializer.data:
#                     child_rec.Room_Permission = serializer.data['rooms']
#                 if 'rgb_rooms' in serializer.data:
#                     child_rec.Rgb_Permission = serializer.data['rgb_rooms']
#                 child_rec.Key1 = parentkey.Key1
#                 child_rec.Key2 = parentkey.Key2
#                 child_rec.Is_parent = False
#                 child_rec.Is_action = True
#                 child_rec.Is_authenticated = True
#                 child_rec.save()
#                 child_rec_serialised = ParentSerializer(child_rec, context={'request': request})
#                 return JsonResponse({"INFO": "Child created successfully", "user_info": child_rec_serialised.data}, status=status.HTTP_201_CREATED)
#             else:
#                 child_rec = check[0]
#                 if child_rec.Is_action is None:
#                     child_rec = Userdata(Usernumber=serializer.data['phone'], Is_authenticated=False)
#                     if 'name' in serializer.data:
#                         child_rec.Username = serializer.data['name']
#                     if 'email' in serializer.data:
#                         child_rec.Useremail = serializer.data['email']
#                     if 'device_id' in serializer.data:
#                         child_rec.Userdeviceid = serializer.data['device_id']
#                     if 'parent_id' in serializer.data:
#                         child_rec.Createdby = serializer.data['parent_id']
#                     if 'rooms' in serializer.data:
#                         child_rec.Room_Permission = serializer.data['rooms']
#                     if 'rgb_rooms' in serializer.data:
#                         child_rec.Rgb_Permission = serializer.data['rgb_rooms']
#                     child_rec.Key1 = parentkey.Key1
#                     child_rec.Key2 = parentkey.Key2
#                     child_rec.Is_parent = False
#                     child_rec.Is_action = True
#                     child_rec.Is_authenticated = True
#                     child_rec.save()
#                     child_rec_serialised = ParentSerializer(child_rec, context={'request': request})
#                     return JsonResponse({"INFO": "Child created successfully", "user_info": child_rec_serialised.data}, status=status.HTTP_201_CREATED)
#                 else:
#                     return JsonResponse({"INFO": "User already with this Phone Number exists."}, status=status.HTTP_400_BAD_REQUEST)


class NewAddChildUser(APIView):
    permission_classes = [AllowAny]
    authentication_classes = (CsrfExemptSessionAuthentication, BasicAuthentication)

    # noinspection PyMethodMayBeStatic
    def post(self, request):
        serializer = ChildSignupSerializer(data=request.data, context={'request': request})
        if not serializer.is_valid():
            data = {"INFO": serializer.errors}
            return JsonResponse(data, status=status.HTTP_400_BAD_REQUEST)
        else:
            check = Userdata.objects.filter(Usernumber=serializer.data['phone'])
            parentkey = Userdata.objects.get(Usernumber=serializer.data['parent_id'])
            if len(check) == 0:
                child_rec = Userdata(Usernumber=serializer.data['phone'], Is_authenticated=False)
                if 'name' in serializer.data:
                    child_rec.Username = serializer.data['name']
                if 'email' in serializer.data:
                    child_rec.Useremail = serializer.data['email']
                if 'device_id' in serializer.data:
                    child_rec.Userdeviceid = serializer.data['device_id']
                if 'parent_id' in serializer.data:
                    child_rec.Createdby = serializer.data['parent_id']
                if 'rooms' in serializer.data:
                    child_rec.Room_Permission = serializer.data['rooms']
                if 'rgb_rooms' in serializer.data:
                    child_rec.Rgb_Permission = serializer.data['rgb_rooms']
                if parentkey.Response is not None:
                    child_rec.Unknownfield = 'some'
                child_rec.Key1 = parentkey.Key1
                child_rec.Key2 = parentkey.Key2
                child_rec.Is_parent = False
                child_rec.Is_action = True
                child_rec.Is_authenticated = True
                child_rec.save()
                child_rec_serialised = ParentSerializer(child_rec, context={'request': request})
                return JsonResponse({"INFO": "Child created successfully", "user_info": child_rec_serialised.data}, status=status.HTTP_201_CREATED)
            else:
                child_rec = check[0]
                if child_rec.Is_action is None:
                    child_rec = Userdata(Usernumber=serializer.data['phone'], Is_authenticated=False)
                    if 'name' in serializer.data:
                        child_rec.Username = serializer.data['name']
                    if 'email' in serializer.data:
                        child_rec.Useremail = serializer.data['email']
                    if 'device_id' in serializer.data:
                        child_rec.Userdeviceid = serializer.data['device_id']
                    if 'parent_id' in serializer.data:
                        child_rec.Createdby = serializer.data['parent_id']
                    if 'rooms' in serializer.data:
                        child_rec.Room_Permission = serializer.data['rooms']
                    if 'rgb_rooms' in serializer.data:
                        child_rec.Rgb_Permission = serializer.data['rgb_rooms']
                    if parentkey.Response is not None:
                        child_rec.Unknownfield = 'some'
                    child_rec.Key1 = parentkey.Key1
                    child_rec.Key2 = parentkey.Key2
                    child_rec.Is_parent = False
                    child_rec.Is_action = True
                    child_rec.Is_authenticated = True
                    child_rec.save()
                    child_rec_serialised = ParentSerializer(child_rec, context={'request': request})
                    return JsonResponse({"INFO": "Child created successfully", "user_info": child_rec_serialised.data}, status=status.HTTP_201_CREATED)
                else:
                    return JsonResponse({"INFO": "User already with this Phone Number exists."}, status=status.HTTP_400_BAD_REQUEST)


class GetChildList(APIView):
    permission_classes = [AllowAny]
    authentication_classes = (CsrfExemptSessionAuthentication, BasicAuthentication)

    # noinspection PyMethodMayBeStatic
    def post(self, request):
        serializer = GetChildListSerializer(data=request.data, context={'request': request})
        if not serializer.is_valid():
            data = {"INFO": serializer.errors}
            return JsonResponse(data, status=status.HTTP_400_BAD_REQUEST)
        else:
            child_list_data = Userdata.objects.filter(Createdby=serializer.data['parent_id']).values()
            child_recs_serialised = ParentSerializer(child_list_data, many=True, context={'request': request})
            return JsonResponse({"child_list": child_recs_serialised.data}, status=status.HTTP_200_OK)


class DeleteChild(APIView):
    permission_classes = [AllowAny]
    authentication_classes = (CsrfExemptSessionAuthentication, BasicAuthentication)

    # noinspection PyMethodMayBeStatic
    def post(self, request):
        serializer = DeleteChildSerializer(data=request.data, context={'request': request})
        if not serializer.is_valid():
            data = {"INFO": serializer.errors}
            return JsonResponse(data, status=status.HTTP_400_BAD_REQUEST)
        else:
            try:
                child_rec = Userdata.objects.get(Usernumber=serializer.data['child_id'])
                child_rec.delete()
                return JsonResponse({"INFO": "Child deleted successfully"}, status=status.HTTP_200_OK)
            except Userdata.DoesNotExist:
                return JsonResponse({"INFO": "No child exists with the given ID."}, status=status.HTTP_400_BAD_REQUEST)


class UpdateChild(APIView):
    permission_classes = [AllowAny]
    authentication_classes = (CsrfExemptSessionAuthentication, BasicAuthentication)

    # noinspection PyMethodMayBeStatic
    def post(self, request):
        serializer = UpdateChildSerializer(data=request.data, context={'request': request})
        if not serializer.is_valid():
            data = {"INFO": serializer.errors}
            return JsonResponse(data, status=status.HTTP_400_BAD_REQUEST)
        else:
            # noinspection PyBroadException
            try:
                child_rec = Userdata.objects.get(Usernumber=serializer.data['child_id'])
                if serializer.data['rooms'] != 'null':
                    child_rec.Room_Permission = serializer.data['rooms']
                else:
                    child_rec.Rgb_Permission = serializer.data['rgb_rooms']
                child_rec.save()
                child_rec_serialised = ParentSerializer(child_rec, context={'request': request})
                return JsonResponse({"INFO": "Child updated successfully", "child_info": child_rec_serialised.data}, status=status.HTTP_200_OK)
            except Userdata.DoesNotExist:
                return JsonResponse({"INFO": "No child exists with the given ID."}, status=status.HTTP_400_BAD_REQUEST)


class NewUpdateChild(APIView):
    permission_classes = [AllowAny]
    authentication_classes = (CsrfExemptSessionAuthentication, BasicAuthentication)

    # noinspection PyMethodMayBeStatic
    def post(self, request):
        serializer = NewUpdateChildSerializer(data=request.data, context={'request': request})
        if not serializer.is_valid():
            data = {"INFO": serializer.errors}
            return JsonResponse(data, status=status.HTTP_400_BAD_REQUEST)
        else:
            print(serializer.data)
            # noinspection PyBroadException
            try:
                child_rec = Userdata.objects.get(Usernumber=serializer.data['child_id'])
                permission = serializer.data['rooms']
                #  permission2 = json.loads(permission)
                action_type = serializer.data['action']
                present_rooms = child_rec.Room_Permission
                if action_type == 'add':
                    # present_rooms2 = json.loads(present_rooms)
                    total_data = present_rooms + permission
                    child_rec.Room_Permission = total_data
                    child_rec.save()
                    return JsonResponse({"INFO": "Child Rooms added successfully", "child_info": "ok"}, status=status.HTTP_200_OK)
                elif action_type == 'update':
                    if serializer.data['rooms'] != 'null':
                        child_rec.Room_Permission = serializer.data['rooms']
                    else:
                        child_rec.Rgb_Permission = serializer.data['rgb_rooms']
                    child_rec.save()
                    return JsonResponse({"INFO": "Child updated successfully", "child_info": "ok"}, status=status.HTTP_200_OK)
            except Userdata.DoesNotExist:
                return JsonResponse({"INFO": "No child exists with the given ID."}, status=status.HTTP_400_BAD_REQUEST)


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
            if serializer.data['auth_key'] == settings.AUTH_KEY:
                try:
                    acsame = Scheduling.objects.filter(Devicename=serializer.data['device_id']).filter(Action=serializer.data['action']).filter(Timestamp=serializer.data['fire_date'])
                    if len(acsame) != 0:
                        return JsonResponse({"INFO": "Already Added With Same Values"}, status=status.HTTP_400_BAD_REQUEST)
                    dev_data = Scheduling(Devicename=serializer.data['device_id'], Action=serializer.data['action'], Timestamp=serializer.data['fire_date'])
                    dev_data.save()
                    # os.system('at now < a.txt')
                    return JsonResponse({"INFO": "Scheduled successfully"}, status=status.HTTP_201_CREATED)
                except Scheduling.DoesNotExist:
                    return JsonResponse({"INFO": "Exception"}, status=status.HTTP_400_BAD_REQUEST)
            else:
                return JsonResponse({"INFO": "Please check the Auth-Key provided."}, status=status.HTTP_400_BAD_REQUEST)


class DeleteSchedule(APIView):
    permission_classes = [AllowAny]
    authentication_classes = (CsrfExemptSessionAuthentication, BasicAuthentication)

    # noinspection PyMethodMayBeStatic
    def post(self, request):
        serializer = DeleteScheduleSerializer(data=request.data, context={'request': request})
        if not serializer.is_valid():
            data = {"INFO": serializer.errors}
            return JsonResponse(data, status=status.HTTP_400_BAD_REQUEST)
        else:
            try:
                dev_sched = Scheduling.objects.get(Devicename=serializer.data['device_id'], Action=serializer.data['action'], Timestamp=serializer.data['fire_date'])
                dev_sched.delete()
                return JsonResponse({"INFO": "Schedule deleted successfully"}, status=status.HTTP_200_OK)
            except Scheduling.DoesNotExist:
                return JsonResponse({"INFO": "No device exists with the given ID."}, status=status.HTTP_400_BAD_REQUEST)


class DeleteScheduleDevice(APIView):
    permission_classes = [AllowAny]
    authentication_classes = (CsrfExemptSessionAuthentication, BasicAuthentication)

    # noinspection PyMethodMayBeStatic
    def post(self, request):
        serializer = DeleteScheduleDeviceSerializer(data=request.data, context={'request': request})
        if not serializer.is_valid():
            data = {"INFO": serializer.errors}
            return JsonResponse(data, status=status.HTTP_400_BAD_REQUEST)
        else:
            try:
                Scheduling.objects.filter(Devicename=serializer.data['device_id'])
                device_scheduling = Scheduling.objects.get(Devicename=serializer.data['device_id'], id=serializer.data['id'])
                device_scheduling.delete()
                return JsonResponse({"INFO": "Schedule deleted successfully"}, status=status.HTTP_200_OK)
            except Scheduling.DoesNotExist:
                return JsonResponse({"INFO": "No device exists with the given ID."}, status=status.HTTP_400_BAD_REQUEST)


class GetScheduleInfo(APIView):
    permission_classes = [AllowAny]
    authentication_classes = (CsrfExemptSessionAuthentication, BasicAuthentication)

    # noinspection PyMethodMayBeStatic
    def get(self, request, device_id):
        serializer = DeviceSerializer(data={'device_id': device_id}, context={'request': request})

        if not(serializer.is_valid()):
            data = {"error": "invalid_request", "error_description": serializer.errors}
            return JsonResponse(data, status=status.HTTP_400_BAD_REQUEST)
        else:
            scheduling_records = Scheduling.objects.filter(Devicename=serializer.data['device_id'])
            if len(scheduling_records) > 0:
                ser_resp = DeviceSchedulingSerializer(scheduling_records, many=True)
                return JsonResponse({"schedule_info": ser_resp.data}, status=status.HTTP_200_OK)
            else:
                data = {"INFO": "No scheduling available for this device"}
                return JsonResponse(data, status=status.HTTP_200_OK)


class GetScheduleInfoApps(APIView):
    permission_classes = [AllowAny]
    authentication_classes = (CsrfExemptSessionAuthentication, BasicAuthentication)

    # noinspection PyMethodMayBeStatic
    def get(self, request, device_id):
        serializer = DeviceSerializer(data={'device_id': device_id}, context={'request': request})

        if not(serializer.is_valid()):
            data = {"error": "invalid_request", "error_description": serializer.errors}
            return JsonResponse(data, status=status.HTTP_400_BAD_REQUEST)
        else:
            sched_records = Scheduling.objects.filter(Devicename=serializer.data['device_id'])
            if len(sched_records) > 0:
                ser_resp = DeviceSchedulingSerializerApps(sched_records, many=True)
                return JsonResponse({"schedule_info": ser_resp.data}, status=status.HTTP_200_OK)
            else:
                data = {"INFO": "No scheduling available for this device"}
                return JsonResponse(data, status=status.HTTP_200_OK)


class Time(APIView):
    permission_classes = [AllowAny]
    authentication_classes = (CsrfExemptSessionAuthentication, BasicAuthentication)

    # noinspection PyMethodMayBeStatic
    def get(self, request):
        print(request)
        ist = pytz.timezone('Asia/Calcutta')
        current_date = datetime.datetime.now(ist)

        year = current_date.date().year
        month = current_date.date().month
        day = current_date.date().day

        hours = current_date.time().hour
        minutes = current_date.time().minute
        seconds = current_date.time().second

        return JsonResponse({"y": year, "m": month, "d": day, "h": hours, "min": minutes, "s": seconds}, status=status.HTTP_200_OK)


class DeviceRecognition(APIView):
    permission_classes = [AllowAny]
    authentication_classes = (CsrfExemptSessionAuthentication, BasicAuthentication)

    # noinspection PyMethodMayBeStatic
    def get(self, request, device_id):
        serializer = DeviceSerializer(data={'device_id': device_id}, context={'request': request})
        if not(serializer.is_valid()):
            data = {"error": "invalid_request", "error_description": serializer.errors}
            return JsonResponse(data, status=status.HTTP_400_BAD_REQUEST)
        else:
            device_records = Device.objects.filter(Devicename=serializer.data['device_id'])
            print(device_records)
            if len(device_records) > 0:
                dev_rec = device_records[0]
                current_time = datetime.datetime.now()
                last_requested_time = dev_rec.Lastrequested
                if last_requested_time is None:
                    dev_rec.Lastrequested = current_time
                    dev_rec.Requestcount = dev_rec.Requestcount+1
                    dev_rec.save()
                else:
                    duration = current_time - last_requested_time
                    duration_in_s = duration.total_seconds()
                    if duration_in_s/60 < 15:
                        if dev_rec.Requestcount == 10:
                            # send email and make the count to Zero
                            try:
                                if "CC50E395C58C" != serializer.data['device_id']:
                                    res = send_mail('Multiple requests from this Device id: '+serializer.data['device_id']+' in last 15 minutes', 'Please check this device as soon as possible.', settings.EMAIL_HOST_USER, [settings.EMAIL_RECEPIENTS])
                                    if res == 1:
                                        dev_rec.Requestcount = 0
                                        dev_rec.save()
                            except Exception as e:
                                print(e)
                        else:
                            dev_rec.Lastrequested = current_time
                            dev_rec.Requestcount = dev_rec.Requestcount+1
                            dev_rec.save()
                    else:
                        dev_rec.Lastrequested = current_time
                        dev_rec.Requestcount = 0
                        dev_rec.save()
                parent_records = Userdata.objects.filter(Usernumber=device_records[0].Parentid)
                if len(parent_records) > 0:
                    if device_records[0].Devicenumber == 0:
                        lalith = parent_records[0].Usernumber + '/' + serializer.data['device_id'] + settings.ENCRPT
                    else:
                        lalith = parent_records[0].Usernumber + '/' + device_records[0].Deviceparent + settings.ENCRPT
                    tdata = json.loads(device_records[0].Namer)
                    data_set = '['
                    for ll in range(len(tdata)):
                        data_set = str(data_set) + device_records[0].Deviceusername + ' ' + tdata[ll]
                        if ll != len(tdata) - 1:
                            data_set += ','
                    data_set += ']'
                    return JsonResponse({"IP": settings.IP, "PORT": settings.IP_PORT, "all_on": settings.ALL_ON, "all_off": settings.ALL_OFF, "dame": data_set, "time": settings.TIME, "skd": settings.SKD, "key1": parent_records[0].Key1, "key2": parent_records[0].Key2, "NAME": lalith, "pd": device_records[0].Publisheddata, "work": device_records[0].Work, "NState": device_records[0].Notification_State}, status=status.HTTP_200_OK)
                else:
                    return JsonResponse({"Lalith": "just", "IP": "192.168.0.104", "PORT": "1883", "key1": "lalith", "key2": "lalith56", "NAME": "918008182410"}, status=status.HTTP_200_OK)
            else:
                device_records2 = RGB.objects.filter(RGB_Devicename=serializer.data['device_id'])
                if len(device_records2) > 0:
                    dev_rec = device_records2[0]
                    current_time = datetime.datetime.now()
                    last_requested_time = dev_rec.RGB_Lastrequested
                    if last_requested_time is None:
                        dev_rec.RGB_Lastrequested = current_time
                        dev_rec.RGB_Requestcount = dev_rec.RGB_Requestcount + 1
                        dev_rec.save()
                    else:
                        duration = current_time - last_requested_time
                        duration_in_s = duration.total_seconds()
                        if duration_in_s / 60 < 15:
                            if dev_rec.RGB_Requestcount == 10:
                                # send email and make the count to Zero
                                try:
                                    if "CC50E395C58C" != serializer.data['device_id']:
                                        res = send_mail('Multiple requests from this Device id: ' + serializer.data[
                                            'device_id'] + ' in last 15 minutes',
                                                        'Please check this device as soon as possible.',
                                                        settings.EMAIL_HOST_USER, [settings.EMAIL_RECEPIENTS])
                                        if res == 1:
                                            dev_rec.RGB_Requestcount = 0
                                            dev_rec.save()
                                except Exception as e:
                                    print(e)
                            else:
                                dev_rec.RGB_Lastrequested = current_time
                                dev_rec.RGB_Requestcount = dev_rec.RGB_Requestcount + 1
                                dev_rec.save()
                        else:
                            dev_rec.RGB_Lastrequested = current_time
                            dev_rec.RGB_Requestcount = 0
                            dev_rec.save()
                    parent_records = Userdata.objects.filter(Usernumber=device_records2[0].RGB_Parentid)
                    if len(parent_records) > 0:
                        # if device_records[0].Devicenumber == 0:
                        #     lalith = parent_records[0].Usernumber + '/' + serializer.data['device_id'] + settings.ENCRPT
                        # else:
                        #     lalith = parent_records[0].Usernumber + '/' + device_records[
                        #         0].Deviceparent + settings.ENCRPT
                        lalith = parent_records[0].Usernumber + '/' + serializer.data['device_id'] + settings.ENCRPT
                        return JsonResponse({"IP": settings.IP, "PORT": settings.IP_PORT, "all_on": settings.ALL_ON,
                                             "all_off": settings.ALL_OFF, "time": settings.TIME, "skd": settings.SKD,
                                             "key1": parent_records[0].Key1, "key2": parent_records[0].Key2,
                                             "NAME": lalith, "pd": device_records2[0].RGB_Publisheddata
                                             }, status=status.HTTP_200_OK)
                    else:
                        return JsonResponse({"Lalith": "just", "IP": "192.168.0.104", "PORT": "1883", "key1": "lalith",
                                             "key2": "lalith56", "NAME": "918008182410"}, status=status.HTTP_200_OK)
                else:
                    res = send_mail("Device Requesting Please Forward this.", str(serializer.data['device_id']), "lalithkumargoona@gmail.com", ["lalithkumargoona@gmail.com"], fail_silently=False)
                    return JsonResponse({"INFO": "No Device is registered with this Name. Please check the database." + str(res)}, status=status.HTTP_400_BAD_REQUEST)


class IRDeviceRecognition(APIView):
    permission_classes = [AllowAny]
    authentication_classes = (CsrfExemptSessionAuthentication, BasicAuthentication)

    # noinspection PyMethodMayBeStatic
    def get(self, request, device_id):
        serializer = DeviceSerializer(data={'device_id': device_id}, context={'request': request})
        if not(serializer.is_valid()):
            data = {"error": "invalid_request", "error_description": serializer.errors}
            return JsonResponse(data, status=status.HTTP_400_BAD_REQUEST)
        else:
            device_records = IRDevice.objects.filter(DeviceName=serializer.data['device_id'])
            print(device_records)
            if len(device_records) > 0:
                dev_rec = device_records[0]
                current_time = datetime.datetime.now()
                last_requested_time = dev_rec.LastRequested
                if last_requested_time is None:
                    dev_rec.LastRequested = current_time
                    dev_rec.save()
                parent_records = Userdata.objects.filter(Usernumber=device_records[0].ParentId)
                if len(parent_records) > 0:
                    lalith = parent_records[0].Usernumber + '/' + serializer.data['device_id'] + settings.ENCRPT
                    return JsonResponse({"IP": settings.IP, "PORT": settings.IP_PORT, "all_on": settings.ALL_ON, "all_off": settings.ALL_OFF, "time": settings.TIME, "skd": settings.SKD, "key1": parent_records[0].Key1, "key2": parent_records[0].Key2, "NAME": lalith, "pd": device_records[0].PublishedData}, status=status.HTTP_200_OK)
                else:
                    res = send_mail("Device Requesting Please Forward this.", str(serializer.data['device_id']), "lalithkumargoona@gmail.com", ["lalithkumargoona@gmail.com"], fail_silently=False)
                    return JsonResponse({"INFO": "No Device is registered with this Name. Please check the database." + str(res)}, status=status.HTTP_400_BAD_REQUEST)


class RGBDeviceRecognition(APIView):
    permission_classes = [AllowAny]
    authentication_classes = (CsrfExemptSessionAuthentication, BasicAuthentication)

    # noinspection PyMethodMayBeStatic
    def get(self, request, device_id):
        serializer = DeviceSerializer(data={'device_id': device_id}, context={'request': request})
        if not(serializer.is_valid()):
            data = {"error": "invalid_request", "error_description": serializer.errors}
            return JsonResponse(data, status=status.HTTP_400_BAD_REQUEST)
        else:
            device_records2 = RGB.objects.filter(RGB_Devicename=serializer.data['device_id'])
            if len(device_records2) > 0:
                dev_rec = device_records2[0]
                current_time = datetime.datetime.now()
                last_requested_time = dev_rec.RGB_Lastrequested
                if last_requested_time is None:
                    dev_rec.RGB_Lastrequested = current_time
                    dev_rec.RGB_Requestcount = dev_rec.RGB_Requestcount + 1
                    dev_rec.save()
                else:
                    duration = current_time - last_requested_time
                    duration_in_s = duration.total_seconds()
                    if duration_in_s / 60 < 15:
                        if dev_rec.RGB_Requestcount == 10:
                            # send email and make the count to Zero
                            try:
                                if "CC50E395C58C" != serializer.data['device_id']:
                                    res = send_mail('Multiple requests from this Device id: ' + serializer.data[
                                        'device_id'] + ' in last 15 minutes',
                                                    'Please check this device as soon as possible.',
                                                    settings.EMAIL_HOST_USER, [settings.EMAIL_RECEPIENTS])
                                    if res == 1:
                                        dev_rec.RGB_Requestcount = 0
                                        dev_rec.save()
                            except Exception as e:
                                print(e)
                        else:
                            dev_rec.RGB_Lastrequested = current_time
                            dev_rec.RGB_Requestcount = dev_rec.RGB_Requestcount + 1
                            dev_rec.save()
                    else:
                        dev_rec.RGB_Lastrequested = current_time
                        dev_rec.RGB_Requestcount = 0
                        dev_rec.save()
                parent_records = Userdata.objects.filter(Usernumber=device_records2[0].RGB_Parentid)
                if len(parent_records) > 0:
                    # if device_records[0].Devicenumber == 0:
                    #     lalith = parent_records[0].Usernumber + '/' + serializer.data['device_id'] + settings.ENCRPT
                    # else:
                    #     lalith = parent_records[0].Usernumber + '/' + device_records[
                    #         0].Deviceparent + settings.ENCRPT
                    lalith = parent_records[0].Usernumber + '/' + serializer.data['device_id'] + settings.ENCRPT
                    return JsonResponse({"IP": settings.IP, "PORT": settings.IP_PORT, "all_on": settings.ALL_ON,
                                         "all_off": settings.ALL_OFF, "time": settings.TIME, "skd": settings.SKD,
                                         "key1": parent_records[0].Key1, "key2": parent_records[0].Key2,
                                         "NAME": lalith, "pd": device_records2[0].RGB_Publisheddata
                                         }, status=status.HTTP_200_OK)
                else:
                    return JsonResponse({"Lalith": "just", "IP": "192.168.0.104", "PORT": "1883", "key1": "lalith",
                                         "key2": "lalith56", "NAME": "918008182410"}, status=status.HTTP_200_OK)
            else:
                res = send_mail("Device Requesting Please Forward this.", str(serializer.data['device_id']), "lalithkumargoona@gmail.com", ["lalithkumargoona@gmail.com"], fail_silently=False)
                return JsonResponse({"INFO": "No Device is registered with this Name. Please check the database." + str(res)}, status=status.HTTP_400_BAD_REQUEST)


class CloneDeviceRecognition(APIView):
    permission_classes = [AllowAny]
    authentication_classes = (CsrfExemptSessionAuthentication, BasicAuthentication)

    # noinspection PyMethodMayBeStatic
    def get(self, request, device_id):
        serializer = DeviceSerializer(data={'device_id': device_id}, context={'request': request})
        if not(serializer.is_valid()):
            data = {"error": "invalid_request", "error_description": serializer.errors}
            return JsonResponse(data, status=status.HTTP_400_BAD_REQUEST)
        else:
            device_records = TouchCloneDevice.objects.filter(DeviceName=serializer.data['device_id'])
            if len(device_records) > 0:
                dev_rec = device_records[0]
                lalith = dev_rec.ParentId + '/' + dev_rec.ParentDevice + settings.ENCRPT
                parent_records = Userdata.objects.filter(Usernumber=device_records[0].ParentId)
                parent_device = Device.objects.filter(Devicename=device_records[0].ParentDevice)
                return JsonResponse({"IP": settings.IP, "PORT": settings.IP_PORT, "key1": parent_records[0].Key1, "key2": parent_records[0].Key2, "NAME": lalith, "pd": parent_device[0].Publisheddata}, status=status.HTTP_200_OK)
            else:
                res = send_mail("Device Requesting Please Forward this.", str(serializer.data['device_id']), "lalithkumargoona@gmail.com", ["lalithkumargoona@gmail.com"], fail_silently=False)
                return JsonResponse({"INFO": "No Device is registered with this Name. Please check the database." + str(res)}, status=status.HTTP_400_BAD_REQUEST)


class SemiCloneDeviceRecognition(APIView):
    permission_classes = [AllowAny]
    authentication_classes = (CsrfExemptSessionAuthentication, BasicAuthentication)

    # noinspection PyMethodMayBeStatic
    def get(self, request, device_id):
        serializer = DeviceSerializer(data={'device_id': device_id}, context={'request': request})
        if not(serializer.is_valid()):
            data = {"error": "invalid_request", "error_description": serializer.errors}
            return JsonResponse(data, status=status.HTTP_400_BAD_REQUEST)
        else:
            device_records = SemiCloneDevice.objects.filter(DeviceName=serializer.data['device_id'])
            if len(device_records) > 0:
                parent_records = Userdata.objects.filter(Usernumber=device_records[0].ParentId)
                lalith = parent_records[0].Usernumber + '/' + serializer.data['device_id'] + settings.ENCRPT
                return JsonResponse({"IP": settings.IP, "PORT": settings.IP_PORT, "all_on": settings.ALL_ON, "all_off": settings.ALL_OFF, "key1": parent_records[0].Key1, "key2": parent_records[0].Key2, "NAME": lalith, "pd": device_records[0].Publisheddata, "sd": device_records[0].ActionDevice}, status=status.HTTP_200_OK)
            else:
                res = send_mail("Device Requesting Please Forward this.", str(serializer.data['device_id']), "lalithkumargoona@gmail.com", ["lalithkumargoona@gmail.com"], fail_silently=False)
                return JsonResponse({"INFO": "No Device is registered with this Name. Please check the database." + str(res)}, status=status.HTTP_400_BAD_REQUEST)


class RemoteRecognition(APIView):
    permission_classes = [AllowAny]
    authentication_classes = (CsrfExemptSessionAuthentication, BasicAuthentication)

    # noinspection PyMethodMayBeStatic
    def get(self, request, device_id):
        serializer = DeviceSerializer(data={'device_id': device_id}, context={'request': request})
        if not(serializer.is_valid()):
            data = {"error": "invalid_request", "error_description": serializer.errors}
            return JsonResponse(data, status=status.HTTP_400_BAD_REQUEST)
        else:
            device_records = IRDevice.objects.filter(DeviceName=serializer.data['device_id'])
            if len(device_records) > 0:
                dev_rec = device_records[0]
                current_time = datetime.datetime.now()
                last_requested_time = dev_rec.LastRequested
                if last_requested_time is None:
                    dev_rec.LastRequested = current_time
                    dev_rec.save()
                else:
                    duration = current_time - last_requested_time
                    duration_in_s = duration.total_seconds()
                    if duration_in_s/60 < 15:
                        # send email and make the count to Zero
                        try:
                            res = send_mail('Multiple requests from this Device id: '+serializer.data['device_id']+' in last 15 minutes', 'Please check this device as soon as possible.', settings.EMAIL_HOST_USER, [settings.EMAIL_RECEPIENTS])
                            if res == 1:
                                dev_rec.Requestcount = 0
                                dev_rec.save()
                        except Exception as e:
                            print(e)
                        dev_rec.LastRequested = current_time
                        dev_rec.save()
                    else:
                        dev_rec.LastRequested = current_time
                        dev_rec.save()
                parent_records = Userdata.objects.filter(Usernumber=device_records[0].ParentId)
                if len(parent_records) > 0:
                    lalith = parent_records[0].Usernumber + '/' + serializer.data['device_id'] + settings.ENCRPT
                    return JsonResponse({"IP": settings.IP, "PORT": settings.IP_PORT, "key1": parent_records[0].Key1, "key2": parent_records[0].Key2, "NAME": lalith, "pd": device_records[0].PublishedData}, status=status.HTTP_200_OK)
                else:
                    return JsonResponse({"Lalith": "just", "IP": "192.168.0.104", "PORT": "1883", "key1": "lalith", "key2": "lalith56", "NAME": "918008182410"}, status=status.HTTP_200_OK)
            else:
                res = send_mail("Device Requesting Please Forward this.", str(serializer.data['device_id']), "lalithkumargoona@gmail.com", ["lalithkumargoona@gmail.com"], fail_silently=False)
                return JsonResponse({"INFO": "No Device is registered with this Name. Please check the database. " + str(res)}, status=status.HTTP_400_BAD_REQUEST)


class Alexa(APIView):
    permission_classes = [AllowAny]
    authentication_classes = (CsrfExemptSessionAuthentication, BasicAuthentication)

    # noinspection PyMethodMayBeStatic
    def get(self, request, device_id, switch_state):
        serializer = AlexaDeviceSerializer(data={'device_id': device_id, 'switch_state': switch_state}, context={'request': request})
        if not(serializer.is_valid()):
            data = {"error": "invalid_request", "error_description": serializer.errors}
            return JsonResponse(data, status=status.HTTP_400_BAD_REQUEST)
        else:
            device_data = serializer.data['device_id']
            action_data = serializer.data['switch_state']
            device_mac = device_data[:12]
            action = device_data.replace(device_mac, "")
            device_records = Device.objects.filter(Devicename=device_mac)
            if len(device_records) > 0:
                client = mqtt.Client()
                parent_records = Userdata.objects.filter(Usernumber=device_records[0].Parentid)
                client.username_pw_set(parent_records[0].Key1, password=parent_records[0].Key2)
                client.connect(settings.IP)
                lalith = device_records[0].Parentid + '/' + device_mac + settings.ENCRPT + '/Device/' + action
                if len(action) == 1:
                    if action_data == '0':
                        client.publish(lalith, "00")
                    elif action_data == '255':
                        client.publish(lalith, "11")
                else:
                    data = int((int(action_data)+1)/43)
                    client.publish(lalith, action + str(data))
                return JsonResponse({"IP": lalith}, status=status.HTTP_200_OK)
            else:
                return JsonResponse({"INFO": "No Device is registered with this Name. Please check the database."}, status=status.HTTP_400_BAD_REQUEST)


class SsidPassUpdate(APIView):
    permission_classes = [AllowAny]
    authentication_classes = (CsrfExemptSessionAuthentication, BasicAuthentication)

    # noinspection PyMethodMayBeStatic
    def post(self, request):
        serializer = CodeUpdateSerializer(data=request.data, context={'request': request})
        if not serializer.is_valid():
            data = {"INFO": serializer.errors}
            return JsonResponse(data, status=status.HTTP_400_BAD_REQUEST)
        else:
            # noinspection PyBroadException
            try:
                device_records = Device.objects.filter(Devicecompanyname=serializer.data['GCode'])
                if len(device_records) > 0:
                    check = device_records[0]
                    device_mac = check.Devicename
                    action = serializer.data['URL']
                    lalith = device_records[0].Parentid + '/' + device_mac + settings.ENCRPT + '/WUpdate'
                    print(lalith)
                    client = mqtt.Client()
                    parent_records = Userdata.objects.filter(Usernumber=check.Parentid)
                    client.username_pw_set(parent_records[0].Key1, password=parent_records[0].Key2)
                    client.connect(settings.IP)
                    client.publish(lalith, action)
                    return JsonResponse({"INFO": "Update Sent"}, status=status.HTTP_200_OK)
                else:
                    return JsonResponse({"INFO": "No Device is registered with this Name. Please check the database."}, status=status.HTTP_400_BAD_REQUEST)
            except Exception as e:
                print(e)
                return JsonResponse({"INFO": "Check"}, status=status.HTTP_200_OK)


class CodeUpdate(APIView):
    permission_classes = [AllowAny]
    authentication_classes = (CsrfExemptSessionAuthentication, BasicAuthentication)

    # noinspection PyMethodMayBeStatic
    def post(self, request):
        serializer = CodeUpdateSerializer(data=request.data, context={'request': request})
        if not serializer.is_valid():
            data = {"INFO": serializer.errors}
            return JsonResponse(data, status=status.HTTP_400_BAD_REQUEST)
        else:
            # noinspection PyBroadException
            try:
                device_records = Device.objects.filter(Devicecompanyname=serializer.data['GCode'])
                device_records_rgb = RGB.objects.filter(RGB_Devicecompanyname=serializer.data['GCode'])
                device_records_ir = IRDevice.objects.filter(DeviceCompanyName=serializer.data['GCode'])
                if len(device_records) > 0:
                    check = device_records[0]
                    device_mac = check.Devicename
                    action = serializer.data['URL']
                    lalith = device_records[0].Parentid + '/' + device_mac + settings.ENCRPT + '/Update'
                    client = mqtt.Client()
                    parent_records = Userdata.objects.filter(Usernumber=check.Parentid)
                    client.username_pw_set(parent_records[0].Key1, password=parent_records[0].Key2)
                    client.connect(settings.IP)
                    client.publish(lalith, action)
                    return JsonResponse({"INFO": "Update Sent"}, status=status.HTTP_200_OK)
                elif len(device_records_rgb) > 0:
                    check = device_records_rgb[0]
                    device_mac = check.RGB_Devicename
                    action = serializer.data['URL']
                    lalith = device_records_rgb[0].RGB_Parentid + '/' + device_mac + settings.ENCRPT + '/Update'
                    client = mqtt.Client()
                    parent_records = Userdata.objects.filter(Usernumber=check.RGB_Parentid)
                    client.username_pw_set(parent_records[0].Key1, password=parent_records[0].Key2)
                    client.connect(settings.IP)
                    client.publish(lalith, action)
                    return JsonResponse({"INFO": "Update Sent"}, status=status.HTTP_200_OK)
                elif len(device_records_ir) > 0:
                    check = device_records_ir[0]
                    device_mac = check.DeviceName
                    action = serializer.data['URL']
                    lalith = device_records_ir[0].ParentId + '/' + device_mac + settings.ENCRPT + '/Update'
                    client = mqtt.Client()
                    parent_records = Userdata.objects.filter(Usernumber=check.ParentId)
                    client.username_pw_set(parent_records[0].Key1, password=parent_records[0].Key2)
                    client.connect(settings.IP)
                    client.publish(lalith, action)
                    return JsonResponse({"INFO": "Update Sent"}, status=status.HTTP_200_OK)
            except Exception as e:
                print(e)
                return JsonResponse({"INFO": "Check"}, status=status.HTTP_200_OK)


class Alexa_name_list(APIView):
    permission_classes = [AllowAny]
    authentication_classes = (CsrfExemptSessionAuthentication, BasicAuthentication)

    # noinspection PyMethodMayBeStatic
    def post(self, request):
        serializer = RoomsInfoSerializer(data=request.data, context={'request': request})
        if not serializer.is_valid():
            data = {"INFO": serializer.errors}
            return JsonResponse(data, status=status.HTTP_400_BAD_REQUEST)
        else:
            if serializer.data['auth_key'] == settings.AUTH_KEY:
                try:
                    parent_recognition = Userdata.objects.get(Usernumber=serializer.data['phone'])
                    print(parent_recognition)
                    account_exists = True
                except Exception as e:
                    print(e)
                    account_exists = False
                if account_exists is True:
                    parent_rec = Userdata.objects.get(Usernumber=serializer.data['phone'])
                    if parent_rec.Is_action is True:
                        if parent_rec.Response is None:
                            try:
                                data_set = ' '
                                if parent_rec.Is_parent is True:
                                    parent_resp_id = parent_rec.Usernumber
                                    room_resp = Device.objects.filter(Parentid=parent_resp_id).values()
                                    child_recs_serialised = RoomSerializer(room_resp, many=True)
                                    for length in range(child_recs_serialised.data.__len__()):
                                        tdata = child_recs_serialised.data[length]
                                        pubdata = json.loads(tdata['Publisheddata'])
                                        namea = json.loads(tdata['Namer'])
                                        dname = tdata['Devicename']
                                        if serializer.data['phone'] == '919908799084':
                                            duname = tdata['Devicecompanyname']
                                        else:
                                            duname = tdata['Deviceusername']
                                        data_set = str(data_set) + '\n Room Name:   ' + str(duname) + '\n'
                                        for ll in range(len(pubdata)):
                                            data_set = str(data_set) + '            Company_name:  ' + str(dname) + str(pubdata[ll]) + '   Device Name:  ' + str(namea[ll])
                                            if ll != len(pubdata)-1:
                                                data_set += ',\n'
                                        data_set += ''
                                        if length != child_recs_serialised.data.__len__()-1:
                                            data_set += ','
                                return HttpResponse(data_set)# return JsonResponse({"Alexa names: ": data_set}, status=status.HTTP_200_OK)
                            except Exception as e:
                                print(e)
                                return JsonResponse({"INFO": e}, status=status.HTTP_400_BAD_REQUEST)
                        else:
                            if parent_rec.Is_parent is True:
                                try:
                                    room_resp = UserRoomInfo.objects.filter(UserNumber=serializer.data['phone']).values()
                                    child_recs_serialised = UserRoomInfoListSerializer(room_resp, many=True)
                                    res_data = child_recs_serialised.data
                                    res_data = json.dumps(res_data)
                                    res_data2 = str(res_data).replace('\\', '').replace('"roomd": "', '"roomd": [').replace('"}]}"}, {', '"}]}]}, {').replace('}]}"}]', '}]}]}]')
                                    res_data3 = '{"rooms":' + res_data2 + '}'
                                    res_data3 = json.loads(res_data3)
                                except Exception as e:
                                    print(e)
                                    return JsonResponse({"INFO": e}, status=status.HTTP_400_BAD_REQUEST)
                                try:
                                    room_resp2 = IRRoomInfo.objects.filter(UserNumber=serializer.data['phone']).values()
                                    info_serialised2 = IRRoomInfoListSerializer(room_resp2, many=True)
                                    ir_data = info_serialised2.data
                                    ir_data = json.dumps(ir_data)
                                    ir_data = str(ir_data).replace('\\', '').replace('"room_data": "', '"room_data": ').replace('"}]}]}"}]', '"}]}]}}]').replace('"}]}]}",', '"}]}]},')
                                    ir_data = '{"rooms": ' + ir_data + ' }'
                                    ir_data = json.loads(ir_data)
                                except Exception as e:
                                    print(e)
                                    ir_data = None
                                if parent_rec.Room_Permission == 'null':
                                    try2 = 'False'
                                else:
                                    try2 = 'true'
                                if parent_rec.Rgb_Permission == 'null':
                                    try3 = 'False'
                                else:
                                    try3 = 'true'
                                return JsonResponse({"rooms_info_available": try2, "rgb_rooms_info_available": try3, "IP": settings.IP, "PORT": settings.IP_PORT, "Field": parent_rec.Unknownfield, "key1": parent_rec.Key1, "key2": parent_rec.Key2, "Apnd": settings.ENCRPT, "scheduling": settings.MQTT_SCHEDULING, "grouping": settings.MQTT_GROUPING, "skd": settings.SKD, "time": settings.TIME, "all_on": settings.ALL_ON, "all_off": settings.ALL_OFF, "timer": settings.MQTT_TIMER, "is_parent": parent_rec.Is_parent, "room_permissions": parent_rec.Room_Permission, "rgb_room_permissions": parent_rec.Rgb_Permission, "user_info": {"name": parent_rec.Username, "number": parent_rec.Usernumber, "email": parent_rec.Useremail, "prfimg": parent_rec.ProfileImg, "backimg": parent_rec.BacgroundImg}, "rooms_info": res_data3, "Remote": ir_data}, status=status.HTTP_200_OK)
                    else:
                        return JsonResponse({"INFO": "Please Contact Administration for Account activation."}, status=status.HTTP_200_OK)
                else:
                    return JsonResponse({"INFO": "No User exists with this Phone Number."}, status=status.HTTP_400_BAD_REQUEST)
            else:
                return JsonResponse({"INFO": "Please check the Auth-Key provided."}, status=status.HTTP_400_BAD_REQUEST)


class DCodeUpdate(APIView):
    permission_classes = [AllowAny]
    authentication_classes = (CsrfExemptSessionAuthentication, BasicAuthentication)

    # noinspection PyMethodMayBeStatic
    def post(self, request):
        serializer = CodeUpdateSerializer(data=request.data, context={'request': request})
        if not serializer.is_valid():
            data = {"INFO": serializer.errors}
            return JsonResponse(data, status=status.HTTP_400_BAD_REQUEST)
        else:
            # noinspection PyBroadException
            try:
                dealer_rec = DealerDevice.objects.filter(DeviceName=serializer.data['GCode'])
                if len(dealer_rec) < 1:
                    return JsonResponse({"INFO": "UnAuthorized Access."}, status=status.HTTP_400_BAD_REQUEST)
            except Exception as e:
                return JsonResponse({"INFO": "Not Authorized To This Device."}, status=status.HTTP_400_BAD_REQUEST)
            # noinspection PyBroadException
            try:
                device_records = Device.objects.filter(Devicecompanyname=serializer.data['GCode'])
                device_records_rgb = RGB.objects.filter(RGB_Devicecompanyname=serializer.data['GCode'])
                device_records_ir = IRDevice.objects.filter(DeviceCompanyName=serializer.data['GCode'])
                if len(device_records) > 0:
                    check = device_records[0]
                    device_mac = check.Devicename
                    action = serializer.data['URL']
                    lalith = device_records[0].Parentid + '/' + device_mac + settings.ENCRPT + '/Update'
                    client = mqtt.Client()
                    parent_records = Userdata.objects.filter(Usernumber=check.Parentid)
                    client.username_pw_set(parent_records[0].Key1, password=parent_records[0].Key2)
                    client.connect(settings.IP)
                    client.publish(lalith, action)
                    return JsonResponse({"INFO": "Update Sent"}, status=status.HTTP_200_OK)
                elif len(device_records_rgb) > 0:
                    check = device_records_rgb[0]
                    device_mac = check.RGB_Devicename
                    action = serializer.data['URL']
                    lalith = device_records_rgb[0].RGB_Parentid + '/' + device_mac + settings.ENCRPT + '/Update'
                    client = mqtt.Client()
                    parent_records = Userdata.objects.filter(Usernumber=check.RGB_Parentid)
                    client.username_pw_set(parent_records[0].Key1, password=parent_records[0].Key2)
                    client.connect(settings.IP)
                    client.publish(lalith, action)
                    return JsonResponse({"INFO": "Update Sent"}, status=status.HTTP_200_OK)
                elif len(device_records_ir) > 0:
                    check = device_records_ir[0]
                    device_mac = check.DeviceName
                    action = serializer.data['URL']
                    lalith = device_records_ir[0].ParentId + '/' + device_mac + settings.ENCRPT + '/Update'
                    client = mqtt.Client()
                    parent_records = Userdata.objects.filter(Usernumber=check.ParentId)
                    client.username_pw_set(parent_records[0].Key1, password=parent_records[0].Key2)
                    client.connect(settings.IP)
                    client.publish(lalith, action)
                    return JsonResponse({"INFO": "Update Sent"}, status=status.HTTP_200_OK)
            except Exception as e:
                print(e)
                return JsonResponse({"INFO": "Check"}, status=status.HTTP_200_OK)


class AgainDeviceAdd(APIView):
    permission_classes = [AllowAny]
    authentication_classes = (CsrfExemptSessionAuthentication, BasicAuthentication)

    # noinspection PyMethodMayBeStatic
    def post(self, request):
        serializer = DeviceaddSerializer(data=request.data, context={'request': request})
        if not serializer.is_valid():
            data = {"INFO": serializer.errors}
            return JsonResponse(data, status=status.HTTP_400_BAD_REQUEST)
        else:
            # noinspection PyBroadException
            try:
                device_name = serializer.data['device_name']
                device_company_name = serializer.data['company_name']
                total = int(serializer.data['total'])
                # fan = int(serializer.data['fan'])
                count2 = int(serializer.data['switches'])
                device_type = serializer.data['type']
                letter = ['A', 'B', 'C', "D", 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', "O", 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', "X", 'Y', 'Z']
                mkl = ''
                mkl3 = ''
                mkl4 = ''
                mkl5 = ''
                mkl6 = ''
                mkl7 = ''
                mkl8 = ''
                for lki in range(total):
                    if lki == 0:
                        mkl = '['
                        mkl3 = '['
                        mkl4 = '['
                        mkl5 = '['
                        mkl6 = '['
                        mkl7 = '['
                        mkl8 = '['
                    if lki < count2:
                        mkl = mkl + '"' + str(letter[lki]) + '",'
                    else:
                        mkl = mkl + '"Zz",'
                    if lki < count2:
                        mkl3 = mkl3 + '"Light",'
                    else:
                        mkl3 = mkl3 + '"Fan",'
                    if lki < count2:
                        mkl4 = mkl4 + '"Light",'
                    else:
                        mkl4 = mkl4 + '"Fan",'
                    if lki < count2:
                        mkl7 = mkl7 + '"' + 'off",'
                    else:
                        mkl7 = mkl7 + '"' + 'off",'
                    if lki < count2:
                        mkl5 = mkl5 + '"' + 'off",'
                    else:
                        mkl5 = mkl5 + '"' + 'off",'
                    if lki < count2:
                        mkl6 = mkl6 + '"' + 'S0E1490",'
                    else:
                        mkl6 = mkl6 + '"' + 'S0E1490",'
                    if lki < count2:
                        mkl8 = mkl8 + '"' + 'off",'
                    else:
                        mkl8 = mkl8 + '"' + 'off",'
                    if lki == total-1:
                        mkl = mkl + ']'
                        mkl3 = mkl3 + ']'
                        mkl4 = mkl4 + ']'
                        mkl5 = mkl5 + ']'
                        mkl6 = mkl6 + ']'
                        mkl7 = mkl7 + ']'
                        mkl8 = mkl8 + ']'
                published_data = mkl.replace('",]', '"]')
                namer_data = mkl3.replace('",]', '"]')
                type_data = mkl4.replace('",]', '"]')
                state_data = mkl5.replace('",]', '"]')
                time_data = mkl6.replace('",]', '"]')
                heavy_data = mkl7.replace('",]', '"]')
                active_data = mkl8.replace('",]', '"]')
                parent_id = '919908799084'
                is_active = True
                request_count = 0
                last_requested = datetime.datetime.now()
                device_number = 0
                device_user_name = device_company_name
                image = 'https://gthink-images-website.s3.ap-south-1.amazonaws.com/prof+(1).png'
                table_obj = Device.objects.filter(Devicename=device_name, Devicecompanyname=device_company_name)
                if len(table_obj) > 0:
                    f = Device(Namer=namer_data, Typed=type_data, Deviceusername=device_user_name,
                               Devicename=device_name, Parentid=parent_id, IsActive=is_active,
                               Lastrequested=last_requested, Publisheddata=published_data, Requestcount=request_count,
                               Devicenumber=device_number, Devicecompanyname=device_company_name, Imagepath=image,
                               Notification_State=state_data, Notification_Time=time_data, Heavy_State=heavy_data,
                               type=device_type, Assigned_State=active_data)
                    f.save()
                    return JsonResponse({"INFO": "Device is registered Again."}, status=status.HTTP_200_OK)
                try:
                    f = Device(Namer=namer_data, Typed=type_data, Deviceusername=device_user_name, Devicename=device_name, Parentid=parent_id, IsActive=is_active, Lastrequested=last_requested, Publisheddata=published_data, Requestcount=request_count, Devicenumber=device_number, Devicecompanyname=device_company_name, Imagepath=image, Notification_State=state_data, Notification_Time=time_data, Heavy_State=heavy_data, type=device_type, Assigned_State=active_data)
                    f.save()
                except Exception as e:
                    print(e)
                    return JsonResponse({"INFO": "Check Device Name or Company Name"}, status=status.HTTP_200_OK)
                return JsonResponse({"INFO": "Device Added"}, status=status.HTTP_200_OK)
            except Exception as e:
                print(e)
                return JsonResponse({"INFO": "Check again"}, status=status.HTTP_200_OK)


class DeviceAdd(APIView):
    permission_classes = [AllowAny]
    authentication_classes = (CsrfExemptSessionAuthentication, BasicAuthentication)

    # noinspection PyMethodMayBeStatic
    def post(self, request):
        serializer = DeviceaddSerializer(data=request.data, context={'request': request})
        if not serializer.is_valid():
            data = {"INFO": serializer.errors}
            return JsonResponse(data, status=status.HTTP_400_BAD_REQUEST)
        else:
            # noinspection PyBroadException
            try:
                device_name = serializer.data['device_name']
                device_company_name = serializer.data['company_name']
                total = int(serializer.data['total'])
                # fan = int(serializer.data['fan'])
                count2 = int(serializer.data['switches'])
                device_type = serializer.data['type']
                letter = ['A', 'B', 'C', "D", 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', "O", 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', "X", 'Y', 'Z']
                mkl = ''
                mkl3 = ''
                mkl4 = ''
                mkl5 = ''
                mkl6 = ''
                mkl7 = ''
                mkl8 = ''
                for lki in range(total):
                    if lki == 0:
                        mkl = '['
                        mkl3 = '['
                        mkl4 = '['
                        mkl5 = '['
                        mkl6 = '['
                        mkl7 = '['
                        mkl8 = '['
                    if lki < count2:
                        mkl = mkl + '"' + str(letter[lki]) + '",'
                    else:
                        mkl = mkl + '"Zz",'
                    if lki < count2:
                        mkl3 = mkl3 + '"Light",'
                    else:
                        mkl3 = mkl3 + '"Fan",'
                    if lki < count2:
                        mkl4 = mkl4 + '"Light",'
                    else:
                        mkl4 = mkl4 + '"Fan",'
                    if lki < count2:
                        mkl7 = mkl7 + '"' + 'off",'
                    else:
                        mkl7 = mkl7 + '"' + 'off",'
                    if lki < count2:
                        mkl5 = mkl5 + '"' + 'off",'
                    else:
                        mkl5 = mkl5 + '"' + 'off",'
                    if lki < count2:
                        mkl6 = mkl6 + '"' + 'S0E1490",'
                    else:
                        mkl6 = mkl6 + '"' + 'S0E1490",'
                    if lki < count2:
                        mkl8 = mkl8 + '"' + 'off",'
                    else:
                        mkl8 = mkl8 + '"' + 'off",'
                    if lki == total-1:
                        mkl = mkl + ']'
                        mkl3 = mkl3 + ']'
                        mkl4 = mkl4 + ']'
                        mkl5 = mkl5 + ']'
                        mkl6 = mkl6 + ']'
                        mkl7 = mkl7 + ']'
                        mkl8 = mkl8 + ']'
                published_data = mkl.replace('",]', '"]')
                namer_data = mkl3.replace('",]', '"]')
                type_data = mkl4.replace('",]', '"]')
                state_data = mkl5.replace('",]', '"]')
                time_data = mkl6.replace('",]', '"]')
                heavy_data = mkl7.replace('",]', '"]')
                active_data = mkl8.replace('",]', '"]')
                parent_id = '919908799084'
                is_active = True
                request_count = 0
                last_requested = datetime.datetime.now()
                device_number = 0
                device_user_name = device_company_name
                image = 'https://gthink-images-website.s3.ap-south-1.amazonaws.com/prof+(1).png'
                table_obj = Device.objects.filter(Devicename=device_name, Devicecompanyname=device_company_name)
                if len(table_obj) > 0:
                    return JsonResponse({"INFO": "Device is registered with this ID or Company Name."}, status=status.HTTP_200_OK)
                try:
                    f = Device(Namer=namer_data, Typed=type_data, Deviceusername=device_user_name, Devicename=device_name, Parentid=parent_id, IsActive=is_active, Lastrequested=last_requested, Publisheddata=published_data, Requestcount=request_count, Devicenumber=device_number, Devicecompanyname=device_company_name, Imagepath=image, Notification_State=state_data, Notification_Time=time_data, Heavy_State=heavy_data, type=device_type, Assigned_State=active_data)
                    f.save()
                except Exception as e:
                    print(e)
                    return JsonResponse({"INFO": "Check Device Name or Company Name"}, status=status.HTTP_200_OK)
                return JsonResponse({"INFO": "Device Added"}, status=status.HTTP_200_OK)
            except Exception as e:
                print(e)
                return JsonResponse({"INFO": "Check again"}, status=status.HTTP_200_OK)

#
# class DeviceAddFan(APIView):
#     permission_classes = [AllowAny]
#     authentication_classes = (CsrfExemptSessionAuthentication, BasicAuthentication)
#
#     # noinspection PyMethodMayBeStatic
#     def post(self, request):
#         serializer = DeviceAddFanSerializer(data=request.data, context={'request': request})
#         if not serializer.is_valid():
#             data = {"INFO": serializer.errors}
#             return JsonResponse(data, status=status.HTTP_400_BAD_REQUEST)
#         else:
#             # noinspection PyBroadException
#             try:
#                 device_name = serializer.data['device_name']
#                 device_company_name = serializer.data['company_name']
#                 total = int(serializer.data['total'])
#                 # fan = int(serializer.data['fan'])
#                 # count2 = int(serializer.data['switches'])
#                 device_type = serializer.data['type']
#                 published_data = ''
#                 namer_data = ''
#                 type_data = ''
#                 state_data = ''
#                 time_data = ''
#                 heavy_data = ''
#                 active_data = ''
#                 if total == 5:
#                     published_data = '["Zz","B","C","D","E"]'
#                     namer_data = '["Fan","Light","Light","Light","Light"]'
#                     type_data = '["Fan","Light","Light","Light","Light"]'
#                     state_data = '["off","off","off","off","off"]'
#                     time_data = '["S0E1490","S0E1490","S0E1490","S0E1490","S0E1490"]'
#                     heavy_data = '["off","off","off","off","off"]'
#                     active_data = '["off","off","off","off","off"]'
#                 if total == 7:
#                     published_data = '["Zz","B","C","D","E","F","G"]'
#                     namer_data = '["Fan","Light","Light","Light","Light","Light","Light"]'
#                     type_data = '["Fan","Light","Light","Light","Light","Light","Light"]'
#                     state_data = '["off","off","off","off","off","off","off"]'
#                     time_data = '["S0E1490","S0E1490","S0E1490","S0E1490","S0E1490","S0E1490","S0E1490"]'
#                     heavy_data = '["off","off","off","off","off","off","off"]'
#                     active_data = '["off","off","off","off","off","off","off"]'
#                 if total == 8:
#                     published_data = '["A","B","C","D","E","F","G","H"]'
#                     namer_data = '["Light","Light","Light","Light","Light","Light","Light","Light"]'
#                     type_data = '["Light","Light","Light","Light","Light","Light","Light","Light"]'
#                     state_data = '["off","off","off","off","off","off","off","off"]'
#                     time_data = '["S0E1490","S0E1490","S0E1490","S0E1490","S0E1490","S0E1490","S0E1490","S0E1490"]'
#                     heavy_data = '["off","off","off","off","off","off","off","off"]'
#                     active_data = '["off","off","off","off","off","off","off","off"]'
#                 if total == 6:
#                     published_data = '["A","B","C","D","E","F"]'
#                     namer_data = '["Light","Light","Light","Light","Light","Light"]'
#                     type_data = '["Light","Light","Light","Light","Light","Light"]'
#                     state_data = '["off","off","off","off","off","off"]'
#                     time_data = '["S0E1490","S0E1490","S0E1490","S0E1490","S0E1490","S0E1490"]'
#                     heavy_data = '["off","off","off","off","off","off"]'
#                     active_data = '["off","off","off","off","off","off"]'
#                 if total == 4:
#                     published_data = '["A","B","C","D"]'
#                     namer_data = '["Light","Light","Light","Light"]'
#                     type_data = '["Light","Light","Light","Light"]'
#                     state_data = '["off","off","off","off"]'
#                     time_data = '["S0E1490","S0E1490","S0E1490","S0E1490"]'
#                     heavy_data = '["off","off","off","off"]'
#                     active_data = '["off","off","off","off"]'
#                 if total == 2:
#                     published_data = '["A","B"]'
#                     namer_data = '["Light","Light"]'
#                     type_data = '["Light","Light"]'
#                     state_data = '["off","off"]'
#                     time_data = '["S0E1490","S0E1490"]'
#                     heavy_data = '["off","off"]'
#                     active_data = '["off","off"]'
#                 if total == 1:
#                     published_data = '["A"]'
#                     namer_data = '["Curtain"]'
#                     type_data = '["Curtain"]'
#                     state_data = '["off"]'
#                     time_data = '["S0E1490"]'
#                     heavy_data = '["off"]'
#                     active_data = '["off"]'
#                 parent_id = '919908799084'
#                 is_active = True
#                 request_count = 0
#                 last_requested = datetime.datetime.now()
#                 device_number = 0
#                 device_user_name = device_company_name
#                 image = 'https://gthink-images-website.s3.ap-south-1.amazonaws.com/prof+(1).png'
#                 table_obj = Device.objects.filter(Devicename=device_name, Devicecompanyname=device_company_name)
#                 if len(table_obj) > 0:
#                     f = Device(Namer=namer_data, Typed=type_data, Deviceusername=device_user_name, Devicename=device_name, Parentid=parent_id, IsActive=is_active, Lastrequested=last_requested, Publisheddata=published_data, Requestcount=request_count, Devicenumber=device_number, Devicecompanyname=device_company_name, Imagepath=image, Notification_State=state_data, Notification_Time=time_data, Heavy_State=heavy_data, type=device_type, Assigned_State=active_data)
#                     f.save()
#                     return JsonResponse({"INFO": "Device is registered Again."}, status=status.HTTP_200_OK)
#                 try:
#                     f = Device(Namer=namer_data, Typed=type_data, Deviceusername=device_user_name, Devicename=device_name, Parentid=parent_id, IsActive=is_active, Lastrequested=last_requested, Publisheddata=published_data, Requestcount=request_count, Devicenumber=device_number, Devicecompanyname=device_company_name, Imagepath=image, Notification_State=state_data, Notification_Time=time_data, Heavy_State=heavy_data, type=device_type, Assigned_State=active_data)
#                     f.save()
#                 except Exception as e:
#                     print(e)
#                     return JsonResponse({"INFO": "Check Device Name or Company Name"}, status=status.HTTP_200_OK)
#                 return JsonResponse({"INFO": "Device Added"}, status=status.HTTP_200_OK)
#             except Exception as e:
#                 print(e)
#                 return JsonResponse({"INFO": "Check again"}, status=status.HTTP_200_OK)
#

class OldDeviceAddFan(APIView):
    permission_classes = [AllowAny]
    authentication_classes = (CsrfExemptSessionAuthentication, BasicAuthentication)

    # noinspection PyMethodMayBeStatic
    def post(self, request):
        serializer = OldDeviceAddFanSerializer(data=request.data, context={'request': request})
        if not serializer.is_valid():
            data = {"INFO": serializer.errors}
            return JsonResponse(data, status=status.HTTP_400_BAD_REQUEST)
        else:
            # noinspection PyBroadException
            try:
                device_name = serializer.data['device_name']
                device_company_name = serializer.data['company_name']
                total = int(serializer.data['total'])
                # fan = int(serializer.data['fan'])
                # count2 = int(serializer.data['switches'])
                device_type = serializer.data['type']
                published_data = ''
                namer_data = ''
                type_data = ''
                state_data = ''
                time_data = ''
                heavy_data = ''
                active_data = ''
                if total == 5:
                    published_data = '["Zz","B","C","D","E"]'
                    namer_data = '["Fan","Light","Light","Light","Light"]'
                    type_data = '["Fan","Light","Light","Light","Light"]'
                    state_data = '["off","off","off","off","off"]'
                    time_data = '["S0E1490","S0E1490","S0E1490","S0E1490","S0E1490"]'
                    heavy_data = '["off","off","off","off","off"]'
                    active_data = '["off","off","off","off","off"]'
                if total == 7:
                    published_data = '["Zz","B","C","D","E","F","G"]'
                    namer_data = '["Fan","Light","Light","Light","Light","Light","Light"]'
                    type_data = '["Fan","Light","Light","Light","Light","Light","Light"]'
                    state_data = '["off","off","off","off","off","off","off"]'
                    time_data = '["S0E1490","S0E1490","S0E1490","S0E1490","S0E1490","S0E1490","S0E1490"]'
                    heavy_data = '["off","off","off","off","off","off","off"]'
                    active_data = '["off","off","off","off","off","off","off"]'
                if total == 8:
                    published_data = '["A","B","C","D","E","F","G","H"]'
                    namer_data = '["Light","Light","Light","Light","Light","Light","Light","Light"]'
                    type_data = '["Light","Light","Light","Light","Light","Light","Light","Light"]'
                    state_data = '["off","off","off","off","off","off","off","off"]'
                    time_data = '["S0E1490","S0E1490","S0E1490","S0E1490","S0E1490","S0E1490","S0E1490","S0E1490"]'
                    heavy_data = '["off","off","off","off","off","off","off","off"]'
                    active_data = '["off","off","off","off","off","off","off","off"]'
                if total == 6:
                    published_data = '["A","B","C","D","E","F"]'
                    namer_data = '["Light","Light","Light","Light","Light","Light"]'
                    type_data = '["Light","Light","Light","Light","Light","Light"]'
                    state_data = '["off","off","off","off","off","off"]'
                    time_data = '["S0E1490","S0E1490","S0E1490","S0E1490","S0E1490","S0E1490"]'
                    heavy_data = '["off","off","off","off","off","off"]'
                    active_data = '["off","off","off","off","off","off"]'
                if total == 4:
                    published_data = '["A","B","C","D"]'
                    namer_data = '["Light","Light","Light","Light"]'
                    type_data = '["Light","Light","Light","Light"]'
                    state_data = '["off","off","off","off"]'
                    time_data = '["S0E1490","S0E1490","S0E1490","S0E1490"]'
                    heavy_data = '["off","off","off","off"]'
                    active_data = '["off","off","off","off"]'
                if total == 2:
                    published_data = '["A","B"]'
                    namer_data = '["Light","Light"]'
                    type_data = '["Light","Light"]'
                    state_data = '["off","off"]'
                    time_data = '["S0E1490","S0E1490"]'
                    heavy_data = '["off","off"]'
                    active_data = '["off","off"]'
                if total == 1:
                    published_data = '["A"]'
                    namer_data = '["Curtain"]'
                    type_data = '["Curtain"]'
                    state_data = '["off"]'
                    time_data = '["S0E1490"]'
                    heavy_data = '["off"]'
                    active_data = '["off"]'
                parent_id = '919908799084'
                is_active = True
                request_count = 0
                last_requested = datetime.datetime.now()
                device_number = 0
                device_user_name = device_company_name
                image = 'https://gthink-images-website.s3.ap-south-1.amazonaws.com/prof+(1).png'
                table_obj = Device.objects.filter(Devicename=device_name, Devicecompanyname=device_company_name)
                if len(table_obj) > 0:
                    device_rec = Device.objects.get(Devicename=device_name)
                    device_rec.delete()
                    #  return JsonResponse({"INFO": "Device is registered with this ID or Company Name."}, status=status.HTTP_200_OK)
                try:
                    f = Device(Namer=namer_data, Typed=type_data, Deviceusername=device_user_name, Devicename=device_name, Parentid=parent_id, IsActive=is_active, Lastrequested=last_requested, Publisheddata=published_data, Requestcount=request_count, Devicenumber=device_number, Devicecompanyname=device_company_name, Imagepath=image, Notification_State=state_data, Notification_Time=time_data, Heavy_State=heavy_data, type=device_type, Assigned_State=active_data)
                    f.save()
                except Exception as e:
                    print(e)
                    return JsonResponse({"INFO": "Check Device Name or Company Name"}, status=status.HTTP_200_OK)
                return JsonResponse({"INFO": "Device Added"}, status=status.HTTP_200_OK)
            except Exception as e:
                print(e)
                return JsonResponse({"INFO": "Check again"}, status=status.HTTP_200_OK)


class ODeviceAddFan(APIView):
    permission_classes = [AllowAny]
    authentication_classes = (CsrfExemptSessionAuthentication, BasicAuthentication)

    # noinspection PyMethodMayBeStatic
    def post(self, request):
        serializer = OldDeviceAddFanSerializer(data=request.data, context={'request': request})
        if not serializer.is_valid():
            data = {"INFO": serializer.errors}
            return JsonResponse(data, status=status.HTTP_400_BAD_REQUEST)
        else:
            # noinspection PyBroadException
            try:
                device_name = serializer.data['device_name']
                device_company_name = serializer.data['company_name']
                total = int(serializer.data['total'])
                device_type = serializer.data['type']
                published_data = ''
                namer_data = ''
                type_data = ''
                state_data = ''
                time_data = ''
                heavy_data = ''
                active_data = ''
                device_state = ''
                if total == 5:
                    published_data = '["F1","T1","T2","T3","T4"]'
                    namer_data = '["Fan","Light","Light","Light","Light"]'
                    type_data = '["Fan","Light","Light","Light","Light"]'
                    state_data = '["off","off","off","off","off"]'
                    time_data = '["S0E1490","S0E1490","S0E1490","S0E1490","S0E1490"]'
                    heavy_data = '["off","off","off","off","off"]'
                    active_data = '["off","off","off","off","off"]'
                    device_state = '["0","0","0","0","0"]'
                if total == 7:
                    published_data = '["F1","T1","T2","T3","T4","T5","T6"]'
                    namer_data = '["Fan","Light","Light","Light","Light","Light","Light"]'
                    type_data = '["Fan","Light","Light","Light","Light","Light","Light"]'
                    state_data = '["off","off","off","off","off","off","off"]'
                    time_data = '["S0E1490","S0E1490","S0E1490","S0E1490","S0E1490","S0E1490","S0E1490"]'
                    heavy_data = '["off","off","off","off","off","off","off"]'
                    active_data = '["off","off","off","off","off","off","off"]'
                    device_state = '["0","0","0","0","0","0","0"]'
                if total == 8:
                    published_data = '["T1","T2","T3","T4","T5","T6","T7","T8"]'
                    namer_data = '["Light","Light","Light","Light","Light","Light","Light","Light"]'
                    type_data = '["Light","Light","Light","Light","Light","Light","Light","Light"]'
                    state_data = '["off","off","off","off","off","off","off","off"]'
                    time_data = '["S0E1490","S0E1490","S0E1490","S0E1490","S0E1490","S0E1490","S0E1490","S0E1490"]'
                    heavy_data = '["off","off","off","off","off","off","off","off"]'
                    active_data = '["off","off","off","off","off","off","off","off"]'
                    device_state = '["0","0","0","0","0","0","0","0"]'
                if total == 6:
                    published_data = '["T1","T2","T3","T4","T5","T6"]'
                    namer_data = '["Light","Light","Light","Light","Light","Light"]'
                    type_data = '["Light","Light","Light","Light","Light","Light"]'
                    state_data = '["off","off","off","off","off","off"]'
                    time_data = '["S0E1490","S0E1490","S0E1490","S0E1490","S0E1490","S0E1490"]'
                    heavy_data = '["off","off","off","off","off","off"]'
                    active_data = '["off","off","off","off","off","off"]'
                    device_state = '["0","0","0","0","0","0"]'
                if total == 4:
                    published_data = '["T1","T2","T3","T4"]'
                    namer_data = '["Light","Light","Light","Light"]'
                    type_data = '["Light","Light","Light","Light"]'
                    state_data = '["off","off","off","off"]'
                    time_data = '["S0E1490","S0E1490","S0E1490","S0E1490"]'
                    heavy_data = '["off","off","off","off"]'
                    active_data = '["off","off","off","off"]'
                    device_state = '["0","0","0","0"]'
                if total == 3:
                    published_data = '["T1","T2","T3"]'
                    namer_data = '["Light","Light","Light"]'
                    type_data = '["Light","Light","Light"]'
                    state_data = '["off","off","off"]'
                    time_data = '["S0E1490","S0E1490","S0E1490"]'
                    heavy_data = '["off","off","off"]'
                    active_data = '["off","off","off"]'
                    device_state = '["0","0","0"]'
                if total == 2:
                    published_data = '["T1","T2"]'
                    namer_data = '["Light","Light"]'
                    type_data = '["Light","Light"]'
                    state_data = '["off","off"]'
                    time_data = '["S0E1490","S0E1490"]'
                    heavy_data = '["off","off"]'
                    active_data = '["off","off"]'
                    device_state = '["0","0"]'
                if total == 1:
                    published_data = '["A"]'
                    namer_data = '["Curtain"]'
                    type_data = '["Curtain"]'
                    state_data = '["off"]'
                    time_data = '["S0E1490"]'
                    heavy_data = '["off"]'
                    active_data = '["off"]'
                    device_state = '["0"]'
                parent_id = '919908799084'
                is_active = True
                request_count = 0
                last_requested = datetime.datetime.now()
                device_number = 0
                device_user_name = device_company_name
                image = 'https://gthink-images-website.s3.ap-south-1.amazonaws.com/prof+(1).png'
                table_obj = Device.objects.filter(Devicename=device_name, Devicecompanyname=device_company_name)
                if len(table_obj) > 0:
                    device_rec = Device.objects.get(Devicename=device_name)
                    device_rec.delete()
                    #  return JsonResponse({"INFO": "Device is registered with this ID or Company Name."}, status=status.HTTP_200_OK)
                try:
                    f = Device(Namer=namer_data, Typed=type_data, Deviceusername=device_user_name, Devicename=device_name, Parentid=parent_id, IsActive=is_active, Lastrequested=last_requested, Publisheddata=published_data, Requestcount=request_count, Devicenumber=device_number, Devicecompanyname=device_company_name, Imagepath=image, Notification_State=state_data, Notification_Time=time_data, Heavy_State=heavy_data, type=device_type, Assigned_State=active_data, Device_State=device_state)
                    f.save()
                except Exception as e:
                    print(e)
                    return JsonResponse({"INFO": "Check Device Name or Company Name"}, status=status.HTTP_200_OK)
                return JsonResponse({"INFO": "Device Added"}, status=status.HTTP_200_OK)
            except Exception as e:
                print(e)
                return JsonResponse({"INFO": "Check again"}, status=status.HTTP_200_OK)


class Code(APIView):
    permission_classes = [AllowAny]
    authentication_classes = (CsrfExemptSessionAuthentication, BasicAuthentication)

    # noinspection PyMethodMayBeStatic
    def get(self, request, device_id):
        serializer = DeviceSerializer(data={'device_id': device_id}, context={'request': request})
        if not(serializer.is_valid()):
            data = {"error": "invalid_request", "error_description": serializer.errors}
            return JsonResponse(data, status=status.HTTP_400_BAD_REQUEST)
        else:
            device_records = Device.objects.filter(Devicename=serializer.data['device_id'])
            if len(device_records) > 0:
                return JsonResponse({"INFO": "Device is registered with this Name."}, status=status.HTTP_200_OK)
            else:
                device_name = serializer.data['device_id']
                parent_id = '918008182410'
                is_active = False
                request_count = 0
                try:
                    f = Device(Devicename=device_name, Parentid=parent_id, IsActive=is_active,  Requestcount=request_count)
                    f.save()
                except Exception as e:
                    print(e)
                    return JsonResponse({"INFO": "Check Device Name or Company Name"}, status=status.HTTP_200_OK)
                return JsonResponse({"INFO": "Device Added"}, status=status.HTTP_200_OK)


class DeviceAddFirst(APIView):
    permission_classes = [AllowAny]
    authentication_classes = (CsrfExemptSessionAuthentication, BasicAuthentication)

    # noinspection PyMethodMayBeStatic
    def post(self, request):
        serializer = DeviceaddfirstSerializer(data=request.data, context={'request': request})
        if not serializer.is_valid():
            data = {"INFO": serializer.errors}
            return JsonResponse(data, status=status.HTTP_400_BAD_REQUEST)
        else:
            try:
                device_name = serializer.data['device_name']
                parent_id = '918008182410'
                is_active = True
                request_count = 0
                try:
                    f = Device(Devicename=device_name, Parentid=parent_id, IsActive=is_active,  Requestcount=request_count)
                    f.save()
                except Exception as e:
                    print(e)
                    return JsonResponse({"INFO": "Check Device Name or Company Name"}, status=status.HTTP_200_OK)
                return JsonResponse({"INFO": "Device Added"}, status=status.HTTP_200_OK)
            except Exception as e:
                print(e)
                return JsonResponse({"INFO": "Check again"}, status=status.HTTP_200_OK)


class RoomsInfo(APIView):
    permission_classes = [AllowAny]
    authentication_classes = (CsrfExemptSessionAuthentication, BasicAuthentication)

    # noinspection PyMethodMayBeStatic
    def post(self, request):
        serializer = RoomsInfoSerializer(data=request.data, context={'request': request})
        if not serializer.is_valid():
            data = {"INFO": serializer.errors}
            return JsonResponse(data, status=status.HTTP_400_BAD_REQUEST)
        else:
            if serializer.data['auth_key'] == settings.AUTH_KEY:
                try:
                    parent_rec = Userdata.objects.get(Usernumber=serializer.data['phone'])
                    print(parent_rec)
                    parent_exists = True
                except Exception as e:
                    print(e)
                    parent_exists = False
                try:
                    parent_rec2 = Userdata.objects.get(Usernumber=serializer.data['phone'])
                    print(parent_rec2)
                    parent_exists2 = True
                except Exception as e:
                    print(e)
                    parent_exists2 = False
                if parent_exists is True or parent_exists2 is True:
                    parent_rec = Userdata.objects.get(Usernumber=serializer.data['phone'])
                    if parent_rec.Is_action is True:
                        if parent_rec.Response is None:
                            try:
                                if parent_rec.Is_parent is True:
                                    parent_resp_id = parent_rec.Usernumber
                                else:
                                    parent_resp_id = parent_rec.Createdby
                                room_resp = Device.objects.filter(Parentid=parent_resp_id).values()
                                room_resp2 = Curtain.objects.filter(Parentid=parent_resp_id).values()
                                child_recs_serialised = RoomSerializer(room_resp, many=True)
                                data_set = '{"rooms":['
                                for length in range(child_recs_serialised.data.__len__()):
                                    tdata = child_recs_serialised.data[length]
                                    pubdata = json.loads(tdata['Publisheddata'])
                                    namea = json.loads(tdata['Namer'])
                                    ir = tdata['Work']
                                    dname = tdata['Devicename']
                                    if serializer.data['phone'] == '919908799084':
                                        duname = tdata['Devicecompanyname']
                                    else:
                                        duname = tdata['Deviceusername']
                                    imagep = tdata['Imagepath']
                                    tdata = json.loads(tdata['Typed'])
                                    data_set = str(data_set) + '{"roomid":"' + str(dname) + '","roomImg":"' + str(imagep) + '","name":"' + str(duname) + '","roomd":[{"pub":"' + str(parent_resp_id) + '/' + str(dname) + 'G/Device","sub":"' + str(parent_resp_id)+'/' + str(dname) + 'G/App","namer":'+str(len(pubdata))+',"device":['
                                    for ll in range(len(pubdata)):
                                        data_set = str(data_set) + '{"type":"' + str(tdata[ll]) + '","name":"' + str(namea[ll]) + '","action":"' + str(pubdata[ll]) + '","irdata":"' + str(ir) + '","pub":"' + str(parent_resp_id) + '/' + str(dname) + 'G/Device/' + str(pubdata[ll]) + '","sub":"' + str(parent_resp_id)+'/' + str(dname) + 'G/App/' + str(pubdata[ll]) + '","index":"' + str(ll) + '"}'
                                        if ll != len(pubdata)-1:
                                            data_set += ','
                                    data_set += ']}]}'
                                    if length != child_recs_serialised.data.__len__()-1:
                                        data_set += ','
                                data_set += '],"Curtain":['
                                child_recs_serialised2 = CurtainRoomSerializer(room_resp2, many=True)
                                for length in range(child_recs_serialised2.data.__len__()):
                                    tdata = child_recs_serialised2.data[length]
                                    pubdata = json.loads(tdata['Publisheddata'])
                                    dname = tdata['Devicename']
                                    duname = tdata['Deviceusername']
                                    imagep = tdata['Imagepath']
                                    tdata = json.loads(tdata['Typed'])
                                    data_set = str(data_set) + '{"roomid":"' + str(dname) + '","roomImg":"' + str(imagep) + '","name":"' + str(duname) + '","roomd":[{"device":['
                                    for ll in range(len(pubdata)):
                                        data_set = str(data_set) + '{"type":"' + str(tdata[ll]) + '","action":"' + str(pubdata[ll]) + '","pub":"' + str(parent_resp_id) + '/' + str(dname) + 'G/Device/' + str(pubdata[ll]) + '","sub":"' + str(parent_resp_id)+'/' + str(dname) + 'G/App/' + str(pubdata[ll]) + '"}'
                                        if ll != len(pubdata)-1:
                                            data_set += ','
                                    data_set += ']}]}'
                                    if length != child_recs_serialised2.data.__len__()-1:
                                        data_set += ','
                                data_set += ']}'
                                data_set = json.loads(data_set)
                            except Exception as e:
                                print(e)
                                return JsonResponse({"INFO": e}, status=status.HTTP_400_BAD_REQUEST)
                            return JsonResponse({"rooms_info_available": True, "IP": settings.IP, "PORT": settings.IP_PORT, "key1": parent_rec.Key1, "key2": parent_rec.Key2, "Apnd": settings.ENCRPT, "scheduling": settings.MQTT_SCHEDULING, "grouping": settings.MQTT_GROUPING, "skd": settings.SKD, "time": settings.TIME, "all_on": settings.ALL_ON, "all_off": settings.ALL_OFF, "timer": settings.MQTT_TIMER, "is_parent": parent_rec.Is_parent, "room_permissions": parent_rec.Room_Permission, "user_info": {"name": parent_rec.Username, "number": parent_rec.Usernumber, "email": parent_rec.Useremail, "prfimg": parent_rec.ProfileImg, "backimg": parent_rec.BacgroundImg}, "rooms_info": data_set}, status=status.HTTP_200_OK)
                        else:
                            if parent_rec.Is_parent is True:
                                try:
                                    room_resp = UserRoomInfo.objects.filter(UserNumber=serializer.data['phone']).values()
                                    child_recs_serialised = UserRoomInfoListSerializer(room_resp, many=True)
                                    res_data = child_recs_serialised.data
                                    res_data = json.dumps(res_data)
                                    res_data2 = str(res_data).replace('\\', '').replace('"roomd": "', '"roomd": [').replace('"}]}"}, {', '"}]}]}, {').replace('}]}"}]', '}]}]}]')
                                    res_data3 = '{"rooms":' + res_data2 + '}'
                                    res_data3 = json.loads(res_data3)
                                except Exception as e:
                                    print(e)
                                    return JsonResponse({"INFO": e}, status=status.HTTP_400_BAD_REQUEST)
                                try:
                                    room_resp2 = IRRoomInfo.objects.filter(UserNumber=serializer.data['phone']).values()
                                    info_serialised2 = IRRoomInfoListSerializer(room_resp2, many=True)
                                    ir_data = info_serialised2.data
                                    ir_data = json.dumps(ir_data)
                                    ir_data = str(ir_data).replace('\\', '').replace('"room_data": "', '"room_data": ').replace('"}]}]}"}]', '"}]}]}}]').replace('"}]}]}",', '"}]}]},')
                                    ir_data = '{"rooms": ' + ir_data + ' }'
                                    ir_data = json.loads(ir_data)
                                except Exception as e:
                                    print(e)
                                    ir_data = None
                                return JsonResponse({"rooms_info_available": True, "IP": settings.IP, "PORT": settings.IP_PORT, "Field": parent_rec.Unknownfield, "key1": parent_rec.Key1, "key2": parent_rec.Key2, "Apnd": settings.ENCRPT, "scheduling": settings.MQTT_SCHEDULING, "grouping": settings.MQTT_GROUPING, "skd": settings.SKD, "time": settings.TIME, "all_on": settings.ALL_ON, "all_off": settings.ALL_OFF, "timer": settings.MQTT_TIMER, "is_parent": parent_rec.Is_parent, "room_permissions": parent_rec.Room_Permission, "user_info": {"name": parent_rec.Username, "number": parent_rec.Usernumber, "email": parent_rec.Useremail, "prfimg": parent_rec.ProfileImg, "backimg": parent_rec.BacgroundImg}, "rooms_info": res_data3, "Remote": ir_data}, status=status.HTTP_200_OK)
                    else:
                        return JsonResponse({"INFO": "Please Contact Administration for Account activation."}, status=status.HTTP_200_OK)
                else:
                    return JsonResponse({"INFO": "No User exists with this Phone Number."}, status=status.HTTP_400_BAD_REQUEST)
            else:
                return JsonResponse({"INFO": "Please check the Auth-Key provided."}, status=status.HTTP_400_BAD_REQUEST)


class IRRoomsInfo(APIView):
    permission_classes = [AllowAny]
    authentication_classes = (CsrfExemptSessionAuthentication, BasicAuthentication)

    # noinspection PyMethodMayBeStatic
    def post(self, request):
        serializer = RoomsInfoSerializer(data=request.data, context={'request': request})
        if not serializer.is_valid():
            data = {"INFO": serializer.errors}
            return JsonResponse(data, status=status.HTTP_400_BAD_REQUEST)
        else:
            if serializer.data['auth_key'] == settings.AUTH_KEY:
                try:
                    parent_recognition = Userdata.objects.get(Usernumber=serializer.data['phone'])
                    print(parent_recognition)
                    account_exists = True
                except Exception as e:
                    print(e)
                    account_exists = False
                if account_exists is True:
                    parent_rec = Userdata.objects.get(Usernumber=serializer.data['phone'])
                    if parent_rec.Is_action is True:
                        if parent_rec.Is_parent is True:
                            try:
                                room_resp2 = IRRoomInfo.objects.filter(UserNumber=serializer.data['phone']).values()
                                info_serialised2 = IRRoomInfoListSerializer(room_resp2, many=True)
                                ir_data = info_serialised2.data
                                ir_data = json.dumps(ir_data)
                                ir_data = str(ir_data).replace('\\', '').replace('"room_data": "', '"room_data": ').replace('"}]}]}"}]', '"}]}]}}]').replace('"}]}]}",', '"}]}]},')
                                ir_data = '{"rooms": ' + ir_data + ' }'
                                ir_data = json.loads(ir_data)
                            except Exception as e:
                                print(e)
                                ir_data = None
                            if parent_rec.Room_Permission == 'null':
                                try2 = 'False'
                            else:
                                try2 = 'true'
                            if parent_rec.Rgb_Permission == 'null':
                                try3 = 'False'
                            else:
                                try3 = 'true'
                            return JsonResponse({"rooms_info_available": try2, "rgb_rooms_info_available": try3, "IP": settings.IP, "PORT": settings.IP_PORT, "Field": parent_rec.Unknownfield, "key1": parent_rec.Key1, "key2": parent_rec.Key2, "Apnd": settings.ENCRPT, "scheduling": settings.MQTT_SCHEDULING, "grouping": settings.MQTT_GROUPING, "skd": settings.SKD, "time": settings.TIME, "all_on": settings.ALL_ON, "all_off": settings.ALL_OFF, "timer": settings.MQTT_TIMER, "is_parent": parent_rec.Is_parent, "room_permissions": parent_rec.Room_Permission, "rgb_room_permissions": parent_rec.Rgb_Permission, "user_info": {"name": parent_rec.Username, "number": parent_rec.Usernumber, "email": parent_rec.Useremail, "prfimg": parent_rec.ProfileImg, "backimg": parent_rec.BacgroundImg}, "Remote": ir_data}, status=status.HTTP_200_OK)
                    else:
                        return JsonResponse({"INFO": "Please Contact Administration for Account activation."}, status=status.HTTP_200_OK)
                else:
                    return JsonResponse({"INFO": "No User exists with this Phone Number."}, status=status.HTTP_400_BAD_REQUEST)
            else:
                return JsonResponse({"INFO": "Please check the Auth-Key provided."}, status=status.HTTP_400_BAD_REQUEST)


class NewRoomsInfo(APIView):
    permission_classes = [AllowAny]
    authentication_classes = (CsrfExemptSessionAuthentication, BasicAuthentication)

    # noinspection PyMethodMayBeStatic
    def post(self, request):
        serializer = RoomsInfoSerializer(data=request.data, context={'request': request})
        if not serializer.is_valid():
            data = {"INFO": serializer.errors}
            return JsonResponse(data, status=status.HTTP_400_BAD_REQUEST)
        else:
            if serializer.data['auth_key'] == settings.AUTH_KEY:
                try:
                    parent_recognition = Userdata.objects.get(Usernumber=serializer.data['phone'])
                    print(parent_recognition)
                    account_exists = True
                except Exception as e:
                    print(e)
                    account_exists = False
                if account_exists is True:
                    parent_rec = Userdata.objects.get(Usernumber=serializer.data['phone'])
                    if parent_rec.Is_action is True:
                        if parent_rec.Response is None:
                            try:
                                data_set = '{"rooms":['
                                ir_data = None
                                if parent_rec.Is_parent is True:
                                    parent_resp_id = parent_rec.Usernumber
                                    room_resp = Device.objects.filter(Parentid=parent_resp_id).values()
                                    child_recs_serialised = RoomSerializer(room_resp, many=True)
                                    for length in range(child_recs_serialised.data.__len__()):
                                        tdata = child_recs_serialised.data[length]
                                        # print(tdata)
                                        icondata = json.loads(tdata['Device_Icon'])
                                        pubdata = json.loads(tdata['Publisheddata'])
                                        namea = json.loads(tdata['Namer'])
                                        ir = tdata['Work']
                                        dname = tdata['Devicename']
                                        if serializer.data['phone'] == '919908799084':
                                            duname = tdata['Devicecompanyname']
                                        else:
                                            duname = tdata['Deviceusername']
                                        company_name = tdata['Devicecompanyname']
                                        imagep = tdata['Imagepath']
                                        tdata = json.loads(tdata['Typed'])
                                        data_set = str(data_set) + '{"roomid":"' + str(dname) + '","roomImg":"' + str(imagep) + '","name":"' + str(duname) + '","roomd":[{"namer":'+str(len(pubdata))+',"device":['
                                        for ll in range(len(pubdata)):
                                            data_set = str(data_set) + '{"type":"' + str(tdata[ll]) + '","index":"' + str(ll) + '","assign":"@' + '","Gcode":"' + str(company_name) + '","Company_name":"' + str(dname) + '","name":"' + str(namea[ll]) + '","action":"' + str(pubdata[ll]) + '","irdata":"' + str(ir) + '","pub":"' + str(parent_resp_id) + '/' + str(dname) + 'G/Device/' + str(pubdata[ll]) + '","sub":"' + str(parent_resp_id)+'/' + str(dname) + 'G/App/' + str(pubdata[ll]) + '","icon":"' + str(icondata[ll]) + '"}'
                                            if ll != len(pubdata)-1:
                                                data_set += ','
                                        data_set += ']}]}'
                                        if length != child_recs_serialised.data.__len__()-1:
                                            data_set += ','
                                    data_set += ']}'
                                    data_set = json.loads(data_set)
                                    try:
                                        room_resp2 = IRRoomInfo.objects.filter(UserNumber=serializer.data['phone']).values()
                                        info_serialised2 = IRRoomInfoListSerializer(room_resp2, many=True)
                                        ir_data = info_serialised2.data
                                        ir_data = json.dumps(ir_data)
                                        ir_data = str(ir_data).replace('\\', '').replace('"room_data": "', '"room_data": ').replace('"}]}]}"}]', '"}]}]}}]').replace('"}]}]}",', '"}]}]},')
                                        ir_data = '{"rooms": ' + ir_data + ' }'
                                        ir_data = json.loads(ir_data)
                                    except Exception as e:
                                        print(e)
                                        ir_data = None
                                elif parent_rec.Is_parent is False and parent_rec.Unknownfield is None:
                                    parent_resp_id = parent_rec.Createdby
                                    room_access = parent_rec.Room_Permission
                                    # ir_access = parent_rec.IR_Permission
                                    fail = str(room_access).replace(' ', '').replace(',', '\',\'').replace('[', '[\'').replace(']', '\']')
                                    # fail_ir = str(ir_access).replace(' ', '').replace(',', '\',\'').replace('[', '[\'').replace(']', '\']')
                                    # ir_dictionary = eval(fail_ir)
                                    final_dictionary = eval(fail)
                                    data_set = '{"rooms":['
                                    for length in range(len(final_dictionary)):
                                        device_records = Device.objects.filter(Devicename=final_dictionary[length])
                                        check = device_records[0]
                                        dname = check.Devicename
                                        imagep = check.Imagepath
                                        duname = check.Deviceusername
                                        pubdata = check.Publisheddata
                                        company_name = check.Devicecompanyname
                                        pubdata = eval(pubdata)
                                        tdata = check.Typed
                                        tdata = eval(tdata)
                                        namea = check.Namer
                                        namea = eval(namea)
                                        ir = check.Work
                                        data_set = str(data_set) + '{"roomid":"' + str(dname) + '","roomImg":"' + str(imagep) + '","name":"' + str(duname) + '","roomd":[{"namer":' + str(len(pubdata)) + ',"device":['
                                        for ll in range(len(pubdata)):
                                            data_set = str(data_set) + '{"type":"' + str(tdata[ll]) + '","index":"' + str(ll) + '","assign":"@' + '","Gcode":"' + str(company_name) + '","Company_name":"' + str(dname) + '","name":"' + str(namea[ll]) + '","action":"' + str(pubdata[ll]) + '","irdata":"' + str(ir) + '","pub":"' + str(parent_resp_id) + '/' + str(dname) + 'G/Device/' + str(pubdata[ll]) + '","sub":"' + str(parent_resp_id) + '/' + str(dname) + 'G/App/' + str(pubdata[ll]) + '"}'
                                            if ll != len(pubdata) - 1:
                                                data_set += ','
                                        data_set += ']}]}'
                                        if length != len(final_dictionary) - 1:
                                            data_set += ','
                                    data_set += ']}'
                                    data_set = json.loads(data_set)
                                    try:
                                        room_resp2 = IRRoomInfo.objects.filter(UserNumber=serializer.data['phone']).values()
                                        info_serialised2 = UserRoomInfoListSerializer(room_resp2, many=True)
                                        ir_data = info_serialised2.data
                                        ir_data = json.dumps(ir_data)
                                        ir_data = str(ir_data).replace('\\', '').replace('"roomd": "', '"roomd": ').replace('"}]}]}"}]', '"}]}]}}]')
                                        ir_data = '{"rooms": ' + ir_data + ' }'
                                        ir_data = json.loads(ir_data)
                                    except Exception as e:
                                        print(e)
                                        ir_data = None
                                elif parent_rec.Is_parent is False and parent_rec.Unknownfield is not None:
                                    try:
                                        # parent_resp_id = parent_rec.Createdby
                                        room_access = parent_rec.Room_Permission
                                        # ir_access = parent_rec.IR_Permission
                                        fail = str(room_access).replace(' ', '').replace(',', '\',\'').replace('[', '[\'').replace(']', '\']')
                                        # fail_ir = str(ir_access).replace(' ', '').replace(',', '\',\'').replace('[', '[\'').replace(']', '\']')
                                        # ir_dictionary = eval(fail_ir)
                                        final_dictionary = eval(fail)
                                        for length in range(len(final_dictionary)):
                                            device_records = UserRoomInfo.objects.filter(id=final_dictionary[length])
                                            check = device_records[0]
                                            data_set += '{"roomid":"'+str(check.id) + '","roomImg":"' + str(check.ImagePath) + '","name":"' + str(check.NamePath) + '","roomd":[' + str(check.Response) + ']},'
                                        data_set += ']}'
                                        data_set = str(data_set).replace('\\', '').replace(']},]}', ']}]}')
                                        data_set = json.loads(data_set)
                                    except Exception as e:
                                        print(e)
                                        data_set = None
                                    try:
                                        room_resp2 = IRRoomInfo.objects.filter(UserNumber=serializer.data['phone']).values()
                                        info_serialised2 = IRRoomInfoListSerializer(room_resp2, many=True)
                                        ir_data = info_serialised2.data
                                        ir_data = json.dumps(ir_data)
                                        ir_data = str(ir_data).replace('\\', '').replace('"room_data": "', '"room_data": ').replace('"}]}]}"}]', '"}]}]}}]').replace('"}]}]}",', '"}]}]},')
                                        ir_data = '{"rooms": ' + ir_data + ' }'
                                        ir_data = json.loads(ir_data)
                                    except Exception as e:
                                        print(e)
                                        ir_data = None
                                if parent_rec.Room_Permission == 'null':
                                    try2 = 'False'
                                else:
                                    try2 = 'true'
                                if parent_rec.Rgb_Permission == 'null':
                                    try3 = 'False'
                                else:
                                    try3 = 'true'
                                return JsonResponse({"rooms_info_available": try2, "rgb_rooms_info_available": try3, "IP": settings.IP, "PORT": settings.IP_PORT, "Field": parent_rec.Unknownfield, "key1": parent_rec.Key1, "key2": parent_rec.Key2, "Apnd": settings.ENCRPT, "scheduling": settings.MQTT_SCHEDULING, "grouping": settings.MQTT_GROUPING, "skd": settings.SKD, "time": settings.TIME, "all_on": settings.ALL_ON, "all_off": settings.ALL_OFF, "timer": settings.MQTT_TIMER, "is_parent": parent_rec.Is_parent, "room_permissions": parent_rec.Room_Permission, "rgb_room_permissions": parent_rec.Rgb_Permission, "user_info": {"name": parent_rec.Username, "number": parent_rec.Usernumber, "email": parent_rec.Useremail, "prfimg": parent_rec.ProfileImg, "backimg": parent_rec.BacgroundImg}, "rooms_info": data_set, "Remote": ir_data}, status=status.HTTP_200_OK)
                            except Exception as e:
                                print(e)
                                return JsonResponse({"INFO": e}, status=status.HTTP_400_BAD_REQUEST)
                        else:
                            if parent_rec.Is_parent is True:
                                try:
                                    room_resp = UserRoomInfo.objects.filter(UserNumber=serializer.data['phone']).values()
                                    child_recs_serialised = UserRoomInfoListSerializer(room_resp, many=True)
                                    res_data = child_recs_serialised.data
                                    res_data = json.dumps(res_data)
                                    res_data2 = str(res_data).replace('\\', '').replace('"roomd": "', '"roomd": [').replace('"}]}"}, {', '"}]}]}, {').replace('}]}"}]', '}]}]}]')
                                    res_data3 = '{"rooms":' + res_data2 + '}'
                                    res_data3 = json.loads(res_data3)
                                except Exception as e:
                                    print(e)
                                    return JsonResponse({"INFO": e}, status=status.HTTP_400_BAD_REQUEST)
                                try:
                                    room_resp2 = IRRoomInfo.objects.filter(UserNumber=serializer.data['phone']).values()
                                    info_serialised2 = IRRoomInfoListSerializer(room_resp2, many=True)
                                    ir_data = info_serialised2.data
                                    ir_data = json.dumps(ir_data)
                                    ir_data = str(ir_data).replace('\\', '').replace('"room_data": "', '"room_data": ').replace('"}]}]}"}]', '"}]}]}}]').replace('"}]}]}",', '"}]}]},')
                                    ir_data = '{"rooms": ' + ir_data + ' }'
                                    ir_data = json.loads(ir_data)
                                except Exception as e:
                                    print(e)
                                    ir_data = None
                                if parent_rec.Room_Permission == 'null':
                                    try2 = 'False'
                                else:
                                    try2 = 'true'
                                if parent_rec.Rgb_Permission == 'null':
                                    try3 = 'False'
                                else:
                                    try3 = 'true'
                                return JsonResponse({"rooms_info_available": try2, "rgb_rooms_info_available": try3, "IP": settings.IP, "PORT": settings.IP_PORT, "Field": parent_rec.Unknownfield, "key1": parent_rec.Key1, "key2": parent_rec.Key2, "Apnd": settings.ENCRPT, "scheduling": settings.MQTT_SCHEDULING, "grouping": settings.MQTT_GROUPING, "skd": settings.SKD, "time": settings.TIME, "all_on": settings.ALL_ON, "all_off": settings.ALL_OFF, "timer": settings.MQTT_TIMER, "is_parent": parent_rec.Is_parent, "room_permissions": parent_rec.Room_Permission, "rgb_room_permissions": parent_rec.Rgb_Permission, "user_info": {"name": parent_rec.Username, "number": parent_rec.Usernumber, "email": parent_rec.Useremail, "prfimg": parent_rec.ProfileImg, "backimg": parent_rec.BacgroundImg}, "rooms_info": res_data3, "Remote": ir_data}, status=status.HTTP_200_OK)
                    else:
                        return JsonResponse({"INFO": "Please Contact Administration for Account activation."}, status=status.HTTP_200_OK)
                else:
                    return JsonResponse({"INFO": "No User exists with this Phone Number."}, status=status.HTTP_400_BAD_REQUEST)
            else:
                return JsonResponse({"INFO": "Please check the Auth-Key provided."}, status=status.HTTP_400_BAD_REQUEST)


class IRDeviceDataList(APIView):
    permission_classes = [AllowAny]
    authentication_classes = (CsrfExemptSessionAuthentication, BasicAuthentication)

    # noinspection PyMethodMayBeStatic
    def post(self, request):
        serializer = IRDeviceDataListSerializer(data=request.data, context={'request': request})
        if not serializer.is_valid():
            data = {"INFO": serializer.errors}
            return JsonResponse(data, status=status.HTTP_400_BAD_REQUEST)
        else:
            try:
                if serializer.data['auth_key'] == settings.AUTH_KEY:
                    try:
                        data_test = IRDevice.objects.filter(ParentId=serializer.data['phone']).values()
                        ser_resp = IRDeviceDataListResponseSerializer(data_test, many=True)
                        return JsonResponse({"INFO": " successfully", "devices": ser_resp.data}, status=status.HTTP_200_OK)
                    except Exception as e:
                        print(e)
                        return JsonResponse({"INFO": "not working"}, status=status.HTTP_400_BAD_REQUEST)
                else:
                    return JsonResponse({"INFO": "Please check the Auth-Key provided."}, status=status.HTTP_400_BAD_REQUEST)
            except Exception as e:
                print(e)
                return JsonResponse({"INFO": e}, status=status.HTTP_400_BAD_REQUEST)


class GetIRChildList(APIView):
    permission_classes = [AllowAny]
    authentication_classes = (CsrfExemptSessionAuthentication, BasicAuthentication)

    # noinspection PyMethodMayBeStatic
    def post(self, request):
        serializer = GetChildListSerializer(data=request.data, context={'request': request})
        if not serializer.is_valid():
            data = {"INFO": serializer.errors}
            return JsonResponse(data, status=status.HTTP_400_BAD_REQUEST)
        else:
            child_list_data = Userdata.objects.filter(Createdby=serializer.data['parent_id']).values()
            child_recs_serialised = ParentSerializer(child_list_data, many=True, context={'request': request})
            return JsonResponse({"child_list": child_recs_serialised.data}, status=status.HTTP_200_OK)


class IRUpdateChild(APIView):
    permission_classes = [AllowAny]
    authentication_classes = (CsrfExemptSessionAuthentication, BasicAuthentication)

    # noinspection PyMethodMayBeStatic
    def post(self, request):
        serializer = UpdateChildSerializer(data=request.data, context={'request': request})
        if not serializer.is_valid():
            data = {"INFO": serializer.errors}
            return JsonResponse(data, status=status.HTTP_400_BAD_REQUEST)
        else:
            # noinspection PyBroadException
            try:
                child_rec = Userdata.objects.get(Usernumber=serializer.data['child_id'])
                child_rec.IR_Permission = serializer.data['rooms']
                child_rec.save()
                child_rec_serialised = ParentSerializer(child_rec, context={'request': request})
                return JsonResponse({"INFO": "Child updated successfully", "child_info": child_rec_serialised.data}, status=status.HTTP_200_OK)
            except Userdata.DoesNotExist:
                return JsonResponse({"INFO": "No child exists with the given ID."}, status=status.HTTP_400_BAD_REQUEST)


class DeviceInfoList(APIView):
    permission_classes = [AllowAny]
    authentication_classes = (CsrfExemptSessionAuthentication, BasicAuthentication)

    # noinspection PyMethodMayBeStatic
    def post(self, request):
        serializer = DeviceInfoListSerializer(data=request.data, context={'request': request})
        if not serializer.is_valid():
            data = {"INFO": serializer.errors}
            return JsonResponse(data, status=status.HTTP_400_BAD_REQUEST)
        else:
            if serializer.data['auth_key'] == settings.AUTH_KEY:
                try:
                    parent_recognition = Userdata.objects.get(Usernumber=serializer.data['phone'])
                    print(parent_recognition)
                    account_exists = True
                except Exception as e:
                    print(e)
                    account_exists = False
                if account_exists is True:
                    try:
                        room_resp = Device.objects.filter(Parentid=serializer.data['phone']).values()
                        child_recs_serialised = RoomDeviceInfoListSerializer(room_resp, many=True)
                        data_set = '['
                        for length in range(child_recs_serialised.data.__len__()):
                            tdata = child_recs_serialised.data[length]
                            pubdata = json.loads(tdata['Publisheddata'])
                            namea = json.loads(tdata['Namer'])
                            ir = "null"
                            dname = tdata['Devicename']
                            company_name = tdata['Devicecompanyname']
                            tdata = json.loads(tdata['Typed'])
                            trt = str(child_recs_serialised.data[length]['Assigned_State'])
                            assign = json.loads(trt)
                            # data_set = str(data_set) + '{"roomid":"' + str(dname) + '","roomImg":"' + str(imagep) + '","name":"' + str(duname) + '","roomd":[{"pub":"' + str(parent_resp_id) + '/' + str(dname) + 'G/Device","sub":"' + str(parent_resp_id) + '/' + str(dname) + 'G/App","namer":' + str(len(pubdata)) + ',"device":['
                            for ll in range(len(pubdata)):
                                data_set = str(data_set) + '{"Company_name":"'+str(dname) + '","type":"' + str(tdata[ll]) + '","name":"' + str(namea[ll]) + '","action":"' + str(pubdata[ll]) + '","irdata":"' + str(ir) + '","pub":"' + str(serializer.data['phone']) + '/' + str(dname) + 'G/Device/' + str(pubdata[ll]) + '","sub":"' + str(serializer.data['phone']) + '/' + str(dname) + 'G/App/' + str(pubdata[ll]) + '","assign":"' + str(assign[ll]) + '","index":"' + str(ll) + '","Gcode":"' + str(company_name)+'"}'
                                if ll != len(pubdata) - 1:
                                    data_set += ','
                            #  data_set += ']}]}'
                            if length != child_recs_serialised.data.__len__() - 1:
                                data_set += ','
                        data_set += ']'
                        data_set = json.loads(data_set)
                        return JsonResponse({"Devices": data_set}, status=status.HTTP_200_OK)
                    except Exception as e:
                        print(e)
                        return JsonResponse({"INFO": e}, status=status.HTTP_400_BAD_REQUEST)
                else:
                    return JsonResponse({"INFO": "No User exists with this Phone Number."}, status=status.HTTP_400_BAD_REQUEST)
            else:
                return JsonResponse({"INFO": "Please check the Auth-Key provided."}, status=status.HTTP_400_BAD_REQUEST)


class IRDeviceInfoList(APIView):
    permission_classes = [AllowAny]
    authentication_classes = (CsrfExemptSessionAuthentication, BasicAuthentication)

    # noinspection PyMethodMayBeStatic
    def post(self, request):
        serializer = IRDeviceInfoListSerializer(data=request.data, context={'request': request})
        if not serializer.is_valid():
            data = {"INFO": serializer.errors}
            return JsonResponse(data, status=status.HTTP_400_BAD_REQUEST)
        else:
            if serializer.data['auth_key'] == settings.AUTH_KEY:
                data_test = IRButtonInfo.objects.all()
                ser_resp = IRDeviceListSerializer(data_test, many=True)
                print(ser_resp)
                return JsonResponse({"INFO": " successfully", "check": ser_resp}, status=status.HTTP_200_OK)
            else:
                return JsonResponse({"INFO": "Please check the Auth-Key provided."}, status=status.HTTP_400_BAD_REQUEST)


class UpdateRoomState(APIView):
    permission_classes = [AllowAny]
    authentication_classes = (CsrfExemptSessionAuthentication, BasicAuthentication)

    # noinspection PyMethodMayBeStatic
    def post(self, request):
        serializer = UpdateRoomStateSerializer(data=request.data, context={'request': request})
        if not serializer.is_valid():
            data = {"INFO": serializer.errors}
            return JsonResponse(data, status=status.HTTP_400_BAD_REQUEST)
        else:
            try:
                child_rec = Device.objects.get(Devicename=serializer.data['device_id'])
                state_get = child_rec.Assigned_State
                state_get2 = json.loads(state_get)
                state_get2[int(serializer.data['index'])] = serializer.data['room_state']
                data_set = json.dumps(state_get2)
                child_rec.Assigned_State = data_set
                child_rec.save()
                return JsonResponse({"INFO": "Updated Room Name successfully"}, status=status.HTTP_200_OK)
            except Exception as e:
                print(e)
                return JsonResponse({"INFO": "Contact Customer Support."}, status=status.HTTP_400_BAD_REQUEST)


class UpdateRoomImage(APIView):
    permission_classes = [AllowAny]
    authentication_classes = (CsrfExemptSessionAuthentication, BasicAuthentication)

    # noinspection PyMethodMayBeStatic
    def post(self, request):
        serializer = UpdateRoomImageNameSerializer(data=request.data, context={'request': request})
        if not serializer.is_valid():
            data = {"INFO": serializer.errors}
            return JsonResponse(data, status=status.HTTP_400_BAD_REQUEST)
        else:
            try:
                child_rec = Device.objects.get(id=serializer.data['room_id'])
                child_rec.ImagePath = serializer.data['room_image']
                child_rec.save()
                return JsonResponse({"INFO": "Updated image Name successfully"}, status=status.HTTP_200_OK)
            except Exception as e:
                print(e)
                return JsonResponse({"INFO": "Contact Customer Support."}, status=status.HTTP_400_BAD_REQUEST)


class ChangeRoomImageNew(APIView):
    permission_classes = [AllowAny]
    authentication_classes = (CsrfExemptSessionAuthentication, BasicAuthentication)

    # noinspection PyMethodMayBeStatic
    def post(self, request):
        serializer = ChangeRoomImageNameNewSerializer(data=request.data, context={'request': request})
        if not serializer.is_valid():
            data = {"INFO": serializer.errors}
            return JsonResponse(data, status=status.HTTP_400_BAD_REQUEST)
        else:
            try:
                child_rec = UserRoomInfo.objects.get(id=serializer.data['room_id'])
                child_rec.ImagePath = serializer.data['room_image']
                child_rec.save()
                return JsonResponse({"INFO": "Room Image Has Been Successfully Updated"}, status=status.HTTP_200_OK)
            except Exception as e:
                try:
                    child_rec = Device.objects.get(Devicename=serializer.data['room_id'])
                    child_rec.Imagepath = serializer.data['room_image']
                    child_rec.save()
                    return JsonResponse({"INFO": "Room Image Has Been Successfully Updated"}, status=status.HTTP_200_OK)
                except Exception as el:
                    print(el)
                    res = send_mail("room name problem", str(e), "lalithkumargoona@gmail.com", ["lalithkumargoona@gmail.com"], fail_silently=False)
                    print('test::::', res)
                    return JsonResponse({"INFO": "Contact Customer Support."}, status=status.HTTP_400_BAD_REQUEST)


class ChangeApplianceType(APIView):
    permission_classes = [AllowAny]
    authentication_classes = (CsrfExemptSessionAuthentication, BasicAuthentication)

    # noinspection PyMethodMayBeStatic
    def post(self, request):
        serializer = ChangeApplianceTypeSerializer(data=request.data, context={'request': request})
        if not serializer.is_valid():
            data = {"INFO": serializer.errors}
            return JsonResponse(data, status=status.HTTP_400_BAD_REQUEST)
        else:
            try:
                child_rec = Device.objects.get(Devicecompanyname=serializer.data['code'])
                name_data = child_rec.Typed
                pub_data = child_rec.Publisheddata
                state_get2 = json.loads(name_data)
                state_get2[int(serializer.data['index'])] = serializer.data['type']
                if serializer.data['type'] == 'Fan':
                    pub_get2 = json.loads(pub_data)
                    pub_get2[int(serializer.data['index'])] = 'Zz'
                    data_set2 = json.dumps(pub_get2)
                    child_rec.Publisheddata = data_set2
                data_set = json.dumps(state_get2)
                child_rec.Typed = data_set
                child_rec.save()
                return JsonResponse({"INFO": "Changed Type successfully"}, status=status.HTTP_200_OK)
            except Exception as e:
                print(e)
                return JsonResponse({"INFO": "Contact Customer Support."}, status=status.HTTP_400_BAD_REQUEST)


class ChangeRoomNameNew(APIView):
    permission_classes = [AllowAny]
    authentication_classes = (CsrfExemptSessionAuthentication, BasicAuthentication)

    # noinspection PyMethodMayBeStatic
    def post(self, request):
        serializer = ChangeRoomNameNewSerializer(data=request.data, context={'request': request})
        if not serializer.is_valid():
            data = {"INFO": serializer.errors}
            return JsonResponse(data, status=status.HTTP_400_BAD_REQUEST)
        else:
            try:
                child_rec = UserRoomInfo.objects.get(id=serializer.data['room_id'])
                child_rec.NamePath = serializer.data['room_name']
                child_rec.save()
                return JsonResponse({"INFO": "Room Name Has Been Successfully Updated"}, status=status.HTTP_200_OK)
            except Exception as e:
                try:
                    child_rec = Device.objects.get(Devicename=serializer.data['room_id'])
                    child_rec.Deviceusername = serializer.data['room_name']
                    child_rec.save()
                    return JsonResponse({"INFO": "Room Name Has Been Successfully Updated"}, status=status.HTTP_200_OK)
                except Exception as el:
                    print(el)
                    res = send_mail("room name problem", str(e), "lalithkumargoona@gmail.com", ["lalithkumargoona@gmail.com"], fail_silently=False)
                    print('test::::', res)
                    return JsonResponse({"INFO": "Contact Customer Support."}, status=status.HTTP_400_BAD_REQUEST)


class DeRegisterFromRoom(APIView):
    permission_classes = [AllowAny]
    authentication_classes = (CsrfExemptSessionAuthentication, BasicAuthentication)

    # noinspection PyMethodMayBeStatic
    def post(self, request):
        serializer = DeregisterFromRoomSerializer(data=request.data, context={'request': request})
        if not serializer.is_valid():
            data = {"INFO": serializer.errors}
            return JsonResponse(data, status=status.HTTP_400_BAD_REQUEST)
        else:
            try:
                child_rec = UserRoomInfo.objects.get(id=serializer.data['id'])
                room_data_get = child_rec.Response
                j_data = json.loads(room_data_get)
                for item in j_data['device']:
                    device_off = Device.objects.get(Devicecompanyname=item['Gcode'])
                    room_data_get = device_off.Assigned_State
                    rdata = json.loads(room_data_get)
                    intval_num = int(item['index'])
                    rdata[intval_num] = 'off'
                    rdata = json.dumps(rdata)
                    device_off.Assigned_State = rdata
                    device_off.save()
                    # if item['index'] =serializer.data['index'] and item['Gcode'] == serializer.data['code']:
                    #     item['name'] = serializer.data['icon_name']
                child_rec.delete()
                return JsonResponse({"INFO": "Updated Room Name Successfully"}, status=status.HTTP_200_OK)
            except Exception as e:
                print(e)
                return JsonResponse({"INFO": "Contact Customer Support."}, status=status.HTTP_400_BAD_REQUEST)


class ChangeApplianceName(APIView):
    permission_classes = [AllowAny]
    authentication_classes = (CsrfExemptSessionAuthentication, BasicAuthentication)

    # noinspection PyMethodMayBeStatic
    def post(self, request):
        serializer = ChangeApplianceNameSerializer(data=request.data, context={'request': request})
        if not serializer.is_valid():
            data = {"INFO": serializer.errors}
            return JsonResponse(data, status=status.HTTP_400_BAD_REQUEST)
        else:
            try:
                child_rec = UserRoomInfo.objects.get(id=serializer.data['room_id'])
                room_data_get = child_rec.Response
                j_data = json.loads(room_data_get)
                for item in j_data['device']:
                    if item['index'] == serializer.data['index'] and item['Gcode'] == serializer.data['code']:
                        item['name'] = serializer.data['icon_name']
                json_file = str(j_data)
                child_rec.Response = json_file.replace('\'', '\"')
                child_rec.save()
                return JsonResponse({"INFO": "Name Has Been Successfully Updated"}, status=status.HTTP_200_OK)
            except Exception as e:
                print(e)
                try:
                    d_name_list = Device.objects.get(Devicecompanyname=serializer.data['code'])
                    #  child_rec.Deviceusername = serializer.data['room_name']
                    rdata = json.loads(d_name_list.Namer)
                    int_val_num = int(serializer.data['index'])
                    rdata[int_val_num] = serializer.data['icon_name']
                    rdata = json.dumps(rdata)
                    d_name_list.Namer = rdata
                    d_name_list.save()
                    return JsonResponse({"INFO": "Name Has Been Successfully Updated"}, status=status.HTTP_200_OK)
                except Exception as el:
                    print(el)
                    try:
                        d_name_list = RGB.objects.get(RGB_Devicecompanyname=serializer.data['code'])
                        d_name_list.RGB_Deviceusername = serializer.data['icon_name']
                        d_name_list.save()
                        return JsonResponse({"INFO": "Name Has Been Successfully Updated"}, status=status.HTTP_200_OK)
                    except Exception as el2:
                        print(el2)
                        res = send_mail("room name problem", str(el2), "lalithkumargoona@gmail.com", ["lalithkumargoona@gmail.com"], fail_silently=False)
                        print(res)
                        return JsonResponse({"INFO": "Contact Customer Support."}, status=status.HTTP_400_BAD_REQUEST)


class GetRoomsInfo(APIView):
    permission_classes = [AllowAny]
    authentication_classes = (CsrfExemptSessionAuthentication, BasicAuthentication)

    # noinspection PyMethodMayBeStatic
    def post(self, request):
        serializer = RoomsInfoSerializer(data=request.data, context={'request': request})
        if not serializer.is_valid():
            data = {"INFO": serializer.errors}
            return JsonResponse(data, status=status.HTTP_400_BAD_REQUEST)
        else:
            # noinspection PyBroadException
            try:
                child_rec = Userdata.objects.get(Usernumber=serializer.data['number'])
                ini_string = json.dumps(serializer.data['response'])
                final_dictionary = json.loads(ini_string)
                child_rec.Response = final_dictionary  # serializer.data['response']
                child_rec.save()
                return JsonResponse({"INFO": "Response updated successfully"}, status=status.HTTP_200_OK)
            except Exception as e:
                print(e)
                return JsonResponse({"INFO": "No user exists with the given ID."}, status=status.HTTP_400_BAD_REQUEST)


class CreateRoom(APIView):
    permission_classes = [AllowAny]
    authentication_classes = (CsrfExemptSessionAuthentication, BasicAuthentication)

    # noinspection PyMethodMayBeStatic
    def post(self, request):
        serializer = CreateRoomSerializer(data=request.data, context={'request': request})
        if not serializer.is_valid():
            data = {"INFO": serializer.errors}
            return JsonResponse(data, status=status.HTTP_400_BAD_REQUEST)
        else:
            if serializer.data['auth_key'] == settings.AUTH_KEY:
                # noinspection PyBroadException
                try:

                    f = UserRoomInfo(Response=serializer.data['response'], ImagePath=serializer.data['image_path'],
                                     NamePath=serializer.data['name'], UserNumber=serializer.data['phone'])
                    f.save()
                    id_data = f.id
                    check = serializer.data['response']
                    y = json.loads(check)
                    count = int(y["namer"])
                    for data_range in range(count):
                        name = y["device"][data_range]["Company_name"]
                        index_num = y["device"][data_range]["index"]
                        child_rec = Device.objects.get(Devicename=name)
                        state_get = child_rec.Assigned_State
                        state_get2 = json.loads(state_get)
                        state_get2[int(index_num)] = 'on'
                        data_set = json.dumps(state_get2)
                        child_rec.Assigned_State = data_set
                        child_rec.save()
                    return JsonResponse({"INFO": "Room Created Successfully", "id": id_data}, status=status.HTTP_200_OK)
                except Exception as e:
                    print(e)
                    return JsonResponse({"INFO": "No user exists with the given ID."}, status=status.HTTP_400_BAD_REQUEST)
            else:
                return JsonResponse({"INFO": "Please check the Auth-Key provided."}, status=status.HTTP_400_BAD_REQUEST)


class CreateIRRoom(APIView):
    permission_classes = [AllowAny]
    authentication_classes = (CsrfExemptSessionAuthentication, BasicAuthentication)

    # noinspection PyMethodMayBeStatic
    def post(self, request):
        serializer = CreateIRRoomSerializer(data=request.data, context={'request': request})
        if not serializer.is_valid():
            data = {"INFO": serializer.errors}
            return JsonResponse(data, status=status.HTTP_400_BAD_REQUEST)
        else:
            if serializer.data['auth_key'] == settings.AUTH_KEY:
                # noinspection PyBroadException
                try:

                    f = IRRoomInfo(Response=serializer.data['response'], ImagePath=serializer.data['image_path'], NamePath=serializer.data['name'], UserNumber=serializer.data['phone'], PubData=serializer.data['pub'], SubData=serializer.data['sub'], DeviceId=serializer.data['device_id'])
                    f.save()
                    id_data = f.id
                    return JsonResponse({"INFO": "Room Created Successfully", "id": id_data}, status=status.HTTP_200_OK)
                except Exception as e:
                    print(e)
                    return JsonResponse({"INFO": "No user exists with the given ID."}, status=status.HTTP_400_BAD_REQUEST)
            else:
                return JsonResponse({"INFO": "Please check the Auth-Key provided."}, status=status.HTTP_400_BAD_REQUEST)


class DeleteIRRoom(APIView):
    permission_classes = [AllowAny]
    authentication_classes = (CsrfExemptSessionAuthentication, BasicAuthentication)

    # noinspection PyMethodMayBeStatic
    def post(self, request):
        serializer = DeleteRoomSerializer(data=request.data, context={'request': request})
        if not serializer.is_valid():
            data = {"INFO": serializer.errors}
            return JsonResponse(data, status=status.HTTP_400_BAD_REQUEST)
        else:
            if serializer.data['auth_key'] == settings.AUTH_KEY:
                # noinspection PyBroadException
                try:
                    room_delete = IRRoomInfo.objects.get(id=serializer.data['room_id'])
                    room_delete.delete()
                    return JsonResponse({"INFO": "room delete successfully"}, status=status.HTTP_200_OK)
                except Exception as e:
                    print(e)
                    return JsonResponse({"INFO": "No user exists with the given ID."}, status=status.HTTP_400_BAD_REQUEST)
            else:
                return JsonResponse({"INFO": "Please check the Auth-Key provided."}, status=status.HTTP_400_BAD_REQUEST)


class DeleteRoom(APIView):
    permission_classes = [AllowAny]
    authentication_classes = (CsrfExemptSessionAuthentication, BasicAuthentication)

    # noinspection PyMethodMayBeStatic
    def post(self, request):
        serializer = DeleteRoomSerializer(data=request.data, context={'request': request})
        if not serializer.is_valid():
            data = {"INFO": serializer.errors}
            return JsonResponse(data, status=status.HTTP_400_BAD_REQUEST)
        else:
            if serializer.data['auth_key'] == settings.AUTH_KEY:
                # noinspection PyBroadException
                try:
                    room_delete = UserRoomInfo.objects.get(id=serializer.data['room_id'])
                    room_delete.delete()
                    return JsonResponse({"INFO": "room delete successfully"}, status=status.HTTP_200_OK)
                except Exception as e:
                    print(e)
                    return JsonResponse({"INFO": "No user exists with the given ID."}, status=status.HTTP_400_BAD_REQUEST)
            else:
                return JsonResponse({"INFO": "Please check the Auth-Key provided."}, status=status.HTTP_400_BAD_REQUEST)


class UpdateResponse(APIView):
    permission_classes = [AllowAny]
    authentication_classes = (CsrfExemptSessionAuthentication, BasicAuthentication)

    # noinspection PyMethodMayBeStatic
    def post(self, request):
        serializer = UpdateResponseSerializer(data=request.data, context={'request': request})
        if not serializer.is_valid():
            data = {"INFO": serializer.errors}
            return JsonResponse(data, status=status.HTTP_400_BAD_REQUEST)
        else:
            # noinspection PyBroadException
            try:
                child_rec = Userdata.objects.get(Usernumber=serializer.data['number'])
                # ini_string = json.dumps(serializer.data['response'])
                # final_dictionary = json.loads(ini_string)
                if serializer.data['response'] == settings.AUTH_KEY:
                    child_rec.Response = None  # serializer.data['response']
                    child_rec.save()
                else:
                    child_rec.Response = serializer.data['response']
                    child_rec.save()
                return JsonResponse({"INFO": "Response updated successfully"}, status=status.HTTP_200_OK)
            except Exception as e:
                print(e)
                return JsonResponse({"INFO": "No child exists with the given ID."}, status=status.HTTP_400_BAD_REQUEST)


class ChangeRoomResponse(APIView):
    permission_classes = [AllowAny]
    authentication_classes = (CsrfExemptSessionAuthentication, BasicAuthentication)

    # noinspection PyMethodMayBeStatic
    def post(self, request):
        serializer = ChangeRoomResponseSerializer(data=request.data, context={'request': request})
        if not serializer.is_valid():
            data = {"INFO": serializer.errors}
            return JsonResponse(data, status=status.HTTP_400_BAD_REQUEST)
        else:
            # noinspection PyBroadException
            try:
                child_rec = UserRoomInfo.objects.get(id=serializer.data['id'])
                child_rec.Response = serializer.data['response']
                child_rec.save()
                return JsonResponse({"INFO": "Response updated successfully"}, status=status.HTTP_200_OK)
            except Exception as e:
                print(e)
                return JsonResponse({"INFO": "No child exists with the given ID."}, status=status.HTTP_400_BAD_REQUEST)


class UpdateIRButton(APIView):
    permission_classes = [AllowAny]
    authentication_classes = (CsrfExemptSessionAuthentication, BasicAuthentication)

    # noinspection PyMethodMayBeStatic
    def post(self, request):
        serializer = UpdateIRButtonSerializer(data=request.data, context={'request': request})
        if not serializer.is_valid():
            data = {"INFO": serializer.errors}
            return JsonResponse(data, status=status.HTTP_400_BAD_REQUEST)
        else:
            # noinspection PyBroadException
            try:
                protocol = serializer.data['protocol']
                product_name_id = serializer.data['product_name_id']
                brand_name = serializer.data['brand_name']
                repeat_count = serializer.data['repeat_count']
                bits_count = serializer.data['bits']
                size_count = serializer.data['size_count']
                # {"A": "SINGLE", "DATA": "0xC0000C", "NAME": "Power", "Protocol": "RC6", "BITS": "0", "REPEAT": "2", "SIZE": "0"}
                if 'button1' in serializer.data:
                    button1 = '{"A": "Single", "DATA": "'+serializer.data['button1']+'", "NAME": "1", "Protocol": "'+protocol+'", "BITS": "'+bits_count+'", "REPEAT": "'+repeat_count+'", "SIZE": "'+size_count+'"}'
                else:
                    button1 = None
                if 'button2' in serializer.data:
                    button2 = '{"A": "Single", "DATA": "'+serializer.data['button2']+'", "NAME": "1", "Protocol": "'+protocol+'", "BITS": "'+bits_count+'", "REPEAT": "'+repeat_count+'", "SIZE": "'+size_count+'"}'
                else:
                    button2 = None
                if 'button3' in serializer.data:
                    button3 = '{"A": "Single", "DATA": "'+serializer.data['button3']+'", "NAME": "1", "Protocol": "'+protocol+'", "BITS": "'+bits_count+'", "REPEAT": "'+repeat_count+'", "SIZE": "'+size_count+'"}'
                else:
                    button3 = None
                if 'button4' in serializer.data:
                    button4 = '{"A": "Single", "DATA": "'+serializer.data['button4']+'", "NAME": "1", "Protocol": "'+protocol+'", "BITS": "'+bits_count+'", "REPEAT": "'+repeat_count+'", "SIZE": "'+size_count+'"}'
                else:
                    button4 = None
                if 'button5' in serializer.data:
                    button5 = '{"A": "Single", "DATA": "'+serializer.data['button5']+'", "NAME": "1", "Protocol": "'+protocol+'", "BITS": "'+bits_count+'", "REPEAT": "'+repeat_count+'", "SIZE": "'+size_count+'"}'
                else:
                    button5 = None
                if 'button6' in serializer.data:
                    button6 = '{"A": "Single", "DATA": "'+serializer.data['button6']+'", "NAME": "1", "Protocol": "'+protocol+'", "BITS": "'+bits_count+'", "REPEAT": "'+repeat_count+'", "SIZE": "'+size_count+'"}'
                else:
                    button6 = None
                if 'button7' in serializer.data:
                    button7 = '{"A": "Single", "DATA": "'+serializer.data['button7']+'", "NAME": "1", "Protocol": "'+protocol+'", "BITS": "'+bits_count+'", "REPEAT": "'+repeat_count+'", "SIZE": "'+size_count+'"}'
                else:
                    button7 = None
                if 'button8' in serializer.data:
                    button8 = '{"A": "Single", "DATA": "'+serializer.data['button8']+'", "NAME": "1", "Protocol": "'+protocol+'", "BITS": "'+bits_count+'", "REPEAT": "'+repeat_count+'", "SIZE": "'+size_count+'"}'
                else:
                    button8 = None
                if 'button9' in serializer.data:
                    button9 = '{"A": "Single", "DATA": "'+serializer.data['button9']+'", "NAME": "1", "Protocol": "'+protocol+'", "BITS": "'+bits_count+'", "REPEAT": "'+repeat_count+'", "SIZE": "'+size_count+'"}'
                else:
                    button9 = None
                if 'button10' in serializer.data:
                    button10 = '{"A": "Single", "DATA": "'+serializer.data['button10']+'", "NAME": "1", "Protocol": "'+protocol+'", "BITS": "'+bits_count+'", "REPEAT": "'+repeat_count+'", "SIZE": "'+size_count+'"}'
                else:
                    button10 = None
                if 'button11' in serializer.data:
                    button11 = '{"A": "Single", "DATA": "'+serializer.data['button11']+'", "NAME": "1", "Protocol": "'+protocol+'", "BITS": "'+bits_count+'", "REPEAT": "'+repeat_count+'", "SIZE": "'+size_count+'"}'
                else:
                    button11 = None
                if 'button12' in serializer.data:
                    button12 = '{"A": "Single", "DATA": "'+serializer.data['button12']+'", "NAME": "1", "Protocol": "'+protocol+'", "BITS": "'+bits_count+'", "REPEAT": "'+repeat_count+'", "SIZE": "'+size_count+'"}'
                else:
                    button12 = None
                if 'button13' in serializer.data:
                    button13 = '{"A": "Single", "DATA": "'+serializer.data['button13']+'", "NAME": "1", "Protocol": "'+protocol+'", "BITS": "'+bits_count+'", "REPEAT": "'+repeat_count+'", "SIZE": "'+size_count+'"}'
                else:
                    button13 = None
                if 'button14' in serializer.data:
                    button14 = '{"A": "Single", "DATA": "'+serializer.data['button14']+'", "NAME": "1", "Protocol": "'+protocol+'", "BITS": "'+bits_count+'", "REPEAT": "'+repeat_count+'", "SIZE": "'+size_count+'"}'
                else:
                    button14 = None
                if 'button15' in serializer.data:
                    button15 = '{"A": "Single", "DATA": "'+serializer.data['button15']+'", "NAME": "1", "Protocol": "'+protocol+'", "BITS": "'+bits_count+'", "REPEAT": "'+repeat_count+'", "SIZE": "'+size_count+'"}'
                else:
                    button15 = None
                if 'button16' in serializer.data:
                    button16 = '{"A": "Single", "DATA": "'+serializer.data['button16']+'", "NAME": "1", "Protocol": "'+protocol+'", "BITS": "'+bits_count+'", "REPEAT": "'+repeat_count+'", "SIZE": "'+size_count+'"}'
                else:
                    button16 = None
                if 'button17' in serializer.data:
                    button17 = '{"A": "Single", "DATA": "'+serializer.data['button17']+'", "NAME": "1", "Protocol": "'+protocol+'", "BITS": "'+bits_count+'", "REPEAT": "'+repeat_count+'", "SIZE": "'+size_count+'"}'
                else:
                    button17 = None
                if 'button18' in serializer.data:
                    button18 = '{"A": "Single", "DATA": "'+serializer.data['button18']+'", "NAME": "1", "Protocol": "'+protocol+'", "BITS": "'+bits_count+'", "REPEAT": "'+repeat_count+'", "SIZE": "'+size_count+'"}'
                else:
                    button18 = None
                if 'button19' in serializer.data:
                    button19 = '{"A": "Single", "DATA": "'+serializer.data['button19']+'", "NAME": "1", "Protocol": "'+protocol+'", "BITS": "'+bits_count+'", "REPEAT": "'+repeat_count+'", "SIZE": "'+size_count+'"}'
                else:
                    button19 = None
                if 'button20' in serializer.data:
                    button20 = '{"A": "Single", "DATA": "'+serializer.data['button20']+'", "NAME": "1", "Protocol": "'+protocol+'", "BITS": "'+bits_count+'", "REPEAT": "'+repeat_count+'", "SIZE": "'+size_count+'"}'
                else:
                    button20 = None
                if 'button21' in serializer.data:
                    button21 = '{"A": "Single", "DATA": "'+serializer.data['button21']+'", "NAME": "1", "Protocol": "'+protocol+'", "BITS": "'+bits_count+'", "REPEAT": "'+repeat_count+'", "SIZE": "'+size_count+'"}'
                else:
                    button21 = None
                if 'button22' in serializer.data:
                    button22 = '{"A": "Single", "DATA": "'+serializer.data['button22']+'", "NAME": "1", "Protocol": "'+protocol+'", "BITS": "'+bits_count+'", "REPEAT": "'+repeat_count+'", "SIZE": "'+size_count+'"}'
                else:
                    button22 = None
                if 'button23' in serializer.data:
                    button23 = '{"A": "Single", "DATA": "'+serializer.data['button23']+'", "NAME": "1", "Protocol": "'+protocol+'", "BITS": "'+bits_count+'", "REPEAT": "'+repeat_count+'", "SIZE": "'+size_count+'"}'
                else:
                    button23 = None
                if 'button24' in serializer.data:
                    button24 = '{"A": "Single", "DATA": "'+serializer.data['button24']+'", "NAME": "1", "Protocol": "'+protocol+'", "BITS": "'+bits_count+'", "REPEAT": "'+repeat_count+'", "SIZE": "'+size_count+'"}'
                else:
                    button24 = None
                if 'button25' in serializer.data:
                    button25 = '{"A": "Single", "DATA": "'+serializer.data['button25']+'", "NAME": "1", "Protocol": "'+protocol+'", "BITS": "'+bits_count+'", "REPEAT": "'+repeat_count+'", "SIZE": "'+size_count+'"}'
                else:
                    button25 = None
                f = IRButtonInfo(button1=button1, button2=button2, button3=button3, button4=button4,
                                 button5=button5, button6=button6, button7=button7, button8=button8,
                                 button9=button9, button10=button10, button11=button11,
                                 button12=button12, button13=button13, button14=button14, button15=button15,
                                 button16=button16, button17=button17, button18=button18,
                                 button19=button19, button20=button20, protocol=protocol, button21=button21,
                                 button22=button22, button23=button23, button24=button24,
                                 button25=button25, brand_name=brand_name, repeat_count=repeat_count, product_name_id=product_name_id)
                f.save()
                return JsonResponse({"INFO": "IR Data Added successfully"}, status=status.HTTP_200_OK)
            except Exception as e:
                print(e)
                return JsonResponse({"INFO": "Some problem."}, status=status.HTTP_400_BAD_REQUEST)


class UpdateIconName(APIView):
    permission_classes = [AllowAny]
    authentication_classes = (CsrfExemptSessionAuthentication, BasicAuthentication)

    # noinspection PyMethodMayBeStatic
    def post(self, request):
        serializer = UpdateiconnameSerializer(data=request.data, context={'request': request})
        if not serializer.is_valid():
            data = {"INFO": serializer.errors}
            return JsonResponse(data, status=status.HTTP_400_BAD_REQUEST)
        else:
            try:
                child_rec = Device.objects.get(Devicename=serializer.data['device_id'])
                rdata = json.loads(child_rec.Namer)
                rdata2 = serializer.data['iconname']
                intvalnum = int(rdata2[0])
                rdata[intvalnum] = rdata2
                rdata = json.dumps(rdata)
                child_rec.Namer = rdata
                child_rec.save()
                return JsonResponse({"INFO": "Img Name added successfully"}, status=status.HTTP_200_OK)
            except Exception as e:
                print(e)
                some_data = serializer.data['device_id'] + ':::' + serializer.data['iconname'] + ':::' + str(e)
                res = send_mail("icon name problem", str(some_data), "lalithkumargoona@gmail.com", ["lalithkumargoona@gmail.com"], fail_silently=False)
                print(res)
                return JsonResponse({"INFO": "Contact Customer Support."}, status=status.HTTP_400_BAD_REQUEST)


class UpdateRoomName(APIView):
    permission_classes = [AllowAny]
    authentication_classes = (CsrfExemptSessionAuthentication, BasicAuthentication)

    # noinspection PyMethodMayBeStatic
    def post(self, request):
        serializer = UpdateroomnameSerializer(data=request.data, context={'request': request})
        if not serializer.is_valid():
            data = {"INFO": serializer.errors}
            return JsonResponse(data, status=status.HTTP_400_BAD_REQUEST)
        else:
            try:
                child_rec = Device.objects.get(Devicename=serializer.data['device_id'])
                child_rec.Deviceusername = serializer.data['roomname']
                child_rec.save()
                return JsonResponse({"INFO": "Updated Room Name successfully"}, status=status.HTTP_200_OK)
            except Exception as e:
                try:
                    child_rec = UserRoomInfo.objects.get(id=serializer.data['device_id'])
                    child_rec.ImagePath = serializer.data['roomname']
                    child_rec.save()
                    return JsonResponse({"INFO": "Updated Room Name successfully"}, status=status.HTTP_200_OK)
                except Exception as el:
                    print(el)
                    res = send_mail("room name problem", str(e), "lalithkumargoona@gmail.com", ["lalithkumargoona@gmail.com"], fail_silently=False)
                    print(res)
                    return JsonResponse({"INFO": "Contact Customer Support."}, status=status.HTTP_400_BAD_REQUEST)


class InstallTeam(APIView):
    permission_classes = [AllowAny]
    authentication_classes = (CsrfExemptSessionAuthentication, BasicAuthentication)

    # noinspection PyMethodMayBeStatic
    def post(self, request):
        serializer = UpdateroomnameSerializer(data=request.data, context={'request': request})
        if not serializer.is_valid():
            data = {"INFO": serializer.errors}
            return JsonResponse(data, status=status.HTTP_400_BAD_REQUEST)
        else:
            try:
                dev_sched = Device(Namer=serializer.data['inteam'])
                dev_sched.save()
                return JsonResponse({"INFO": "Updated successfully"}, status=status.HTTP_200_OK)
            except Exception as e:
                print(e)
                return JsonResponse({"INFO": "Contact Customer Support."}, status=status.HTTP_400_BAD_REQUEST)


class UpdatePrfImg(APIView):
    permission_classes = [AllowAny]
    authentication_classes = (CsrfExemptSessionAuthentication, BasicAuthentication)

    # noinspection PyMethodMayBeStatic
    def post(self, request):
        serializer = UpdateprofileimgSerializer(data=request.data, context={'request': request})
        if not serializer.is_valid():
            data = {"INFO": serializer.errors}
            return JsonResponse(data, status=status.HTTP_400_BAD_REQUEST)
        else:
            try:
                child_rec = Userdata.objects.get(Usernumber=serializer.data['device_id'])
                child_rec.ProfileImg = serializer.data['pimg']
                child_rec.save()
                return JsonResponse({"INFO": "Profile Image Updated successfully"}, status=status.HTTP_200_OK)
            except Exception as e:
                print(e)
                res = send_mail("image upload problem problem", str(e), "lalithkumargoona@gmail.com", ["lalithkumargoona@gmail.com"], fail_silently=False)
                print(res)
                return JsonResponse({"INFO": "Contact Customer Support."}, status=status.HTTP_400_BAD_REQUEST)


class UpdateBackImg(APIView):
    permission_classes = [AllowAny]
    authentication_classes = (CsrfExemptSessionAuthentication, BasicAuthentication)

    # noinspection PyMethodMayBeStatic
    def post(self, request):
        serializer = UpdateBackImgSerializer(data=request.data, context={'request': request})
        if not serializer.is_valid():
            data = {"INFO": serializer.errors}
            return JsonResponse(data, status=status.HTTP_400_BAD_REQUEST)
        else:
            try:
                child_rec = Userdata.objects.get(Usernumber=serializer.data['device_id'])
                child_rec.BacgroundImg = serializer.data['bimg']
                child_rec.save()
                return JsonResponse({"INFO": "Background Image added successfully"}, status=status.HTTP_200_OK)
            except Exception as e:
                print(e)
                return JsonResponse({"INFO": "Contact Customer Support."}, status=status.HTTP_400_BAD_REQUEST)


class UpdateRoomImg(APIView):
    permission_classes = [AllowAny]
    authentication_classes = (CsrfExemptSessionAuthentication, BasicAuthentication)

    # noinspection PyMethodMayBeStatic
    def post(self, request):
        serializer = UpdateRoomImgSerializer(data=request.data, context={'request': request})
        if not serializer.is_valid():
            data = {"INFO": serializer.errors}
            return JsonResponse(data, status=status.HTTP_400_BAD_REQUEST)
        else:
            try:
                child_rec = Device.objects.get(Devicename=serializer.data['device_id'])
                child_rec.Imagepath = serializer.data['rimg']
                child_rec.save()
                return JsonResponse({"INFO": "Room Image added successfully"}, status=status.HTTP_200_OK)
            except Exception as e:
                try:
                    child_rec = UserRoomInfo.objects.get(id=serializer.data['device_id'])
                    child_rec.ImagePath = serializer.data['rimg']
                    child_rec.save()
                    print(e)
                    return JsonResponse({"INFO": "Room Image added successfully"}, status=status.HTTP_200_OK)
                except Exception as e2:
                    print(e2)
                    return JsonResponse({"INFO": "Contact Customer Support."}, status=status.HTTP_400_BAD_REQUEST)


class DGqr(APIView):
    permission_classes = [AllowAny]
    authentication_classes = (CsrfExemptSessionAuthentication, BasicAuthentication)

    # noinspection PyMethodMayBeStatic
    def post(self, request):
        serializer = DGqrSerializer(data=request.data, context={'request': request})
        if not serializer.is_valid():
            data = {"INFO": serializer.errors}
            return JsonResponse(data, status=status.HTTP_400_BAD_REQUEST)
        else:
            # noinspection PyBroadException
            try:
                dealer_rec = DealerDevice.objects.get(DeviceName=serializer.data['device_no'])
                print(serializer.data['device_no'])
                print(dealer_rec.DeviceName)
                if dealer_rec.DeviceName == serializer.data['device_no']:
                    print('all okay')
                else:
                    return JsonResponse({"INFO": "UnAuthorized Access."}, status=status.HTTP_400_BAD_REQUEST)
            # noinspection PyBroadException
            except Exception as e:
                return JsonResponse({"INFO": "Not Authorized To This Device."}, status=status.HTTP_400_BAD_REQUEST)
            try:
                child_rec = Device.objects.get(Devicecompanyname=serializer.data['device_no'])
                child_rec.Parentid = serializer.data['client_phone']
                child_rec.save()
                return JsonResponse({"INFO": "Successfully added"}, status=status.HTTP_200_OK)
            except Exception as e:
                return JsonResponse({"INFO": "Contact Customer Support."}, status=status.HTTP_400_BAD_REQUEST)


class DRGBqr(APIView):
    permission_classes = [AllowAny]
    authentication_classes = (CsrfExemptSessionAuthentication, BasicAuthentication)

    # noinspection PyMethodMayBeStatic
    def post(self, request):
        serializer = RGBqrSerializer(data=request.data, context={'request': request})
        if not serializer.is_valid():
            data = {"INFO": serializer.errors}
            return JsonResponse(data, status=status.HTTP_400_BAD_REQUEST)
        else:
            # noinspection PyBroadException
            try:
                dealer_rec = DealerDevice.objects.get(DeviceName=serializer.data['device_no'])
                if dealer_rec.DeviceName == serializer.data['device_no']:
                    print('all okay')
                else:
                    return JsonResponse({"INFO": "UnAuthorized Access."}, status=status.HTTP_400_BAD_REQUEST)
            except Exception as e:
                return JsonResponse({"INFO": "Not Authorized To This Device."}, status=status.HTTP_400_BAD_REQUEST)
            # noinspection PyBroadException
            try:
                child_rec = RGB.objects.get(RGB_Devicecompanyname=serializer.data['device_no'])
                if child_rec.RGB_Parentid == '919908799084':
                    child_rec.RGB_Parentid = serializer.data['client_phone']
                    child_rec.save()
                else:
                    return JsonResponse({"INFO": "Already Added to " + child_rec.RGB_Parentid}, status=status.HTTP_200_OK)
                return JsonResponse({"INFO": "Successfully added"}, status=status.HTTP_200_OK)
            except Exception as e:
                print(e)
                return JsonResponse({"INFO": "Contact Customer Support."}, status=status.HTTP_400_BAD_REQUEST)


class Gqr(APIView):
    permission_classes = [AllowAny]
    authentication_classes = (CsrfExemptSessionAuthentication, BasicAuthentication)

    # noinspection PyMethodMayBeStatic
    def post(self, request):
        serializer = GqrSerializer(data=request.data, context={'request': request})
        if not serializer.is_valid():
            data = {"INFO": serializer.errors}
            return JsonResponse(data, status=status.HTTP_400_BAD_REQUEST)
        else:
            try:
                child_rec = Device.objects.get(Devicecompanyname=serializer.data['device_no'])
                child_rec.Parentid = serializer.data['phone']
                child_rec.save()
                return JsonResponse({"INFO": "Successfully added"}, status=status.HTTP_200_OK)
            except Exception as e:
                try:
                    child_rec = RGB.objects.get(RGB_Devicecompanyname=serializer.data['device_no'])
                    if child_rec.RGB_Parentid == '919908799084':
                        child_rec.RGB_Parentid = serializer.data['phone']
                        child_rec.save()
                    else:
                        if serializer.data['phone'] == '919908799084':
                            child_rec.RGB_Parentid = serializer.data['phone']
                            child_rec.save()
                        else:
                            print(e)
                            return JsonResponse({"INFO": "Already Added to " + child_rec.RGB_Parentid},
                                                status=status.HTTP_200_OK)
                    return JsonResponse({"INFO": "Successfully added"}, status=status.HTTP_200_OK)
                except Exception as e:
                    print(e)
                    return JsonResponse({"INFO": "Contact Customer Support."}, status=status.HTTP_400_BAD_REQUEST)


class ActivateUser(APIView):
    permission_classes = [AllowAny]
    authentication_classes = (CsrfExemptSessionAuthentication, BasicAuthentication)

    # noinspection PyMethodMayBeStatic
    def post(self, request):
        serializer = UserActivationSerializer(data=request.data, context={'request': request})

        if not serializer.is_valid():
            data = {"INFO": serializer.errors}
            return JsonResponse(data, status=status.HTTP_400_BAD_REQUEST)
        else:
            try:
                child_rec = Userdata.objects.get(Usernumber=serializer.data['phone'])
                child_rec.Is_action = True
                child_rec.Key1 = 'lalith'
                child_rec.Key2 = 'lalith56'
                child_rec.save()
                return JsonResponse({"INFO": "Successfully added"}, status=status.HTTP_200_OK)
            except Exception as e:
                print(e)
                return JsonResponse({"INFO": "Contact Customer Support."}, status=status.HTTP_400_BAD_REQUEST)


class DActivateUser(APIView):
    permission_classes = [AllowAny]
    authentication_classes = (CsrfExemptSessionAuthentication, BasicAuthentication)

    # noinspection PyMethodMayBeStatic
    def post(self, request):
        serializer = DUserActivationSerializer(data=request.data, context={'request': request})

        if not serializer.is_valid():
            data = {"INFO": serializer.errors}
            return JsonResponse(data, status=status.HTTP_400_BAD_REQUEST)
        else:
            try:
                child_rec = Userdata.objects.get(Usernumber=serializer.data['client_phone']) #DealerUsers
                if child_rec.Is_parent is True:
                    return JsonResponse({"INFO": "User Not Exists or he is already Master, Contact Customer Support."},
                                        status=status.HTTP_400_BAD_REQUEST)
                else:
                    c_name = serializer.data['client_phone']
                    d_name = serializer.data['dealer_id']
                    f = DealerUsers(D_user=c_name, DealerId=d_name)
                    f.save()
                    dealer_rec = Userdata.objects.get(Usernumber=serializer.data['client_phone'])
                    dealer_rec.Is_authenticated = True
                    dealer_rec.Is_action = True
                    dealer_rec.Is_parent = True
                    dealer_rec.Key1 = 'lalith'
                    dealer_rec.Key2 = 'lalith56'
                    dealer_rec.save()
                    return JsonResponse({"INFO": "Successfully added"}, status=status.HTTP_200_OK)
            except Exception as e:
                print(e)
                return JsonResponse({"INFO": "User Not Exists or a Parent, Contact Customer Support."}, status=status.HTTP_400_BAD_REQUEST)


class RGBqr(APIView):
    permission_classes = [AllowAny]
    authentication_classes = (CsrfExemptSessionAuthentication, BasicAuthentication)

    # noinspection PyMethodMayBeStatic
    def post(self, request):
        serializer = RGBqrSerializer(data=request.data, context={'request': request})
        if not serializer.is_valid():
            data = {"INFO": serializer.errors}
            return JsonResponse(data, status=status.HTTP_400_BAD_REQUEST)
        else:
            try:
                child_rec = RGB.objects.get(RGB_Devicecompanyname=serializer.data['device_no'])
                if child_rec.RGB_Parentid == '919908799084':
                    child_rec.RGB_Parentid = serializer.data['phone']
                    child_rec.save()
                else:
                    return JsonResponse({"INFO": "Already Added to " + child_rec.RGB_Parentid}, status=status.HTTP_200_OK)
                return JsonResponse({"INFO": "Successfully added"}, status=status.HTTP_200_OK)
            except Exception as e:
                print(e)
                return JsonResponse({"INFO": "Contact Customer Support."}, status=status.HTTP_400_BAD_REQUEST)


class RGBUpdateRoomName(APIView):
    permission_classes = [AllowAny]
    authentication_classes = (CsrfExemptSessionAuthentication, BasicAuthentication)

    # noinspection PyMethodMayBeStatic
    def post(self, request):
        serializer = RGBUpdateroomnameSerializer(data=request.data, context={'request': request})
        if not serializer.is_valid():
            data = {"INFO": serializer.errors}
            return JsonResponse(data, status=status.HTTP_400_BAD_REQUEST)
        else:
            try:
                child_rec = RGB.objects.get(RGB_Devicename=serializer.data['device_id'])
                child_rec.RGB_Deviceusername = serializer.data['roomname']
                child_rec.save()
                return JsonResponse({"INFO": "Updated Room Name successfully"}, status=status.HTTP_200_OK)
            except Exception as e:
                print(e)
                return JsonResponse({"INFO": "Contact Customer Support."}, status=status.HTTP_400_BAD_REQUEST)


class RGBDeviceAdd(APIView):
    permission_classes = [AllowAny]
    authentication_classes = (CsrfExemptSessionAuthentication, BasicAuthentication)

    # noinspection PyMethodMayBeStatic
    def post(self, request):
        serializer = RGBDeviceaddSerializer(data=request.data, context={'request': request})
        if not serializer.is_valid():
            data = {"INFO": serializer.errors}
            return JsonResponse(data, status=status.HTTP_400_BAD_REQUEST)
        else:
            try:
                devicename = serializer.data['device_name']
                devicecompanyname = serializer.data['company_name']
                publisheddata = '["000"]'
                typedata = '["RGB"]'
                parentid = '919908799084'
                isactive = True
                requestcount = 0
                lastrequested = datetime.datetime.now()
                devicedata = '["RGB"]'
                deviceusername = 'RGB'
                image = 'https://lalith.s3.ap-south-1.amazonaws.com/G2.png'
                tabel_obj = RGB.objects.filter(RGB_Devicename=devicename, RGB_Devicecompanyname=devicecompanyname)
                if len(tabel_obj) > 0:
                    return JsonResponse({"INFO": "Device is Already registered with this ID or Company Name."}, status=status.HTTP_200_OK)
                # noinspection PyBroadException
                try:
                    f = RGB(RGB_Typed=typedata, RGB_Deviceusername=deviceusername, RGB_Devicedata=devicedata, RGB_Devicename=devicename, RGB_IsActive=isactive, RGB_Lastrequested=lastrequested, RGB_Publisheddata=publisheddata, RGB_Requestcount=requestcount, RGB_Devicecompanyname=devicecompanyname, RGB_Imagepath=image, RGB_Parentid=parentid)
                    f.save()
                    # f2 = Device(Typed=typedata, Namer=namerdata, Deviceusername=deviceusername, Devicename=devicename, IsActive=isactive, Lastrequested=lastrequested, Publisheddata=publisheddata, Requestcount=requestcount, Devicecompanyname=devicecompanyname, Imagepath=image, Parentid=parentid, type=deviceusername)
                    # f2.save()
                except Exception as e:
                    print(e)
                    return JsonResponse({"INFO": "Check Device Name or Company Name"}, status=status.HTTP_200_OK)
                return JsonResponse({"INFO": "Device Added"}, status=status.HTTP_200_OK)
            except Exception as e:
                print(e)
                return JsonResponse({"INFO": "Check again"}, status=status.HTTP_200_OK)


class RGBGCode(APIView):
    permission_classes = [AllowAny]
    authentication_classes = (CsrfExemptSessionAuthentication, BasicAuthentication)

    # noinspection PyMethodMayBeStatic
    def get(self, request, device_id):
        serializer = RGBDeviceSerializer(data={'device_id': device_id}, context={'request': request})
        if not(serializer.is_valid()):
            data = {"error": "invalid_request", "error_description": serializer.errors}
            return JsonResponse(data, status=status.HTTP_400_BAD_REQUEST)
        else:
            device_records = RGB.objects.filter(RGB_Devicename=serializer.data['device_id'])
            if len(device_records) > 0:
                return JsonResponse({"INFO": "Device is registered with this Name."}, status=status.HTTP_200_OK)
            else:
                devicename = serializer.data['device_id']
                parentid = '919908799084'
                isactive = False
                requestcount = 0
                try:
                    f = RGB(RGB_Devicename=devicename, RGB_Parentid=parentid, RGB_IsActive=isactive,  RGB_Requestcount=requestcount)
                    f.save()
                except Exception as e:
                    print(e)
                    return JsonResponse({"INFO": "Check Device Name or Company Name"}, status=status.HTTP_200_OK)
                return JsonResponse({"INFO": "Device Added"}, status=status.HTTP_200_OK)


class RGBDeviceAddFirst(APIView):
    permission_classes = [AllowAny]
    authentication_classes = (CsrfExemptSessionAuthentication, BasicAuthentication)

    # noinspection PyMethodMayBeStatic
    def post(self, request):
        serializer = RGBDeviceaddfirstSerializer(data=request.data, context={'request': request})
        if not serializer.is_valid():
            data = {"INFO": serializer.errors}
            return JsonResponse(data, status=status.HTTP_400_BAD_REQUEST)
        else:
            try:
                devicename = serializer.data['device_name']
                parentid = '918008182410'
                isactive = True
                requestcount = 0
                try:
                    f = RGB(RGB_Devicename=devicename, RGB_Parentid=parentid, RGB_IsActive=isactive,  RGB_Requestcount=requestcount)
                    f.save()
                except Exception as e:
                    print(e)
                    return JsonResponse({"INFO": "Check Device Name or Company Name"}, status=status.HTTP_200_OK)
                return JsonResponse({"INFO": "Device Added"}, status=status.HTTP_200_OK)
            except Exception as e:
                print(e)
                return JsonResponse({"INFO": "Check again"}, status=status.HTTP_200_OK)


class Notification(APIView):
    permission_classes = [AllowAny]
    authentication_classes = (CsrfExemptSessionAuthentication, BasicAuthentication)

    # noinspection PyMethodMayBeStatic
    def get(self, request, mobile_id, device_id, switch_id, state):
        device_id = device_id[:-1]
        serializer = FcmSerializer(data={'device_id': device_id, 'mobile_id': mobile_id, 'switch_id': switch_id, 'state': switch_id}, context={'request': request})
        if not(serializer.is_valid()):
            data = {"error": "invalid_request", "error_description": serializer.errors}
            return JsonResponse(data, status=status.HTTP_400_BAD_REQUEST)
        else:
            device_records = Device.objects.filter(Devicename=serializer.data['device_id'])
            mobile_records = Userdata.objects.filter(Usernumber=serializer.data['mobile_id'])
            if len(device_records) > 0:
                dev_rec = device_records[0]
                mob_rec = mobile_records[0]
                aut_key = mob_rec.Notification_Token
                noontime = dev_rec.Notification_Time
                indexes = dev_rec.Publisheddata
                nameless = dev_rec.Namer
                roommate = dev_rec.Deviceusername
                indexj = json.loads(indexes)
                timej = json.loads(noontime)
                namej = json.loads(nameless)
                testj = indexj.index(switch_id)
                namedisp = namej[testj]
                timedisp = timej[testj]
                timedisp = timedisp[1:]
                timeteststring = timedisp.split('E')
                starttime = int(timeteststring[0])
                endtime = int(timeteststring[1])
                now = datetime.datetime.now()
                munits = (now.hour*60) + now.minute
                if starttime <= munits <= endtime:
                    #  namedisp = namedisp[1:]
                    if state == '0':
                        stateval = 'off'
                    else:
                        stateval = 'on'
                    apiurl = "https://fcm.googleapis.com/fcm/send"
                    headers = {'Content-Type': 'application/json', 'Authorization': 'key=AAAAZUesAx0:APA91bFhb_lLGeOR_2TLQgkaejDMRKXmkXFUfpXJJZATdnAl1p-x_MfB88eGLeVOT7jqyJa5vIXk4RG7divCjiIH-9dVtrP-SCy6lXoNcb1eFT2oA97BCMsTe6rbmk9keVXt8brGTAdp'}
                    message = '''{"notification" : {"body" : "''' + roommate + '''  ''' + namedisp + '''   ''' + stateval + '''", "Title":"hello" } , "to" : "''' + aut_key + '''"}'''
                    r = requests.post(url=apiurl, data=message, headers=headers)
                    pastebin_url = r.text
                    return JsonResponse(pastebin_url, safe=False)
                return JsonResponse({"INFO": "Not in Active Time"}, status=status.HTTP_200_OK)
            else:
                return JsonResponse({"INFO": "No Device Added"}, status=status.HTTP_200_OK)


class GetState(APIView):
    permission_classes = [AllowAny]
    authentication_classes = (CsrfExemptSessionAuthentication, BasicAuthentication)

    # noinspection PyMethodMayBeStatic
    def get(self, request, device_id, switch_id):
        device_id = device_id[:-1]
        serializer = GetStateSerializer(data={'device_id': device_id, 'switch_id': switch_id}, context={'request': request})
        if not(serializer.is_valid()):
            data = {"error": "invalid_request", "error_description": serializer.errors}
            return JsonResponse(data, status=status.HTTP_400_BAD_REQUEST)
        else:
            device_records = Device.objects.filter(Devicename=serializer.data['device_id'])
            if len(device_records) > 0:
                dev_rec = device_records[0]
                indexes = dev_rec.Publisheddata
                dstate = dev_rec.Device_State
                dstatejson = json.loads(dstate)
                dpubdatajson = json.loads(indexes)
                pubstring = str(serializer.data['switch_id'])
                invalue = dpubdatajson.index(pubstring)
                reqstring = dstatejson[invalue]
                return JsonResponse({"INFO": reqstring}, status=status.HTTP_200_OK)
            else:
                return JsonResponse({"INFO": "No Device Added"}, status=status.HTTP_200_OK)


class LastState(APIView):
    permission_classes = [AllowAny]
    authentication_classes = (CsrfExemptSessionAuthentication, BasicAuthentication)

    # noinspection PyMethodMayBeStatic
    def get(self, request, device_id, switch_id, switch_state):
        device_id = device_id[:-1]
        serializer = StateSerializer(data={'device_id': device_id, 'switch_id': switch_id, 'switch_state': switch_state}, context={'request': request})
        if not(serializer.is_valid()):
            data = {"error": "invalid_request", "error_description": serializer.errors}
            return JsonResponse(data, status=status.HTTP_400_BAD_REQUEST)
        else:
            device_records = Device.objects.filter(Devicename=serializer.data['device_id'])
            if len(device_records) > 0:
                dev_rec = device_records[0]
                indexes = dev_rec.Publisheddata
                dstate = dev_rec.Device_State
                dstatejson = json.loads(dstate)
                dpubdatajson = json.loads(indexes)
                pubstring = str(serializer.data['switch_id'])
                invalue = dpubdatajson.index(pubstring)
                d_name_list = Device.objects.get(Devicename=serializer.data['device_id'])
                dstatejson[invalue] = serializer.data['switch_state']
                dstatejson = json.dumps(dstatejson)
                d_name_list.Device_State = dstatejson
                d_name_list.save()
                return JsonResponse({"INFO": "Okay"}, status=status.HTTP_200_OK)
            else:
                return JsonResponse({"INFO": "No Device Added"}, status=status.HTTP_200_OK)


class UpdateNotificationToken(APIView):
    permission_classes = [AllowAny]
    authentication_classes = (CsrfExemptSessionAuthentication, BasicAuthentication)

    # noinspection PyMethodMayBeStatic
    def post(self, request):
        serializer = UpdateFcmTokenSerializer(data=request.data, context={'request': request})
        if not serializer.is_valid():
            data = {"INFO": serializer.errors}
            return JsonResponse(data, status=status.HTTP_400_BAD_REQUEST)
        else:
            # noinspection PyBroadException
            try:
                child_rec = Userdata.objects.get(Usernumber=serializer.data['user_id'])
                if child_rec.Notification_Token != serializer.data['fcmtoken']:
                    child_rec.Notification_Token = serializer.data['fcmtoken']
                    child_rec.save()
                return JsonResponse({"INFO": "FCM Token added successfully"}, status=status.HTTP_200_OK)
            except Exception as e:
                print(e)
                return JsonResponse({"INFO": "Contact Customer Support."}, status=status.HTTP_400_BAD_REQUEST)


class UpdateNotificationStatus(APIView):
    permission_classes = [AllowAny]
    authentication_classes = (CsrfExemptSessionAuthentication, BasicAuthentication)

    # noinspection PyMethodMayBeStatic
    def post(self, request):
        serializer = UpdateNotificationStatusSerializer(data=request.data, context={'request': request})
        if not serializer.is_valid():
            data = {"INFO": serializer.errors}
            return JsonResponse(data, status=status.HTTP_400_BAD_REQUEST)
        else:
            try:
                child_rec = Device.objects.get(Devicecompanyname=serializer.data['code'])
                rdata = json.loads(child_rec.Notification_State)
                rdata2 = serializer.data['notification_name']
                list_index = serializer.data['index']
                rdata[int(list_index)] = rdata2
                rdata = json.dumps(rdata)
                child_rec.Notification_State = rdata
                child_rec.save()
                return JsonResponse({"INFO": "Notification Name added successfully"}, status=status.HTTP_200_OK)
            except Exception as e:
                print(e)
                return JsonResponse({"INFO": "Contact Customer Support."}, status=status.HTTP_400_BAD_REQUEST)


class GETNotificationStatus(APIView):
    permission_classes = [AllowAny]
    authentication_classes = (CsrfExemptSessionAuthentication, BasicAuthentication)

    # noinspection PyMethodMayBeStatic
    def post(self, request):
        serializer = GETNotificationStatusSerializer(data=request.data, context={'request': request})
        if not serializer.is_valid():
            data = {"INFO": serializer.errors}
            return JsonResponse(data, status=status.HTTP_400_BAD_REQUEST)
        else:
            try:
                child_rec = Device.objects.get(Devicecompanyname=serializer.data['code'])
                rdata = json.loads(child_rec.Notification_State)
                list_index = serializer.data['index']
                rdata2 = rdata[int(list_index)]
                return JsonResponse({"INFO": rdata2}, status=status.HTTP_200_OK)
            except Exception as e:
                print(e)
                return JsonResponse({"INFO": "Contact Customer Support."}, status=status.HTTP_400_BAD_REQUEST)


class UpdateNotificationTimeStatus(APIView):
    permission_classes = [AllowAny]
    authentication_classes = (CsrfExemptSessionAuthentication, BasicAuthentication)

    # noinspection PyMethodMayBeStatic
    def post(self, request):
        serializer = UpdateNotificationTimeStatusSerializer(data=request.data, context={'request': request})
        if not serializer.is_valid():
            data = {"INFO": serializer.errors}
            return JsonResponse(data, status=status.HTTP_400_BAD_REQUEST)
        else:
            try:
                child_rec = Device.objects.get(Devicecompanyname=serializer.data['code'])
                rdata = json.loads(child_rec.Notification_Time)
                rdata2 = serializer.data['notification_time']
                name_index = serializer.data['index']
                rdata[int(name_index)] = rdata2
                rdata = json.dumps(rdata)
                child_rec.Notification_Time = rdata
                child_rec.save()
                return JsonResponse({"INFO": "Notification time added successfully"}, status=status.HTTP_200_OK)
            except Exception as e:
                print(e)
                return JsonResponse({"INFO": "Contact Customer Support."}, status=status.HTTP_400_BAD_REQUEST)


class HeavyState(APIView):
    permission_classes = [AllowAny]
    authentication_classes = (CsrfExemptSessionAuthentication, BasicAuthentication)

    # noinspection PyMethodMayBeStatic
    def post(self, request):
        serializer = HeavySerializer(data=request.data, context={'request': request})
        if not serializer.is_valid():
            data = {"INFO": serializer.errors}
            return JsonResponse(data, status=status.HTTP_400_BAD_REQUEST)
        else:
            try:
                child_rec = Device.objects.get(Devicename=serializer.data['device_id'])
                rdata = json.loads(child_rec.Notification_State)
                rdata2 = serializer.data['heavy_name']
                intvalnum = int(rdata2[0])
                rdata[intvalnum] = rdata2
                rdata = json.dumps(rdata)
                child_rec.Heavy_State = rdata
                child_rec.save()
                return JsonResponse({"INFO": "Heavy State added successfully"}, status=status.HTTP_200_OK)
            except Exception as e:
                print(e)
                return JsonResponse({"INFO": "Contact Customer Support."}, status=status.HTTP_400_BAD_REQUEST)


class UpdateHeavyTimeStatus(APIView):
    permission_classes = [AllowAny]
    authentication_classes = (CsrfExemptSessionAuthentication, BasicAuthentication)

    # noinspection PyMethodMayBeStatic
    def post(self, request):
        serializer = UpdateHeavyTimeStatusSerializer(data=request.data, context={'request': request})
        if not serializer.is_valid():
            data = {"INFO": serializer.errors}
            return JsonResponse(data, status=status.HTTP_400_BAD_REQUEST)
        else:
            try:
                child_rec = Device.objects.get(Devicename=serializer.data['device_id'])
                rdata = json.loads(child_rec.Notification_Time)
                rdata2 = serializer.data['heavy_time']
                intvalnum = int(rdata2[0])
                rdata[intvalnum] = rdata2
                rdata = json.dumps(rdata)
                child_rec.Heavy_Time = rdata
                child_rec.save()
                return JsonResponse({"INFO": "Notification Name added successfully"}, status=status.HTTP_200_OK)
            except Exception as e:
                print(e)
                return JsonResponse({"INFO": "Contact Customer Support."}, status=status.HTTP_400_BAD_REQUEST)


class DealerAssignToCustomer(APIView):
    permission_classes = [AllowAny]
    authentication_classes = (CsrfExemptSessionAuthentication, BasicAuthentication)

    # noinspection PyMethodMayBeStatic
    def post(self, request):
        serializer = DealerAssignToCustomerSerializer(data=request.data, context={'request': request})

        if not(serializer.is_valid()):
            data = {"error": "invalid_request", "error_description": serializer.errors}
            return JsonResponse(data, status=status.HTTP_400_BAD_REQUEST)
        else:
            try:
                dealer_records = DealerDevice.objects.filter(Dealer_number=serializer.data['dealer_number'], Dealer_device=serializer.data['dealer_id'])
                if len(dealer_records) > 0:
                    dealer_records_change = Device.objects.filter(Devicecompanyname=serializer.data['dealer_id'])
                    dealer_records_change.Parentid = serializer.data['customer_number']
                    dealer_records_change.save()
                    dealer_records.Dealer_customer_number = serializer.data['customer_number']
                    dealer_records.Dealer_device_state = serializer.data['dealer_number']
                    dealer_records.save()
                    return JsonResponse({"Dealer_info": "Updated"}, status=status.HTTP_200_OK)
                else:
                    data = {"INFO": "No Device Assigned for this Dealer"}
                    return JsonResponse(data, status=status.HTTP_200_OK)
            except Exception as e:
                print(e)
                return JsonResponse({"INFO": "Contact Customer Support."}, status=status.HTTP_400_BAD_REQUEST)


class AssignBackToDealer(APIView):
    permission_classes = [AllowAny]
    authentication_classes = (CsrfExemptSessionAuthentication, BasicAuthentication)

    # noinspection PyMethodMayBeStatic
    def post(self, request):
        serializer = AssignToDealerSerializer(data=request.data, context={'request': request})

        if not(serializer.is_valid()):
            data = {"error": "invalid_request", "error_description": serializer.errors}
            return JsonResponse(data, status=status.HTTP_400_BAD_REQUEST)
        else:
            try:
                dealer_records = DealerDevice.objects.filter(Dealer_number=serializer.data['dealer_number'], Dealer_device=serializer.data['dealer_id'])
                if len(dealer_records) > 0:
                    dealer_records.Dealer_device_state = serializer.data['dealer_number']
                    dealer_records.save()
                    return JsonResponse({"Dealer_info": "Updated"}, status=status.HTTP_200_OK)
                else:
                    data = {"INFO": "No Device Assigned for this Dealer"}
                    return JsonResponse(data, status=status.HTTP_200_OK)
            except Exception as e:
                print(e)
                return JsonResponse({"INFO": "Contact Customer Support."}, status=status.HTTP_400_BAD_REQUEST)


class RGBRoomsInfo(APIView):
    permission_classes = [AllowAny]
    authentication_classes = (CsrfExemptSessionAuthentication, BasicAuthentication)

    # noinspection PyMethodMayBeStatic
    def post(self, request):
        serializer = RGBRoomsInfoSerializer(data=request.data, context={'request': request})
        if not serializer.is_valid():
            data = {"INFO": serializer.errors}
            return JsonResponse(data, status=status.HTTP_400_BAD_REQUEST)
        else:
            if serializer.data['auth_key'] == settings.AUTH_KEY:
                try:
                    parent_rec = Userdata.objects.get(Usernumber=serializer.data['phone'])
                    print(parent_rec)
                    parent_exists = True
                except Exception as e:
                    print(e)
                    parent_exists = False
                if parent_exists is True:
                    try:
                        parent_rec = Userdata.objects.get(Usernumber=serializer.data['phone'])
                    except Exception as e:
                        print(e)
                        return JsonResponse({"INFO": "Please Contact Administration for Account activation."}, status=status.HTTP_200_OK)
                    if parent_rec.Is_action is True:
                        # if parent_rec.Response is None:
                        try:
                            if parent_rec.Is_parent is True:
                                parent_resp_id = parent_rec.Usernumber
                            else:
                                parent_resp_id = parent_rec.Createdby
                            room_resp = RGB.objects.filter(RGB_Parentid=parent_resp_id).values()
                            child_recs_serialised = RGBRoomSerializer(room_resp, many=True)
                            if child_recs_serialised.data.__len__() > 0:
                                data_set = '{"rooms":['
                                for length in range(child_recs_serialised.data.__len__()):
                                    t_data = child_recs_serialised.data[length]
                                    pub_data = json.loads(t_data['RGB_Publisheddata'])
                                    c_name = t_data['RGB_Devicecompanyname']
                                    d_name = t_data['RGB_Devicename']
                                    if serializer.data['phone'] == '919908799084':
                                        d_u_name = t_data['RGB_Devicecompanyname']
                                    else:
                                        d_u_name = t_data['RGB_Deviceusername']
                                    image_p = t_data['RGB_Imagepath']
                                    t_data = json.loads(t_data['RGB_Typed'])
                                    data_set = str(data_set) + '{"roomid":"' + str(d_name) + '","roomImg":"' + str(image_p) + '","name":"' + str(d_u_name) + '","Gcode":"' + str(c_name) + '",'
                                    for ll in range(len(pub_data)):
                                        data_set = str(data_set) + '"type":"' + str(t_data[ll]) + '","action":"' + str(pub_data[ll]) + '","pub":"' + str(parent_resp_id) + '/' + str(d_name) + 'G/Device/' + str(pub_data[ll]) + '","sub":"' + str(parent_resp_id) + '/' + str(d_name) + 'G/App/' + str(pub_data[ll]) + '"'
                                        if ll != len(pub_data)-1:
                                            data_set += ','
                                    data_set += '}'
                                    if length != child_recs_serialised.data.__len__()-1:
                                        data_set += ','
                                data_set += ']}'
                            else:
                                return JsonResponse({"INFO": "Please Contact Administration for Account activation."}, status=status.HTTP_200_OK)
                            data_set = json.loads(data_set)
                        except Exception as e:
                            return JsonResponse({"INFO": "Please check the Auth-Key provided." + str(e)}, status=status.HTTP_400_BAD_REQUEST)
                        if parent_rec.Room_Permission == 'null':
                            try2 = 'false'
                        else:
                            try2 = 'true'
                        if parent_rec.Rgb_Permission == 'null':
                            try3 = 'false'
                        else:
                            try3 = 'true'
                        return JsonResponse({"rooms_info_available": try2, "rgb_info_available": try3, "IP": settings.IP, "PORT": settings.IP_PORT, "key1": parent_rec.Key1, "key2": parent_rec.Key2, "Apnd": settings.ENCRPT, "scheduling": settings.MQTT_SCHEDULING, "grouping": settings.MQTT_GROUPING, "skd": settings.SKD, "time": settings.TIME, "all_on": settings.ALL_ON, "all_off": settings.ALL_OFF, "timer": settings.MQTT_TIMER, "is_parent": parent_rec.Is_parent, "rgb_permissions": parent_rec.Rgb_Permission, "user_info": {"name": parent_rec.Username, "number": parent_rec.Usernumber, "email": parent_rec.Useremail, "prfimg": parent_rec.ProfileImg, "backimg": parent_rec.BacgroundImg}, "rooms_info": data_set}, status=status.HTTP_200_OK)
                        # else:
                        #     return JsonResponse({"rooms_info_available": True, "IP": settings.IP, "PORT": settings.IP_PORT, "key1": parent_rec.Key1, "key2": parent_rec.Key2, "Apnd": settings.ENCRPT, "scheduling": settings.MQTT_SCHEDULING, "grouping": settings.MQTT_GROUPING, "skd": settings.SKD, "time": settings.TIME, "all_on": settings.ALL_ON, "all_off": settings.ALL_OFF, "timer": settings.MQTT_TIMER, "is_parent": parent_rec.Is_parent,
                        #                          "room_permissions": parent_rec.Room_Permission, "user_info": {"name": parent_rec.Username, "number": parent_rec.Usernumber, "email": parent_rec.Useremail, "prfimg": parent_rec.ProfileImg, "backimg": parent_rec.BacgroundImg}, "rooms_info": "NULL"}, status=status.HTTP_200_OK)
                    else:
                        return JsonResponse({"INFO": "Please Contact Administration for Account activation."}, status=status.HTTP_200_OK)
                else:
                    return JsonResponse({"INFO": "No User exists with this Phone Number."}, status=status.HTTP_400_BAD_REQUEST)
            else:
                print(serializer.data['auth_key'])
                return JsonResponse({"INFO": "Please check the Auth-Key provided."}, status=status.HTTP_400_BAD_REQUEST)


class RGBNewRoomsInfo(APIView):
    permission_classes = [AllowAny]
    authentication_classes = (CsrfExemptSessionAuthentication, BasicAuthentication)

    # noinspection PyMethodMayBeStatic
    def post(self, request):
        serializer = RGBRoomsInfoSerializer(data=request.data, context={'request': request})
        if not serializer.is_valid():
            data = {"INFO": serializer.errors}
            return JsonResponse(data, status=status.HTTP_400_BAD_REQUEST)
        else:
            if serializer.data['auth_key'] == settings.AUTH_KEY:
                try:
                    parent_recognition = Userdata.objects.get(Usernumber=serializer.data['phone'])
                    print(parent_recognition)
                    account_exists = True
                except Exception as e:
                    print(e)
                    account_exists = False
                if account_exists is True:
                    parent_rec = Userdata.objects.get(Usernumber=serializer.data['phone'])
                    if parent_rec.Is_action is True:
                        try:
                            data_set = '{"rooms":['
                            if parent_rec.Is_parent is True:
                                parent_resp_id = parent_rec.Usernumber
                                room_resp = RGB.objects.filter(RGB_Parentid=parent_resp_id).values()
                                child_recs_serialised = RGBRoomSerializer(room_resp, many=True)
                                for length in range(child_recs_serialised.data.__len__()):
                                    t_data = child_recs_serialised.data[length]
                                    pubdata = json.loads(t_data['RGB_Publisheddata'])
                                    c_name = t_data['RGB_Devicecompanyname']
                                    d_name = t_data['RGB_Devicename']
                                    if serializer.data['phone'] == '919908799084':
                                        d_u_name = t_data['RGB_Devicecompanyname']
                                    else:
                                        d_u_name = t_data['RGB_Deviceusername']
                                    data_set = str(data_set) + '{"roomid":"' + str(d_name) + '","name":"' + str(d_u_name) + '","roomImg":"' + str(t_data['RGB_Imagepath']) + '",'
                                    t_data = json.loads(t_data['RGB_Typed'])
                                    for ll in range(len(pubdata)):
                                        data_set = str(data_set) + '"type":"' + str(t_data[ll]) + '","index":"' + str(ll) + '","Gcode":"' + str(c_name) + '","Company_name":"' + str(d_name) + '","action":"' + str(pubdata[ll]) + '","pub":"' + str(parent_resp_id) + '/' + str(d_name) + 'G/Device/' + str(pubdata[ll]) + '","sub":"' + str(parent_resp_id)+'/' + str(d_name) + 'G/App/' + str(pubdata[ll]) + '"'
                                        if ll != len(pubdata)-1:
                                            data_set += ','
                                    data_set += '}'
                                    if length != child_recs_serialised.data.__len__()-1:
                                        data_set += ','
                                data_set += ']}'
                                data_set = json.loads(data_set)
                            elif parent_rec.Is_parent is False:
                                parent_resp_id = parent_rec.Createdby
                                room_access = parent_rec.Rgb_Permission
                                fail = str(room_access).replace(' ', '').replace(',', '\',\'').replace('[', '[\'').replace(']', '\']')
                                if fail != 'null':
                                    final_dictionary = eval(fail)
                                    data_set = '{"rooms":['
                                    for length in range(len(final_dictionary)):
                                        device_records = RGB.objects.filter(RGB_Devicename=final_dictionary[length])
                                        check = device_records[0]
                                        dname = check.RGB_Devicename
                                        duname = check.RGB_Deviceusername
                                        pubdata = check.RGB_Publisheddata
                                        company_name = check.RGB_Devicecompanyname
                                        pubdata = eval(pubdata)
                                        tdata = check.RGB_Typed
                                        tdata = eval(tdata)
                                        data_set = str(data_set) + '{"roomid":"' + str(dname) + '","name":"' + str(duname) + '","roomImg":"' + str(check.RGB_Imagepath) + '",'
                                        for ll in range(len(pubdata)):
                                            data_set = str(data_set) + '"type":"' + str(tdata[ll]) + '","index":"' + str(ll) + '","Gcode":"' + str(company_name) + '","Company_name":"' + str(dname) + '","action":"' + str(pubdata[ll]) + '","pub":"' + str(parent_resp_id) + '/' + str(dname) + 'G/Device/' + str(pubdata[ll]) + '","sub":"' + str(parent_resp_id) + '/' + str(dname) + 'G/App/' + str(pubdata[ll]) + '"'
                                            if ll != len(pubdata) - 1:
                                                data_set += ','
                                        data_set += '}'
                                        if length != len(final_dictionary) - 1:
                                            data_set += ','
                                    data_set += ']}'
                                    data_set = json.loads(data_set)
                                else:
                                    data_set = '{"rooms":["null"]}'
                                    data_set = json.loads(data_set)
                            if parent_rec.Room_Permission == 'null':
                                try2 = 'false'
                            else:
                                try2 = 'true'
                            if parent_rec.Rgb_Permission == 'null':
                                try3 = 'false'
                            else:
                                try3 = 'true'
                            return JsonResponse({"rooms_info_available": try2, "rgb_info_available": try3, "IP": settings.IP, "PORT": settings.IP_PORT, "key1": parent_rec.Key1, "key2": parent_rec.Key2, "Apnd": settings.ENCRPT, "scheduling": settings.MQTT_SCHEDULING, "grouping": settings.MQTT_GROUPING, "skd": settings.SKD, "time": settings.TIME, "all_on": settings.ALL_ON, "all_off": settings.ALL_OFF, "timer": settings.MQTT_TIMER, "is_parent": parent_rec.Is_parent, "rgb_permissions": parent_rec.Rgb_Permission, "user_info": {"name": parent_rec.Username, "number": parent_rec.Usernumber, "email": parent_rec.Useremail, "prfimg": parent_rec.ProfileImg, "backimg": parent_rec.BacgroundImg}, "rooms_info": data_set}, status=status.HTTP_200_OK)
                        except Exception as e:
                            print(e)
                            return JsonResponse({"INFO": e}, status=status.HTTP_400_BAD_REQUEST)
                        #        return JsonResponse({"rooms_info_available": try2, "rgb_rooms_info_available": try3, "IP": settings.IP, "PORT": settings.IP_PORT, "Field": parent_rec.Unknownfield, "key1": parent_rec.Key1, "key2": parent_rec.Key2, "Apnd": settings.ENCRPT, "scheduling": settings.MQTT_SCHEDULING, "grouping": settings.MQTT_GROUPING, "skd": settings.SKD, "time": settings.TIME, "all_on": settings.ALL_ON, "all_off": settings.ALL_OFF, "timer": settings.MQTT_TIMER, "is_parent": parent_rec.Is_parent, "room_permissions": parent_rec.Room_Permission, "rgb_room_permissions": parent_rec.Rgb_Permission, "user_info": {"name": parent_rec.Username, "number": parent_rec.Usernumber, "email": parent_rec.Useremail, "prfimg": parent_rec.ProfileImg, "backimg": parent_rec.BacgroundImg}, "rooms_info": res_data3, "Remote": ir_data}, status=status.HTTP_200_OK)
                    else:
                        return JsonResponse({"INFO": "Please Contact Administration for Account activation."}, status=status.HTTP_200_OK)
                else:
                    return JsonResponse({"INFO": "No User exists with this Phone Number."}, status=status.HTTP_400_BAD_REQUEST)
            else:
                return JsonResponse({"INFO": "Please check the Auth-Key provided."}, status=status.HTTP_400_BAD_REQUEST)

 # Checking