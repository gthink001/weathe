from .models import *
from rest_framework import serializers


class ActionSerializer(serializers.Serializer):
    # {pub=4, key1=gsmart, key2=4, ip=G-THINK, port=8}
    pub = serializers.CharField(max_length=18, min_length=1, required=True)
    key1 = serializers.CharField(max_length=14, min_length=1, required=True)
    key2 = serializers.CharField(max_length=10, min_length=1, required=True)
    action = serializers.CharField(max_length=256, min_length=1, required=True)


class UsersupSerializer(serializers.Serializer):
    phone = serializers.CharField(max_length=18, min_length=1, required=True)
    name = serializers.CharField(max_length=256, min_length=1, required=False)
    email = serializers.EmailField(max_length=100, min_length=1, required=False)
    device_id = serializers.CharField(max_length=256, min_length=1, required=True)

    class Meta:
        model = Userdata
        fields = ['Username', 'Usernumber', 'Useremail', 'Userdeviceid', 'Is_authenticated']


class DeviceaddSerializer(serializers.Serializer):
    # {large_switch=4, device_name=gsmart, samll_switch=4, company_name=G-THINK, no_of_switches=8}
    fan = serializers.CharField(max_length=18, min_length=1, required=False)
    device_name = serializers.CharField(max_length=14, min_length=1, required=True)
    switches = serializers.CharField(max_length=10, min_length=1, required=True)
    company_name = serializers.CharField(max_length=256, min_length=1, required=True)
    total = serializers.CharField(max_length=256, min_length=1, required=True)
    type = serializers.CharField(max_length=256, min_length=1, required=True)
    # fan_count = serializers.CharField(max_length=256, min_length=1, required=True)


class OldDeviceAddFanSerializer(serializers.Serializer):
    # {large_switch=4, device_name=gsmart, samll_switch=4, company_name=G-THINK, no_of_switches=8}
    device_name = serializers.CharField(max_length=14, min_length=1, required=True)
    company_name = serializers.CharField(max_length=256, min_length=1, required=True)
    total = serializers.CharField(max_length=256, min_length=1, required=True)
    type = serializers.CharField(max_length=256, min_length=1, required=True)


class DeviceAddFanSerializer(serializers.Serializer):
    # {large_switch=4, device_name=gsmart, samll_switch=4, company_name=G-THINK, no_of_switches=8}
    device_name = serializers.CharField(max_length=14, min_length=1, required=True)
    company_name = serializers.CharField(max_length=256, min_length=1, required=True)
    total = serializers.CharField(max_length=256, min_length=1, required=True)
    type = serializers.CharField(max_length=256, min_length=1, required=True)


class DeviceaddfirstSerializer(serializers.Serializer):
    # {device_name=gsmart}
    device_name = serializers.CharField(max_length=14, min_length=1, required=True)


class MailSerializer(serializers.Serializer):
    # {device_name=gsmart}
    username = serializers.CharField(max_length=140, min_length=1, required=True)
    email = serializers.CharField(max_length=140, min_length=1, required=True)
    contact_message = serializers.CharField(max_length=1400, min_length=1, required=True)


class UnitsSerializer(serializers.Serializer):
    # {device_name=gsmart}
    unit = serializers.CharField(max_length=140, min_length=1, required=True)
    persons = serializers.CharField(max_length=140, min_length=1, required=True)
    square_area = serializers.CharField(max_length=140, min_length=1, required=True)


class ParentSerializer(serializers.ModelSerializer):

    phone = serializers.CharField(source='Usernumber')
    name = serializers.CharField(source='Username')
    email = serializers.EmailField(source='Useremail')
    device_id = serializers.CharField(source='Userdeviceid')
    created_by = serializers.CharField(source='Createdby')
    room_permissions = serializers.CharField(source='Room_Permission')
    rgb_permissions = serializers.CharField(source='Rgb_Permission')
    ir_permissions = serializers.CharField(source='IR_Permission')
    is_authorised = serializers.CharField(source='Is_authenticated')
    is_activated = serializers.CharField(source='Is_action')
    is_parent = serializers.CharField(source='Is_parent')
    mqtt_key_1 = serializers.CharField(source='Key1')
    mqtt_key_2 = serializers.CharField(source='Key2')

    class Meta:
        model = Userdata
        fields = ('phone', 'name', 'email', 'device_id', 'created_by', 'room_permissions', 'rgb_permissions', 'ir_permissions', 'is_authorised', 'is_activated', 'is_parent', 'mqtt_key_1', 'mqtt_key_2')


