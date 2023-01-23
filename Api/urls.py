from django.conf.urls import url
from . import views
from django.urls import path, include
urlpatterns = [
    # url(r'^', include('django_alexa.urls')),
    # url(r'^', include('django_alexa.urls')),
    url(r'^7145847273787561e/', views.pdf_view, name='pdf_view'),  # website
    url(r'^7145847273787561r/', views.pdf_view2, name='pdf_view'),  # website


    # Website
    url(r'^sitemap\.xml/$', views.sitemap, name='sitemap'),  # website
    path('', views.index, name='index'),  # website
    # path("try", views.index2, name='index_new'),  # website
    #  path('api/hello', views.ApiEndpoint.as_view()),
    url(r'^switch/', views.switch, name='switch'),  # website
    url(r'^sensor/', views.sensor, name='sensor'),  # website
    path("robots.txt", views.robots_txt, name='robot.txt'),  # website
    url(r'^try/', views.login, name='login'),  # website
    # path("alexa/callback/", views.alexacallback.as_view(), name='alexa_callback'),  # website
    #  path('api/hello',  views.ApiEndpoint.as_view(), name='alexa_callback2'),
    path('link/',  views.apiendpoint2, name='alexa_callback22'),
    # path('api/login_user/', views.UserLoginalexa.as_view(), name='userLogin'),  # G-smart
    path("favicon.ico", views.favicon, name='favicon'),  # website
    url(r'^lock/', views.lock, name='lock'),  # website
    url(r'^threeimg/', views.threeimg, name='lock'),  # website
    url(r'^curtain/', views.curtain, name='curtain'),  # website
    url(r'^ios_app_policy/', views.ios_app_policy, name='ios_app_policy'),  # website
    url(r'^appprivacypolicy/', views.app_policy, name='app_policy'),  # website
    url(r'^current_data/', views.current_data, name='currentData'),  # website
    # # url(r'^current/', views.Current.as_view(), name='current'),  # website  # website
    # url(r'^api/gthink/email/$', views.Email.as_view(), name='email'),  # website https://www.gthinkinventors.in/google/
    # url(r'^api/google/$', views.Google.as_view(), name='google'),  # G-smart
    #
    # # own
    # # url(r'^api/gthink/device_add/$', views.DeviceAdd.as_view(), name='device_add'),  # own
    # # url(r'^api/gthink/again_device_add/$', views.AgainDeviceAdd.as_view(), name='device_add'),  # own
    # # url(r'^api/gthink/device_add_first/$', views.DeviceAddFirst.as_view(), name='device_add_first'),  # own
    # # url(r'^api/gthink/device_add_fan/$', views.DeviceAddFan.as_view(), name='device_add_fan'),  # own
    # url(r'^api/gthink/old_device_add_fan/$', views.OldDeviceAddFan.as_view(), name='device_add_fan'),  # own
    # url(r'^api/gthink/o_device_add_fan/$', views.ODeviceAddFan.as_view(), name='device_add_fan'),  # own
    # url(r'^api/gthink/alexa/(?P<device_id>[\w+]+)/(?P<switch_state>[\w+]+)$', views.Alexa.as_view(), name='alexa'),  # own
    # url(r'^api/gthink/rgbdevice_add/$', views.RGBDeviceAdd.as_view(), name='rgbdevice_add'),  # own
    # url(r'^api/gthink/alexa_list_names/$', views.Alexa_name_list.as_view(), name='rgbdevice_add'),  # own
    #
    #
    #
    # # G-QR
    # url(r'^api/gthink/g_qr/$', views.Gqr.as_view(), name='Gqr'),  # G-QR
    # url(r'^api/gthink/g_dqr/$', views.DGqr.as_view(), name='Gqr'),  # G-QR
    # url(r'^api/gthink/rgb_qr/$', views.RGBqr.as_view(), name='Gqr'),  # G-QR
    # url(r'^api/gthink/s3files/$', views.ListS3Files.as_view(), name='s3files'),  # G-QR
    # url(r'^api/gthink/Activate/$', views.ActivateUser.as_view(), name='UserActivation'),  # G-QR
    # url(r'^api/gthink/CodeUpdate/$', views.CodeUpdate.as_view(), name='CodeUpdate'),  # G-QR
    # url(r'^api/gthink/SsidPassUpdate/$', views.SsidPassUpdate.as_view(), name='SsidPassUpdate'),  # G-QR
    # url(r'^api/gthink/create_room/$', views.CreateRoom.as_view(), name='CreateRoom'),  # G-QR
    # url(r'^api/gthink/update_room_state/$', views.UpdateRoomState.as_view(), name='UpdateRoomState'),    # G-QR
    # url(r'^api/gthink/device_info_list/$', views.DeviceInfoList.as_view(), name='DeviceInfoList'),  # G-QR
    # url(r'^api/gthink/update_response/$', views.UpdateResponse.as_view(), name='UpdateResponse'),  # G-QR
    #
    #
    # # G-Dealer_QR
    # url(r'^api/gthink/G-Dealer_QRg_qr/$', views.DGqr.as_view(), name='Gqr'),  # G-DQR done checked
    # url(r'^api/gthink/G-Dealer_QRrgb_qr/$', views.DRGBqr.as_view(), name='Gqr'),  # G-DQR done checked
    # url(r'^api/gthink/G-Dealer_QR_Activate/$', views.DActivateUser.as_view(), name='UserActivation'),  # G-DQR done checked
    # url(r'^api/gthink/G-Dealer_QR_CodeUpdate/$', views.DCodeUpdate.as_view(), name='CodeUpdate'),  # G-QR checked
    # url(r'^api/gthink/G-Dealer_QR_SsidPassUpdate/$', views.SsidPassUpdate.as_view(), name='SsidPassUpdate'),  # G-QR
    #
    #
    # # under Work
    # url(r'^api/gthink/Device_State_Update/(?P<mobile_id>[\w-]+)/(?P<device_id>[\w-]+)/(?P<switch_id>[\w+]+)/(?P<state>[\w+]+)$', views.Notification.as_view(), name='Device_Notification'),  # device switch
    # url(r'^api/gthink/update_user/$', views.UpdateUser.as_view(), name='updateUser'),
    # url(r'^api/gthink/new_add_child/$', views.NewAddChildUser.as_view(), name='NewAddChild'),
    # url(r'^api/gthink/new_update_child/$', views.NewUpdateChild.as_view(), name='NewUpdateChild'),
    # url(r'^api/gthink/update_heavy_status/$', views.HeavyState.as_view(), name='HeavyState'),
    # url(r'^api/gthink/Update_heavy_TimeStatus/$', views.UpdateHeavyTimeStatus.as_view(), name='UpdateHeavyTimeStatus'),
    # url(r'^api/gthink/installation/$', views.InstallTeam.as_view(), name='InstallTeam'),
    # url(r'^api/gthink/rooms_info/$', views.RoomsInfo.as_view(), name='rooms_info'),  # need to remove
    # url(r'^api/gthink/delete_room/$', views.DeleteRoom.as_view(), name='DeleteRoom'),
    # url(r'^api/gthink/change_room_image/$', views.ChangeRoomImageNew.as_view(), name='ChangeRoomImage'),
    # url(r'^api/gthink/change_room_name/$', views.ChangeRoomNameNew.as_view(), name='UpdateRoomName'),
    # url(r'^api/gthink/change_room_response/$', views.ChangeRoomResponse.as_view(), name='ChangeRoomResponse'),
    # url(r'^api/gthink/change_appliance_name/$', views.ChangeApplianceName.as_view(), name='ChangeApplianceName'),  # for change name
    # url(r'^api/gthink/change_type/$', views.ChangeApplianceType.as_view(), name='ChangeApplianceType'),   # done
    # url(r'^api/gthink/deregister_from_room/$', views.DeRegisterFromRoom.as_view(), name='DeRegisterFromRoom'),
    #
    #
    # # G-Smart App
    #
    # # get
    # url(r'^api/gthink/get_schedules/(?P<device_id>[\w+]+)$', views.GetScheduleInfoApps.as_view(), name='get_schedule_info_Apps'),  # G-smart
    #
    #
    # # post
    # url(r'^api/gthink/add_user/$', views.UserList.as_view(), name='addUser'),  # G-smart
    # url(r'^api/gthink/login_user/$', views.UserLogin.as_view(), name='userLogin'),  # G-smart
    # url(r'^api/gthink/validate_OTP/$', views.Otp.as_view(), name='validate_OTP'),  # G-smart
    # #  url(r'^api/gthink/add_child/$', views.AddChildUser.as_view(), name='addChild'),  # G-smart old
    # url(r'^api/gthink/child_list/$', views.GetChildList.as_view(), name='childList'),  # G-smart
    # url(r'^api/gthink/update_child/$', views.UpdateChild.as_view(), name='updateChild'),  # G-smart
    # url(r'^api/gthink/delete_child/$', views.DeleteChild.as_view(), name='deleteChild'),  # G-smart
    # url(r'^api/gthink/update_room_img/$', views.UpdateRoomImg.as_view(), name='updateRoomImg'),  # G-smart
    # url(r'^api/gthink/update_room_name/$', views.UpdateRoomName.as_view(), name='updateRoomName'),  # G-smart
    # url(r'^api/gthink/update_icon_name/$', views.UpdateIconName.as_view(), name='updateIconName'),  # G-smart
    # url(r'^api/gthink/update_notification_status/$', views.UpdateNotificationStatus.as_view(), name='UpdateNotificationStatus'),  # G-smart
    # url(r'^api/gthink/get_notification_status/$', views.GETNotificationStatus.as_view(), name='GetNotificationStatus'),  # G-smart
    # url(r'^api/gthink/UpdateNotificationTimeStatus/$', views.UpdateNotificationTimeStatus.as_view(), name='UpdateNotificationTimeStatus'),  # G-smart
    # url(r'^api/gthink/update_profile_img/$', views.UpdatePrfImg.as_view(), name='updatePrfImg'),  # G-smart
    # url(r'^api/gthink/update_background_img/$', views.UpdateBackImg.as_view(), name='UpdateBackImg'),  # G-smart
    # url(r'^api/gthink/update_fcmtoken/$', views.UpdateNotificationToken.as_view(), name='UpdateFcmtoken'),  # G-smart
    # url(r'^api/gthink/delete_schedule/$', views.DeleteSchedule.as_view(), name='delete_schedule'),  # G-smart
    url(r'^api/gthink/schedule_device/$', views.ScheduleDevice.as_view(), name='schedule_device'),  # G-smart
    url(r'^api/gthink/schedule_device2/$', views.ScheduleDevice.as_view(), name='schedule_device'),  # G-smart
    # url(r'^api/gthink/new_rooms_info/$', views.NewRoomsInfo.as_view(), name='rooms_info2'),  # G-smart
    # url(r'^api/gthink/ir_rooms_info/$', views.IRRoomsInfo.as_view(), name='rooms_info2'),  # G-smart
    # # rgb
    # url(r'^api/gthink/rgbrooms_info2/$', views.RGBRoomsInfo.as_view(), name='RGBrooms_info'),  # G-smart
    # url(r'^api/gthink/rgbrooms_info/$', views.RGBNewRoomsInfo.as_view(), name='RGBrooms_info'),  # G-smart
    # url(r'^api/gthink/update_rgbroom_name/$', views.RGBUpdateRoomName.as_view(), name='updateRoomName'),  # G-smart
    # url(r'^api/gthink/Gswitch/rgbGcode/(?P<device_id>[\w+]+)$', views.RGBGCode.as_view(), name='RGBGcode'),  # device not for working
    #
    # # IR
    # url(r'^api/gthink/UpdateIRButton/$', views.UpdateIRButton.as_view(), name='UpdateIRButton'),
    # url(r'^api/gthink/create_ir_room/$', views.CreateIRRoom.as_view(), name='CreateIRRoom'),
    # url(r'^api/gthink/delete_ir_room/$', views.DeleteIRRoom.as_view(), name='DeleteIRRoom'),
    # url(r'^api/gthink/ir_device_info_list/$', views.IRDeviceInfoList.as_view(), name='IRDeviceInfoList'),
    # url(r'^api/gthink/ir_devices_data_list/$', views.IRDeviceDataList.as_view(), name='IRDeviceDataList'),
    # url(r'^api/gthink/ir_update_child/$', views.IRUpdateChild.as_view(), name='irupdateChild'),
    # url(r'^api/gthink/validate_remote_device/(?P<device_id>[\w+]+)$', views.RemoteRecognition.as_view(), name='validate_device'),  # device switch
    #
    # # Device
    # url(r'^api/gthink/get_current_date/$', views.Time.as_view(), name='getDate'),  # device switch
    # url(r'^api/gthink/Device_Notification/(?P<mobile_id>[\w-]+)/(?P<device_id>[\w-]+)/(?P<switch_id>[\w+]+)/(?P<state>[\w+]+)$', views.Notification.as_view(), name='Device_Notification'),  # device switch Device_LastState
    # url(r'^api/gthink/Device_LastState/(?P<device_id>[\w-]+)/(?P<switch_id>[\w-]+)/(?P<switch_state>[\w+]+)$', views.LastState.as_view(), name='Device_State'),  # device switch
    # url(r'^api/gthink/Device_GetState/(?P<device_id>[\w-]+)/(?P<switch_id>[\w-]+)$', views.GetState.as_view(), name='Device_State'),  # device switch
    # url(r'^api/gthink/validate_device/(?P<device_id>[\w+]+)$', views.DeviceRecognition.as_view(), name='validate_device'),  # device switch
    # url(r'^api/gthink/validate_clone_device/(?P<device_id>[\w+]+)$', views.CloneDeviceRecognition.as_view(), name='clone_validate_device'),  # device switch
    # url(r'^api/gthink/validate_semi_clone_device/(?P<device_id>[\w+]+)$', views.SemiCloneDeviceRecognition.as_view(), name='semi_clone_validate_device'),  # device switch
    # url(r'^api/gthink/get_schedule_info/(?P<device_id>[\w+]+)$', views.GetScheduleInfo.as_view(), name='get_schedule_info'),  # device switch
    # url(r'^api/gthink/delete_schedule_device/$', views.DeleteScheduleDevice.as_view(), name='delete_schedule_device'),   # device switch
    # url(r'^api/gthink/validate_rgb_device/(?P<device_id>[\w+]+)$', views.RGBDeviceRecognition.as_view(), name='validate_device'),  # device switch
    # url(r'^api/gthink/validate_ir_device/(?P<device_id>[\w+]+)$', views.IRDeviceRecognition.as_view(), name='validate_device'),  # device switch



    # unknow

    # path('o/', include('oauth2_provider.urls', namespace='oauth2_provider')),
]
