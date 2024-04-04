from django.urls import path
from .views import *

urlpatterns = [
    #! USER PATH
    path('user/phone/', PhoneView.as_view()),
    path('user/sms-check/', OtpView.as_view()),
    path('user/register/', RegisterUserView.as_view()),
    path('user/login/', LoginUserView.as_view()),
    path('user/account-edit/', UserdataUpdateDeleteView.as_view()),
    path('user/get_user_data/<int:pk>/', UserdataUpdateDeleteView.as_view()),
    path('user/change_password/<int:pk>/', ChangePasswordView.as_view()),
    path('user/resent_password', ResetPasswordView.as_view()),
    path('user/resent_password_verify/', ResetPasswordVerifyCode.as_view()),
    path('user/resent_password_confirm/', ResetPasswordConfirm.as_view()),
    path('user/change_phone/', ChangePhoneNumber.as_view()),
    path('user/change_phone_verify/', ChangePhoneNumberVerifyCode.as_view()),
    path('user/change_phone_confirm/', ChangePhoneNumberConfirm.as_view()),
    #! ADMIN PATH
    path('admin/post/', AddAdminView.as_view()),
    path('admin/login/', LoginAdminView.as_view()),
    path('admin/add_protsent/', AddProtsent.as_view()),
    path('admin/edit_product_tasdiq/<int:id>/', EditTasdiqView.as_view()),
    path('admin/get_quantity_ofProduct/', GetSonProduct.as_view()),
]