class OtpSerializer(serializers.Serializer):
    phone = serializers.CharField(max_length=18, min_length=1, required=True)
    otp = serializers.CharField(max_length=4, min_length=1, required=True)
    req_type = serializers.CharField(max_length=13, min_length=1, required=True)
    device_id = serializers.CharField(max_length=256, min_length=1, required=True)


class SendOTPSerializer2(serializers.Serializer):

    phone = serializers.CharField(max_length=18, min_length=1, required=True)


class SendOTPSerializer(serializers.Serializer):

    phone = serializers.CharField(max_length=18, min_length=1, required=True)
    email = serializers.EmailField(max_length=100, min_length=1, required=False)
    req_type = serializers.CharField(max_length=13, min_length=1, required=True)


class DeleteUserSerializer(serializers.Serializer):
    phone = serializers.CharField(max_length=18, min_length=1, required=True)
    auth_key = serializers.CharField(max_length=256, min_length=1, required=True)


class UpdateParentSerializer(serializers.Serializer):
    auth_key = serializers.CharField(max_length=256, min_length=1, required=True)
    user_id = serializers.CharField(max_length=13, min_length=1, required=True)
    email = serializers.CharField(required=False)
    name = serializers.CharField(required=False)


class ChildSignupSerializer(serializers.Serializer):
    phone = serializers.CharField(max_length=18, min_length=1, required=True)
    name = serializers.CharField(max_length=256, min_length=1, required=True)
    email = serializers.EmailField(max_length=100, min_length=1, required=True)
    parent_id = serializers.CharField(max_length=12, min_length=1, required=True)
    rooms = serializers.CharField(min_length=1, required=True)
    rgb_rooms = serializers.CharField(min_length=1, required=False)


class GetChildListSerializer(serializers.Serializer):
    parent_id = serializers.CharField(max_length=13, min_length=1, required=True)


class DeleteChildSerializer(serializers.Serializer):
    child_id = serializers.CharField(max_length=13, min_length=1, required=True)


class UpdateChildSerializer(serializers.Serializer):
    child_id = serializers.CharField(max_length=13, min_length=1, required=True)
    rooms = serializers.CharField(min_length=1, required=True)
    rgb_rooms = serializers.CharField(min_length=1, required=False)


class UpdateResponseSerializer(serializers.Serializer):
    number = serializers.CharField(max_length=13, min_length=1, required=True)
    response = serializers.CharField(required=True)


class ChangeRoomResponseSerializer(serializers.Serializer):
    id = serializers.CharField(max_length=13, min_length=1, required=True)
    response = serializers.CharField(required=True)


class IRDeviceListSerializer(serializers.Serializer):

    class Meta:
        model = IRButtonInfo
        fields = ('product_name_id', 'brand_name', 'protocol', 'repeat_count')


class UpdateIRButtonSerializer(serializers.Serializer):
    product_name_id = serializers.CharField(min_length=1, required=True)
    brand_name = serializers.CharField(min_length=1, required=True)
    protocol = serializers.CharField(min_length=1, required=True)
    repeat_count = serializers.CharField(min_length=1, required=True)
    bits = serializers.CharField(min_length=1, required=True)
    size = serializers.CharField(min_length=1, required=True)
    button1 = serializers.CharField(min_length=1, required=True)
    button2 = serializers.CharField(min_length=1, required=True)
    button3 = serializers.CharField(required=False)
    button4 = serializers.CharField(required=False)
    button5 = serializers.CharField(required=False)
    button6 = serializers.CharField(required=False)
    button7 = serializers.CharField(required=False)
    button8 = serializers.CharField(required=False)
    button9 = serializers.CharField(required=False)
    button10 = serializers.CharField(required=False)
    button11 = serializers.CharField(required=False)
    button12 = serializers.CharField(required=False)
    button13 = serializers.CharField(required=False)
    button14 = serializers.CharField(required=False)
    button15 = serializers.CharField(required=False)
    button16 = serializers.CharField(required=False)
    button17 = serializers.CharField(required=False)
    button18 = serializers.CharField(required=False)
    button19 = serializers.CharField(required=False)
    button20 = serializers.CharField(required=False)
    button21 = serializers.CharField(required=False)
    button22 = serializers.CharField(required=False)
    button23 = serializers.CharField(required=False)
    button24 = serializers.CharField(required=False)
    button25 = serializers.CharField(required=False)


