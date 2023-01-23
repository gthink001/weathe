from django.db import models
from jsonfield import JSONField


class Device(models.Model):
    Devicename = models.CharField(primary_key=True, unique=True, max_length=255, blank=True)
    Parentid = models.CharField(max_length=342, blank=True, null=True)
    IsActive = models.BooleanField(max_length=45, blank=True)
    Requestcount = models.IntegerField(default=0, blank=True, null=True)
    Lastrequested = models.DateTimeField(blank=True, null=True)
    Publisheddata = models.CharField(max_length=342, blank=True, null=True)
    Typed = models.CharField(max_length=345, blank=True, null=True)
    Devicenumber = models.IntegerField(default=0, blank=True, null=True)
    Deviceusername = models.CharField(max_length=87, blank=True, null=True)
    Devicecompanyname = models.CharField(unique=True, max_length=346, blank=True, null=True)
    Namer = models.CharField(max_length=176, blank=True, null=True)
    Imagepath = models.CharField(max_length=256, blank=True, null=True)
    Work = models.CharField(max_length=176, blank=True, null=True)
    type = models.CharField(max_length=176, blank=True, null=True)
    Notification_State = models.CharField(max_length=256, blank=True, null=True)
    Heavy_State = models.CharField(max_length=256, blank=True, null=True)
    Heavy_Time = models.CharField(max_length=256, blank=True, null=True)
    Notification_Time = models.CharField(max_length=256, blank=True, null=True)
    Assigned_State = models.CharField(max_length=256, blank=True, null=True)
    Device_State = models.CharField(max_length=256, blank=True, null=True)
    Device_Icon = models.CharField(max_length=2256, default='["https://gthink-images-website.s3.ap-south-1.amazonaws.com/svg/bulb01.svg","https://gthink-images-website.s3.ap-south-1.amazonaws.com/svg/bulb01.svg","https://gthink-images-website.s3.ap-south-1.amazonaws.com/svg/bulb01.svg","https://gthink-images-website.s3.ap-south-1.amazonaws.com/svg/bulb01.svg","https://gthink-images-website.s3.ap-south-1.amazonaws.com/svg/bulb01.svg","https://gthink-images-website.s3.ap-south-1.amazonaws.com/svg/bulb01.svg","https://gthink-images-website.s3.ap-south-1.amazonaws.com/svg/bulb01.svg","https://gthink-images-website.s3.ap-south-1.amazonaws.com/svg/bulb01.svg"]', blank=True, null=True)
    objects = models.Manager()


class Enquiry(models.Model):
    Customer_Name = models.CharField(primary_key=True, unique=True, max_length=255, blank=True)
    Customer_Number = models.CharField(max_length=12, blank=True, null=True)
    Customer_requirement = models.CharField(max_length=1100, blank=True, null=True)
    objects = models.Manager()


class DealerDevice(models.Model):
    DeviceName = models.CharField(primary_key=True, unique=True, max_length=255, blank=True)
    DealerId = models.CharField(max_length=342, blank=True, null=True)
    objects = models.Manager()


class DealerUsers(models.Model):
    D_user = models.CharField(primary_key=True, unique=True, max_length=255, blank=True)
    DealerId = models.CharField(max_length=342, blank=True, null=True)
    objects = models.Manager()


class TouchCloneDevice(models.Model):
    DeviceName = models.CharField(primary_key=True, unique=True, max_length=255, blank=True)
    ParentId = models.CharField(max_length=342, blank=True, null=True)
    IsActive = models.BooleanField(max_length=45, blank=True)
    RequestCount = models.IntegerField(default=0, blank=True, null=True)
    LastRequested = models.DateTimeField(blank=True, null=True)
    DeviceNumber = models.IntegerField(default=0, blank=True, null=True)
    DeviceCompanyName = models.CharField(unique=True, max_length=346, blank=True, null=True)
    ParentDevice = models.CharField(max_length=342, blank=True, null=True)
    objects = models.Manager()