class NewUpdateChildSerializer(serializers.Serializer):
    child_id = serializers.CharField(max_length=13, min_length=1, required=True)
    rooms = serializers.CharField(min_length=1, required=True)
    action = serializers.CharField(min_length=1, required=True)
    rgb_rooms = serializers.CharField(min_length=1, required=False)


class ScheduleDeviceSerializer(serializers.Serializer):
    device_id = serializers.CharField(required=True)
    action = serializers.CharField(required=True)
    fire_date = serializers.DateTimeField(required=True)
    auth_key = serializers.CharField(max_length=256, min_length=1, required=True)


class DeleteScheduleSerializer(serializers.Serializer):
    device_id = serializers.CharField(required=True)
    action = serializers.CharField(required=True)
    fire_date = serializers.DateTimeField(required=True)


class DeleteScheduleDeviceSerializer(serializers.Serializer):
    device_id = serializers.CharField(required=True)
    id = serializers.CharField(required=True)


class DeviceSerializer(serializers.Serializer):
    device_id = serializers.CharField(required=True)


class DealerInfoSerializer(serializers.Serializer):
    device_id = serializers.CharField(required=True)
    mobile = serializers.CharField(required=True)


class AssignToDealerSerializer(serializers.Serializer):
    dealer_number = serializers.CharField(required=True)
    dealer_id = serializers.CharField(required=True)
    dealer_state = serializers.CharField(required=True)


class DealerAssignToCustomerSerializer(serializers.Serializer):
    customer_number = serializers.CharField(required=True)
    dealer_number = serializers.CharField(required=True)
    dealer_id = serializers.CharField(required=True)
    dealer_state = serializers.CharField(required=True)


class DealerDeviceSerializer(serializers.ModelSerializer):
    a = serializers.CharField(source='Action')
    t = serializers.CharField(source='Times')
    id = serializers.ReadOnlyField()

    class Meta:
        model = Scheduling
        fields = ('a', 't', 'id')


class AlexaDeviceSerializer(serializers.Serializer):
    device_id = serializers.CharField(required=True)
    switch_state = serializers.CharField(required=True)


class UpdateprofileimgSerializer(serializers.Serializer):
    device_id = serializers.CharField(required=True)
    pimg = serializers.CharField(min_length=1, required=True)


class UpdateiconnameSerializer(serializers.Serializer):
    device_id = serializers.CharField(required=True)
    iconname = serializers.CharField(min_length=1, required=True)


class FcmSerializer(serializers.Serializer):
    device_id = serializers.CharField(required=True)
    mobile_id = serializers.CharField(required=True)
    switch_id = serializers.CharField(required=True)
    state = serializers.CharField(required=True)


class GoogleSerializer(serializers.Serializer):
    device_id = serializers.CharField(required=True)
    mobile_id = serializers.CharField(required=True)
    switch_id = serializers.CharField(required=True)
    state = serializers.CharField(required=True)


class StateSerializer(serializers.Serializer):
    device_id = serializers.CharField(required=True)
    switch_id = serializers.CharField(required=True)
    switch_state = serializers.CharField(required=True)


class GetStateSerializer(serializers.Serializer):
    device_id = serializers.CharField(required=True)
    switch_id = serializers.CharField(required=True)


class UpdateNotificationStatusSerializer(serializers.Serializer):
    code = serializers.CharField(required=True)
    notification_name = serializers.CharField(min_length=1, required=True)
    index = serializers.CharField(min_length=1, required=True)


class DeregisterFromRoomSerializer(serializers.Serializer):
    id = serializers.CharField(required=True)


class GETNotificationStatusSerializer(serializers.Serializer):
    code = serializers.CharField(required=True)
    index = serializers.CharField(min_length=1, required=True)


class HeavySerializer(serializers.Serializer):
    device_id = serializers.CharField(required=True)
    heavy_name = serializers.CharField(min_length=1, required=True)


class UpdateHeavyTimeStatusSerializer(serializers.Serializer):
    device_id = serializers.CharField(required=True)
    heavy_time = serializers.CharField(min_length=1, required=True)


class UpdateNotificationTimeStatusSerializer(serializers.Serializer):
    code = serializers.CharField(required=True)
    notification_time = serializers.CharField(min_length=1, required=True)
    index = serializers.CharField(min_length=1, required=True)


class InstallTeamSerializer(serializers.Serializer):
    device_id = serializers.CharField(required=True)
    inteam = serializers.CharField(min_length=1, required=True)


class UpdateroomnameSerializer(serializers.Serializer):
    device_id = serializers.CharField(required=True)
    roomname = serializers.CharField(min_length=1, required=True)


class UpdateRoomStateSerializer(serializers.Serializer):
    device_id = serializers.CharField(required=True)
    room_state = serializers.CharField(min_length=1, required=True)
    index = serializers.CharField(min_length=1, required=True)


class UpdateRoomImageNameSerializer(serializers.Serializer):
    room_id = serializers.CharField(required=True)
    room_image = serializers.CharField(min_length=1, required=True)


class UpdateRoomMainNameSerializer(serializers.Serializer):
    room_id = serializers.CharField(required=True)
    room_name = serializers.CharField(min_length=1, required=True)


class ChangeApplianceNameSerializer(serializers.Serializer):
    room_id = serializers.CharField(required=True)
    icon_name = serializers.CharField(min_length=1, required=True)
    code = serializers.CharField(min_length=1, required=True)
    index = serializers.CharField(min_length=1, required=True)


class ChangeApplianceTypeSerializer(serializers.Serializer):
    code = serializers.CharField(required=True)
    type = serializers.CharField(min_length=1, required=True)
    index = serializers.CharField(min_length=1, required=True)


class ChangeRoomNameNewSerializer(serializers.Serializer):
    room_id = serializers.CharField(required=True)
    room_name = serializers.CharField(min_length=1, required=True)


class ChangeRoomImageNameNewSerializer(serializers.Serializer):
    room_id = serializers.CharField(required=True)
    room_image = serializers.CharField(min_length=1, required=True)


class UpdateBackImgSerializer(serializers.Serializer):
    device_id = serializers.CharField(required=True)
    bimg = serializers.CharField(min_length=1, required=True)


class UpdateRoomImgSerializer(serializers.Serializer):
    device_id = serializers.CharField(required=True)
    rimg = serializers.CharField(min_length=1, required=True)


class DeviceSchedulingSerializer(serializers.ModelSerializer):
    a = serializers.CharField(source='Action')
    t = serializers.CharField(source='Times')
    id = serializers.ReadOnlyField()

    class Meta:
        model = Scheduling
        fields = ('a', 't', 'id')


class UserRoomInfoListSerializer(serializers.ModelSerializer):
    roomd = serializers.CharField(source='Response')
    roomImg = serializers.CharField(source='ImagePath')
    name = serializers.CharField(source='NamePath')
    roomid = serializers.CharField(source='id')

    class Meta:
        model = UserRoomInfo
        fields = ('roomid', 'roomImg', 'name', 'roomd')


class UpdateIRChildSerializer(serializers.Serializer):
    child_id = serializers.CharField(max_length=13, min_length=1, required=True)
    rooms = serializers.CharField(min_length=1, required=True)


class IRRoomInfoListSerializer(serializers.ModelSerializer):
    room_data = serializers.CharField(source='Response')
    roomImg = serializers.CharField(source='ImagePath')
    name = serializers.CharField(source='NamePath')
    roomId = serializers.CharField(source='id')
    Device_Id = serializers.CharField(source='DeviceId')
    Pub_Data = serializers.CharField(source='PubData')
    Sub_Data = serializers.CharField(source='SubData')
    IR_Type = serializers.CharField(source='IRType')

    class Meta:
        model = IRRoomInfo
        fields = ('roomId', 'roomImg', 'name', 'room_data', 'Pub_Data', 'Device_Id', 'Sub_Data', 'IR_Type')