class SemiCloneDevice(models.Model):
    DeviceName = models.CharField(primary_key=True, unique=True, max_length=255, blank=True)
    ParentId = models.CharField(max_length=342, blank=True, null=True)
    Publisheddata = models.CharField(max_length=342, blank=True, null=True)
    RequestCount = models.IntegerField(default=0, blank=True, null=True)
    LastRequested = models.DateTimeField(blank=True, null=True)
    DeviceNumber = models.IntegerField(default=0, blank=True, null=True)
    DeviceCompanyName = models.CharField(unique=True, max_length=346, blank=True, null=True)
    ActionDevice = models.CharField(max_length=342, blank=True, null=True)
    objects = models.Manager()


class IRDevice(models.Model):
    DeviceName = models.CharField(primary_key=True, unique=True, max_length=255, blank=True)
    ParentId = models.CharField(max_length=342, blank=True, null=True)
    LastRequested = models.DateTimeField(blank=True, null=True)
    PublishedData = models.CharField(max_length=342, blank=True, null=True)
    DeviceCompanyName = models.CharField(unique=True, max_length=346, blank=True, null=True)
    Assigned_State = models.CharField(max_length=256, blank=True, null=True)
    rooms = models.TextField(blank=True, null=True)
    objects = models.Manager()


class IRRoomInfo(models.Model):
    Response = models.TextField(blank=True, null=True)
    ImagePath = models.TextField(blank=True, null=True)
    NamePath = models.TextField(blank=True, null=True)
    UserNumber = models.CharField(max_length=13)
    DeviceId = models.TextField(blank=True, null=True)
    PubData = models.TextField(blank=True, null=True)
    SubData = models.TextField(blank=True, null=True)
    IRType = models.TextField(max_length=56)
    objects = models.Manager()


class IRButtonInfo(models.Model):
    company_name_id = models.TextField(blank=True, null=True)
    product_name_id = models.TextField(blank=True, null=True)
    brand_name = models.CharField(max_length=56)
    IRType = models.TextField(max_length=56)
    protocol = models.CharField(max_length=56)
    repeat_count = models.CharField(max_length=3)
    button1 = models.TextField(blank=True, null=True)
    button2 = models.TextField(blank=True, null=True)
    button3 = models.TextField(blank=True, null=True)
    button4 = models.TextField(blank=True, null=True)
    button5 = models.TextField(blank=True, null=True)
    button6 = models.TextField(blank=True, null=True)
    button7 = models.TextField(blank=True, null=True)
    button8 = models.TextField(blank=True, null=True)
    button9 = models.TextField(blank=True, null=True)
    button10 = models.TextField(blank=True, null=True)
    button11 = models.TextField(blank=True, null=True)
    button12 = models.TextField(blank=True, null=True)
    button13 = models.TextField(blank=True, null=True)
    button14 = models.TextField(blank=True, null=True)
    button15 = models.TextField(blank=True, null=True)
    button16 = models.TextField(blank=True, null=True)
    button17 = models.TextField(blank=True, null=True)
    button18 = models.TextField(blank=True, null=True)
    button19 = models.TextField(blank=True, null=True)
    button20 = models.TextField(blank=True, null=True)
    button21 = models.TextField(blank=True, null=True)
    button22 = models.TextField(blank=True, null=True)
    button23 = models.TextField(blank=True, null=True)
    button24 = models.TextField(blank=True, null=True)
    button25 = models.TextField(blank=True, null=True)
    objects = models.Manager()