class IRDeviceDataListSerializer(serializers.Serializer):
    auth_key = serializers.CharField(required=True)
    phone = serializers.CharField(max_length=18, min_length=1, required=True)


class IRDeviceDataListResponseSerializer(serializers.ModelSerializer):

    class Meta:
        model = IRDevice
        fields = ('DeviceName', 'ParentId', 'PublishedData', 'DeviceCompanyName', 'Assigned_State', 'rooms')


class DeviceSchedulingSerializerApps(serializers.ModelSerializer):
    a = serializers.CharField(source='Action')
    t = serializers.CharField(source='Timestamp')

    class Meta:
        model = Scheduling
        fields = ('a', 't')


class KeySerializer(serializers.Serializer):
    auth_key = serializers.CharField(max_length=256, min_length=1, required=True)


class AlexaLoginSerializer(serializers.Serializer):
    client_id = serializers.CharField(max_length=180, min_length=1, required=True)
    response_type = serializers.CharField(max_length=256, min_length=1, required=True)
    scope = serializers.CharField(max_length=256, min_length=1, required=True)
    redirect_uri = serializers.CharField(max_length=256, min_length=1, required=True)


class RoomsInfoSerializer(serializers.Serializer):
    phone = serializers.CharField(max_length=18, min_length=1, required=True)
    auth_key = serializers.CharField(max_length=256, min_length=1, required=True)


class CreateRoomSerializer(serializers.Serializer):
    response = serializers.CharField(min_length=1, required=True)
    image_path = serializers.CharField(max_length=180, min_length=1, required=True)
    name = serializers.CharField(max_length=80, min_length=1, required=True)
    phone = serializers.CharField(max_length=18, min_length=1, required=True)
    auth_key = serializers.CharField(max_length=256, min_length=1, required=True)


class CreateIRRoomSerializer(serializers.Serializer):
    response = serializers.CharField(min_length=1, required=True)
    image_path = serializers.CharField(max_length=180, min_length=1, required=True)
    name = serializers.CharField(max_length=80, min_length=1, required=True)
    phone = serializers.CharField(max_length=18, min_length=1, required=True)
    pub = serializers.CharField(max_length=18, min_length=1, required=True)
    sub = serializers.CharField(max_length=18, min_length=1, required=True)
    device_id = serializers.CharField(max_length=18, min_length=1, required=True)
    auth_key = serializers.CharField(max_length=256, min_length=1, required=True)


class DeleteRoomSerializer(serializers.Serializer):
    room_id = serializers.CharField(max_length=18, min_length=1, required=True)
    auth_key = serializers.CharField(max_length=256, min_length=1, required=True)


class DeviceInfoListSerializer(serializers.Serializer):
    phone = serializers.CharField(max_length=18, min_length=1, required=True)
    auth_key = serializers.CharField(max_length=256, min_length=1, required=True)


class IRDeviceInfoListSerializer(serializers.Serializer):
    auth_key = serializers.CharField(max_length=256, min_length=1, required=True)


class RoomSerializer(serializers.ModelSerializer):

    class Meta:
        model = Device
        fields = ('Devicename', 'Imagepath', 'Deviceusername', 'Publisheddata', 'Typed', 'Namer', 'Work', 'Devicecompanyname', 'Device_Icon')


class RoomDeviceInfoListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Device
        fields = ('Devicename', 'Assigned_State', 'Imagepath', 'Deviceusername', 'Publisheddata', 'Typed', 'Namer', 'Devicecompanyname')


class UserActivationSerializer(serializers.Serializer):
    phone = serializers.CharField(max_length=18, min_length=1, required=True)


class DUserActivationSerializer(serializers.Serializer):
    client_phone = serializers.CharField(max_length=18, min_length=1, required=True)
    dealer_id = serializers.CharField(max_length=18, min_length=1, required=True)


class GqrSerializer(serializers.Serializer):
    phone = serializers.CharField(max_length=18, min_length=1, required=True)
    device_no = serializers.CharField(max_length=256, min_length=1, required=True)


class DGqrSerializer(serializers.Serializer):
    client_phone = serializers.CharField(max_length=18, min_length=1, required=True)
    dealer_id = serializers.CharField(max_length=18, min_length=1, required=True)
    device_no = serializers.CharField(max_length=256, min_length=1, required=True)


class UpdateFcmTokenSerializer(serializers.Serializer):
    user_id = serializers.CharField(required=True)
    fcmtoken = serializers.CharField(min_length=1, required=True)


class CodeUpdateSerializer(serializers.Serializer):
    GCode = serializers.CharField(required=True)
    URL = serializers.CharField(min_length=1, required=True)


# RGB

class RGBqrSerializer(serializers.Serializer):
    phone = serializers.CharField(max_length=18, min_length=1, required=True)
    device_no = serializers.CharField(max_length=256, min_length=1, required=True)


class RGBUpdateroomnameSerializer(serializers.Serializer):
    device_id = serializers.CharField(required=True)
    roomname = serializers.CharField(min_length=1, required=True)


class RGBUpdateRoomImgSerializer(serializers.Serializer):
    device_id = serializers.CharField(required=True)
    rimg = serializers.CharField(min_length=1, required=True)


class RGBDeviceaddSerializer(serializers.Serializer):
    device_name = serializers.CharField(max_length=14, min_length=1, required=True)
    company_name = serializers.CharField(max_length=256, min_length=1, required=True)


class RGBDeviceaddfirstSerializer(serializers.Serializer):
    # {device_name=gsmart}
    device_name = serializers.CharField(max_length=14, min_length=1, required=True)


class RGBRoomsInfoSerializer(serializers.Serializer):
    phone = serializers.CharField(max_length=18, min_length=1, required=True)
    auth_key = serializers.CharField(max_length=256, min_length=1, required=True)


class RGBRoomSerializer(serializers.ModelSerializer):

    class Meta:
        model = RGB
        fields = ('RGB_Devicename', 'RGB_Imagepath', 'RGB_Deviceusername', 'RGB_Publisheddata', 'RGB_Typed', 'RGB_Devicecompanyname')


class RGBDeviceSerializer(serializers.Serializer):

    device_id = serializers.CharField(required=True)


# curtain


class CurtainaddSerializer(serializers.Serializer):
    # {large_switch=4, device_name=gsmart, samll_switch=4, company_name=G-THINK, no_of_switches=8}
    large_switch = serializers.CharField(max_length=18, min_length=1, required=True)
    device_name = serializers.CharField(max_length=14, min_length=1, required=True)
    samll_switch = serializers.CharField(max_length=10, min_length=1, required=True)
    company_name = serializers.CharField(max_length=256, min_length=1, required=True)
    no_of_switches = serializers.CharField(max_length=256, min_length=1, required=True)


class CurtainaddfirstSerializer(serializers.Serializer):
    # {device_name=gsmart}
    device_name = serializers.CharField(max_length=14, min_length=1, required=True)


class CurtainSerializer(serializers.Serializer):

    device_id = serializers.CharField(min_length=1, required=True)


class CurtainRoomSerializer(serializers.ModelSerializer):

    class Meta:
        model = Curtain
        fields = ('Devicename', 'Imagepath', 'Deviceusername', 'Publisheddata', 'Typed', 'Namer')


# Door


class DooraddSerializer(serializers.Serializer):
    # {large_switch=4, device_name=gsmart, samll_switch=4, company_name=G-THINK, no_of_switches=8}
    large_switch = serializers.CharField(max_length=18, min_length=1, required=True)
    device_name = serializers.CharField(max_length=14, min_length=1, required=True)
    samll_switch = serializers.CharField(max_length=10, min_length=1, required=True)
    company_name = serializers.CharField(max_length=256, min_length=1, required=True)
    no_of_switches = serializers.CharField(max_length=256, min_length=1, required=True)


class DooraddfirstSerializer(serializers.Serializer):
    # {device_name=gsmart}
    device_name = serializers.CharField(max_length=14, min_length=1, required=True)


class DoorSerializer(serializers.Serializer):

    device_id = serializers.CharField(required=True, min_length=1)