class RGB(models.Model):
    RGB_Devicename = models.CharField(primary_key=True, unique=True, max_length=255, blank=True)
    RGB_Parentid = models.CharField(max_length=342, blank=True, null=True)
    RGB_IsActive = models.BooleanField(max_length=45, blank=True)
    RGB_Requestcount = models.IntegerField(default=0, blank=True, null=True)
    RGB_Lastrequested = models.DateTimeField(blank=True, null=True)
    RGB_Publisheddata = models.CharField(max_length=342, blank=True, null=True)
    RGB_Devicedata = models.CharField(max_length=67, blank=True, null=True)
    RGB_Deviceusername = models.CharField(max_length=87, blank=True, null=True)
    RGB_Devicecompanyname = models.CharField(unique=True, max_length=346, blank=True, null=True)
    # RGB_Namer = models.CharField(max_length=76, blank=True, null=True)
    RGB_Imagepath = models.CharField(max_length=76, blank=True, null=True)
    RGB_Typed = models.CharField(max_length=76, blank=True, null=True)
    objects = models.Manager()


class Curtain(models.Model):
    Devicename = models.CharField(primary_key=True, unique=True, max_length=255, blank=True)
    Parentid = models.CharField(max_length=342, blank=True, null=True)
    IsActive = models.BooleanField(max_length=45, blank=True)
    Requestcount = models.IntegerField(default=0, blank=True, null=True)
    Lastrequested = models.DateTimeField(blank=True, null=True)
    Publisheddata = models.CharField(max_length=342, blank=True, null=True)
    Typed = models.CharField(max_length=345, blank=True, null=True)
    Recorddata = models.CharField(max_length=345, blank=True, null=True)
    Deviceparent = models.CharField(max_length=234, blank=True, null=True)
    Devicenumber = models.IntegerField(default=0, blank=True, null=True)
    Devicedata = models.CharField(max_length=67, blank=True, null=True)
    Deviceusername = models.CharField(max_length=87, blank=True, null=True)
    Devicecompanyname = models.CharField(unique=True, max_length=346, blank=True, null=True)
    Namer = models.CharField(max_length=76, blank=True, null=True)
    Imagepath = models.CharField(max_length=76, blank=True, null=True)
    Work = models.CharField(max_length=76, blank=True, null=True)
    type = models.CharField(max_length=76, blank=True, null=True)
    objects = models.Manager()


class Scheduling(models.Model):
    Devicename = models.CharField(max_length=67)
    Action = models.CharField(max_length=254)
    Times = models.CharField(max_length=254, blank=True, null=True)
    Timestamp = models.DateTimeField(blank=True, null=True)
    objects = models.Manager()


class Userdata(models.Model):
    Usernumber = models.CharField(primary_key=True, unique=True, max_length=13)
    Username = models.CharField(max_length=45, blank=True, null=True)
    Useremail = models.EmailField(max_length=89, blank=True, null=True)
    Createdby = models.CharField(max_length=87, blank=True, null=True)
    Userdeviceid = models.CharField(max_length=56, blank=True, null=True)
    Is_authenticated = models.BooleanField(max_length=78, blank=True, null=True)
    Is_action = models.BooleanField(max_length=87, blank=True, null=True)
    Is_parent = models.BooleanField(max_length=78, blank=True, null=True)
    Room_Permission = models.CharField(max_length=956, blank=True, null=True)
    Rgb_Permission = models.CharField(max_length=956, blank=True, null=True)
    IR_Permission = models.CharField(max_length=956, blank=True, null=True)
    Key1 = models.CharField(max_length=34, blank=True, null=True)
    Key2 = models.CharField(max_length=87, blank=True, null=True)
    Unknownfield = models.CharField(max_length=256, blank=True, null=True)
    BacgroundImg = models.CharField(max_length=256, blank=True, null=True)
    ProfileImg = models.CharField(max_length=256, blank=True, null=True)
    Response = models.TextField(blank=True, null=True)
    Notification_Token = models.CharField(max_length=256, blank=True, null=True)
    # Second_House = models.CharField(max_length=256, blank=True, null=True)
    Response_Data = JSONField(blank=True, null=True)
    objects = models.Manager()


class UserRoomInfo(models.Model):
    Response = models.TextField(blank=True, null=True)
    ImagePath = models.TextField(blank=True, null=True)
    NamePath = models.TextField(blank=True, null=True)
    UserNumber = models.CharField(max_length=13)
    objects = models.Manager()