class DoorRoomSerializer(serializers.ModelSerializer):

    class Meta:
        model = Curtain
        fields = ('Devicename', 'Imagepath', 'Deviceusername', 'Publisheddata', 'Typed', 'Namer')


# Video


class VideoaddSerializer(serializers.Serializer):
    # {large_switch=4, device_name=gsmart, samll_switch=4, company_name=G-THINK, no_of_switches=8}
    large_switch = serializers.CharField(max_length=18, min_length=1, required=True)
    device_name = serializers.CharField(max_length=14, min_length=1, required=True)
    samll_switch = serializers.CharField(max_length=10, min_length=1, required=True)
    company_name = serializers.CharField(max_length=256, min_length=1, required=True)
    no_of_switches = serializers.CharField(max_length=256, min_length=1, required=True)


class VideoaddfirstSerializer(serializers.Serializer):
    # {device_name=gsmart}
    device_name = serializers.CharField(max_length=14, min_length=1, required=True)


class VideoSerializer(serializers.Serializer):

    device_id = serializers.CharField(required=True, min_length=1)


class VideoRoomSerializer(serializers.ModelSerializer):

    class Meta:
        model = Curtain
        fields = ('Devicename', 'Imagepath', 'Deviceusername', 'Publisheddata', 'Typed', 'Namer')


# Gate
#
#
# class GateaddSerializer(serializers.Serializer):
#     # {large_switch=4, device_name=gsmart, samll_switch=4, company_name=G-THINK, no_of_switches=8}
#     large_switch = serializers.CharField(max_length=18, min_length=1, required=True)
#     device_name = serializers.CharField(max_length=14, min_length=1, required=True)
#     samll_switch = serializers.CharField(max_length=10, min_length=1, required=True)
#     company_name = serializers.CharField(max_length=256, min_length=1, required=True)
#     no_of_switches = serializers.CharField(max_length=256, min_length=1, required=True)
#
#
# class GateaddfirstSerializer(serializers.Serializer):
#     # {device_name=gsmart}
#     device_name = serializers.CharField(max_length=14, min_length=1, required=True)
#
#
# class GateSerializer(serializers.Serializer):
#
#     device_id = serializers.CharField(required=True, min_length=1)
#
#
# class GateRoomSerializer(serializers.ModelSerializer):
#
#     class Meta:
#         model = Curtain
#         fields = ('Devicename', 'Imagepath', 'Deviceusername', 'Publisheddata', 'Typed', 'Namer')
# Tree
#
#
# class UpdateTreeImgSerializer(serializers.Serializer):
#     TreeId = serializers.CharField(required=True)
#     TreeImage = serializers.CharField(min_length=1, required=True)
#
#
# class UpdateTreeHeightSerializer(serializers.Serializer):
#     TreeId = serializers.CharField(required=True)
#     TreeHeight = serializers.CharField(min_length=1, required=True)
#
#
# class UpdateTreeDetailsSerializer(serializers.Serializer):
#     TreeId = serializers.CharField(required=True)
#     TreeDetails = serializers.CharField(min_length=1, required=True)
#
#
# class TreeResponseSerializer(serializers.Serializer):
#     auth_key = serializers.CharField(max_length=256, min_length=1, required=True)
#     TreeParent = serializers.CharField(min_length=1, required=True)
#
#
# class TreeAddSerializer(serializers.Serializer):
#     TreeName = serializers.CharField(min_length=1, required=True)
#     TreeParent = serializers.CharField(min_length=1, required=True)
#     TreeId = serializers.CharField(min_length=1, required=True)
#     TreeImage = serializers.CharField(min_length=1, required=True)
#     TreeWeight = serializers.CharField(min_length=1, required=True)
#     TreeHeight = serializers.CharField(min_length=1, required=True)
#     TreeDetails = serializers.CharField(min_length=1, required=True)
#     TreeLocation = serializers.CharField(min_length=1, required=True)
#     TreePlantedDate = serializers.CharField(min_length=1, required=True)
#
#
# class TreeEmployAddSerializer(serializers.Serializer):
#     EmployNumber = serializers.CharField(min_length=1, required=True)
#     EmployState = serializers.CharField(min_length=1, required=True)
#     EmployType = serializers.CharField(min_length=1, required=True)
#     EmployAddedBy = serializers.CharField(min_length=1, required=True)
#
#
# class TreeDataSerializer(serializers.ModelSerializer):
#
#     class Meta:
#         model = Tree
#         fields = ('TreeName', 'TreeParent', 'TreeId', 'TreeImage', 'TreeWeight', 'TreeHeight', 'TreeDetails', 'TreeLocation')
#
#
# class TreeUserDataSerializer(serializers.ModelSerializer):
#
#     class Meta:
#         model = TreeUser
#         fields = ('TreeUserNumber', 'TreeUserName')
#
#
# class TreeDataResponseSerializer(serializers.ModelSerializer):
#
#     class Meta:
#         model = Tree
#         fields = ('TreeName', 'TreeParent', 'TreeId', 'TreeImage', 'TreeWeight', 'TreeHeight', 'TreeDetails', 'TreeLocation', 'TreePlantedDate')
#
#
# class TreeOtpSerializer(serializers.Serializer):
#     phone = serializers.CharField(max_length=18, min_length=1, required=True)
#     otp = serializers.CharField(max_length=4, min_length=1, required=True)
#     req_type = serializers.CharField(max_length=13, min_length=1, required=True)
#
#
# class TwitterTreeLoginSerializer(serializers.Serializer):
#     tag = serializers.CharField(max_length=48, min_length=1, required=True)
#     id = serializers.CharField(max_length=40, min_length=1)
#     profile_img = serializers.CharField(max_length=240, min_length=1)
#     auth_key = serializers.CharField(max_length=256, min_length=1, required=True)
#
#
# class TwitterTreeDataResponseSerializer(serializers.ModelSerializer):
#
#     class Meta:
#         model = TwitterTree
#         fields = ('TwitterTreeName', 'TwitterTreeParent', 'TwitterTreeId', 'TwitterTreeImage', 'TwitterTreeWeight', 'TwitterTreeHeight', 'TwitterTreeDetails', 'TwitterTreeLocation', 'TwitterTreePlantedDate', 'TwitterTreeState')
#
#
# class TwitterTreeUserSerializer(serializers.ModelSerializer):
#
#     class Meta:
#         model = TwitterUser
#         fields = ('TwitterUserTag', 'TwitterUserId', 'TwitterTagLine', 'TwitterProfile', 'TwitterCount')
#
#
# class TwitterTreeAddSerializer(serializers.Serializer):
#     Name = serializers.CharField(min_length=1, required=True)
#     Parent = serializers.CharField(min_length=1, required=True)
#     Id = serializers.CharField(min_length=1, required=True)
#     Image = serializers.CharField(min_length=1, required=True)
#     Weight = serializers.CharField(min_length=1, required=True)
#     Height = serializers.CharField(min_length=1, required=True)
#     Details = serializers.CharField(min_length=1, required=True)
#     Location = serializers.CharField(min_length=1, required=True)
#     PlantedDate = serializers.CharField(min_length=1, required=True)
#     State = serializers.CharField(min_length=1, required=True)
#
#
# class TwitterUpdateprofileimgSerializer(serializers.Serializer):
#     id = serializers.CharField(required=True)
#     img = serializers.CharField(min_length=1, required=True)
#
#
# class TwitterTagLineEditSerializer(serializers.Serializer):
#     id = serializers.CharField(required=True)
#     tag = serializers.CharField(min_length=1, required=True)
#
#
# class TwitterProfileSerializer(serializers.Serializer):
#     id = serializers.CharField(required=True)
#
#
# class TreeTwitterResponseSerializer(serializers.Serializer):
#     auth_key = serializers.CharField(max_length=256, min_length=1, required=True)
#     id = serializers.CharField(min_length=1, required=True)
#
#
# class TwitterUpdateTreeDetailsSerializer(serializers.Serializer):
#     id = serializers.CharField(required=True)
#     Details = serializers.CharField(min_length=1, required=True)
#
#
# class TwitterUpdateTreeHeightSerializer(serializers.Serializer):
#     id = serializers.CharField(required=True)
#     Height = serializers.CharField(min_length=1, required=True)





