import requests
import pytz
import datetime as d
from random import randint
from django.forms.models import model_to_dict
from rest_framework import generics
from django.conf import settings
from get_sms import Getsms
from drf_yasg.utils import swagger_auto_schema
from django.utils.translation import gettext_lazy as _
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework_simplejwt.tokens import AccessToken, RefreshToken
from django.contrib.auth.hashers import make_password, check_password
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, parsers
from Product.serializer import *
from .models import *
from .serializer import *

# Create your views here.

utc = pytz.timezone(settings.TIME_ZONE)
min = 1
def send_sms(phone_number, step_reset=None, change_phone=None):
    try:
        verify_code = randint(1111, 9999)
        try:
            obj = Verification.objects.get(phone_number=phone_number)
        except Verification.DoesNotExist:
            obj = Verification(phone_number=phone_number, verify_code=verify_code)
            obj.step_reset=step_reset 
            obj.step_change_phone=change_phone
            obj.save()
            context = {'phone_number': str(obj.phone_number), 'verify_code': obj.verify_code,
                       'lifetime': _(f"{min} minutes")}
            return context
        time_now = d.datetime.now(utc)
        diff = time_now - obj.created
        three_minute = d.timedelta(minutes=min)
        if diff <= three_minute:
            time_left = str(three_minute - diff)
            return {'message': _(f"Try again in {time_left[3:4]} minute {time_left[5:7]} seconds")}
        obj.delete()
        obj = Verification(phone_number=phone_number)
        obj.verify_code=verify_code 
        obj.step_reset=step_reset
        obj.step_change_phone=change_phone
        obj.save()
        context = {'phone_number': str(obj.phone_number), 'verify_code': obj.verify_code, 'lifetime': _(f"{min} minutes")}
        return context
    except Exception as e:
        print(f"\n[ERROR] error in send_sms <<<{e}>>>\n")


class SendSms(generics.CreateAPIView):
    permission_classes = [AllowAny]
    serializer_class = SendSmsSerializer

    
    def post(self, request):
        serializer = SendSmsSerializer(data=request.data)
        if serializer.is_valid():
            login = "QUANTIC"
            password = "B180Ns49DnRbuPX9686R"
            nickname = "QuanticUz"

            message = Getsms(login=login, password=password, nickname=nickname)
            phone_numbers = [serializer.data['phone_number']]

            results = message.send_message(phone_numbers=phone_numbers, text=serializer.data['text'])

            if 'error' in results:
                print(results)

            for result in results:
                print(result)
            return Response({"msg": f"Send SMS successfully to {serializer.data['phone_number']}"})
        else:
            return Response({"msg":serializer.errors})

class PhoneView(APIView):
    queryset = User.objects.all()
    serializer_class = PhoneSRL
    permission_classes = [AllowAny]

    @swagger_auto_schema(request_body=PhoneSRL, tags = ['User'])
    def post(self, request, *args, **kwargs):
        phone_number = request.data.get("phone_number")
        if phone_number.isdigit() and len(phone_number)>8:
            user = User.objects.filter(phone_number__iexact=phone_number)
            if user.exists():
                return Response({
                    "status": False,
                    "detail": "Bu raqam avval registerdan otgan."
                })
            else:
                otp = send_sms(phone_number)
                if 'verify_code' in otp:
                    code = str(otp['verify_code'])
                    try:
                        validate = ValidatedOtp.objects.get(phone_number=phone_number)
                        if validate.validated:
                            validate.otp = code
                            validate.validated= False
                            validate.save()
                        
                    except ValidatedOtp.DoesNotExist as e:
                        phon = ValidatedOtp.objects.filter(phone_number__iexact=phone_number)
                        if not phon.exists():
                            ValidatedOtp.objects.create(phone_number=phone_number, otp=code, validated=False)
                        else:
                            Response({"phone": "mavjud"})

                return Response({
                    "status": True,
                    "detail": "SMS xabarnoma jo'natildi",
                    "code":otp #<--vaqtinchalik qo'shildi
                })
        else:
            if len(phone_number)<8:
                return Response({"detail":"Telefon raqamingizni kod bilan kiriting!"})
            else:    
                return Response({
                    "status": False,
                    "detail": "Telefon raqamni kiriting ."
                })


    def send_otp(phone_number, otp):
        if phone_number:
            otp = randint(999, 9999)
            print(otp)
            return otp
        else:
            return False
        

class OtpView(APIView):
    permission_classes = [AllowAny]

    @swagger_auto_schema(request_body=OtpSRL, tags=['User'])
    def post(self, request):
        phone_number = request.data.get('phone_number', True)
        code_send = request.data.get('otp', True)
        if not phone_number and code_send:
            return Response({
                'status': False,
                'detail': 'Otpni va phone ni kiriting'
            })

        try:
            verify = ValidatedOtp.objects.get(phone_number=phone_number, validated=False)
            if verify.otp == code_send:
                verify.count += 1
                verify.validated = True
                verify.save()

                return Response({
                    'status': True,
                    'detail': "Otp to'g'ri"
                })
            else:
                return Response({
                    'status': False,
                    'error': "Otpni to'g'ri kiriting"})

        except ValidatedOtp.DoesNotExist as e:
            return Response({
                'error': "Otp aktiv emas yoki mavjud emas, boshqa otp oling"
            })
        

class RegisterUserView(APIView):
    permission_classes = [AllowAny]
    serializer_class = RegisterUserSerialzier

    @swagger_auto_schema(request_body=SwaggerRegisterSerializer, tags=['User'])
    def post(self, request):
        try:
            serializer = self.serializer_class(data=request.data)
            if serializer.is_valid():
                phone_number = serializer.validated_data.get('phone_number')
                password = serializer.validated_data.get('password')
                otp = serializer.validated_data.get('otp')
                name = request.data.get('name')
                last_name = request.data.get('last_name')
                print(last_name)
                card = request.data.get('card')
                card_info = request.data.get('card_info')
                paspord_raqam = request.data.get('paspord_raqam')
                paspord_seria = request.data.get('paspord_seria')
                paspord = request.data.get('paspord')
                image = request.data.get('image')
                adress = request.data.get('adress')
                viloyat = request.data.get('viloyat')

                verify = ValidatedOtp.objects.filter(phone_number__iexact=phone_number, validated=True)
                if not verify.exists():
                    return Response({
                        "status": False,
                        "detail": _("You haven't entered a valid one-time secret code. Therefore, you cannot proceed with registration.")
                    }, status=status.HTTP_400_BAD_REQUEST)

                hashed_password = make_password(password)
                user_obj = User.objects.create(phone_number=phone_number, password=hashed_password, otp=otp)

                client_obj = Client.objects.create(user=user_obj, name = name, last_name=last_name, card=card, card_info=card_info,
                                                   paspord_raqam=paspord_raqam, paspord_seria=paspord_seria,
                                                   paspord=paspord, image=image, adress=adress, viloyat=viloyat)

                access_token = AccessToken().for_user(user_obj)
                refresh_token = RefreshToken().for_user(user_obj)

                return Response({
                    "access": str(access_token),
                    "refresh": str(refresh_token),
                    "phone": str(user_obj.phone_number),
                    "client_id": client_obj.id,
                })
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        except Exception as e:
            print(e)
            return Response({
                "status": False,
                "detail": _("An error occurred while processing your request.")
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
class LoginUserView(generics.GenericAPIView):
    permission_classes = [AllowAny, ]
    serializer_class = Log

    @swagger_auto_schema(request_body=Log, tags=['User'])
    def post(self, request):
        try:
            user = User.objects.get(phone_number=request.data['phone_number'])
            if check_password(request.data['password'], user.password):
                phone = User.objects.get(phone_number=request.data['phone_number'])
                access_token = AccessToken().for_user(phone)
                refresh_token = RefreshToken().for_user(phone)
                return Response({
                    "id": phone.id,
                    "access": str(access_token),
                    "refresh": str(refresh_token),
                })
            else:
                return Response({'Xato': "Noto'g'ri password kiritdingiz :("})

        except:
            return Response({'Xato': 'Bunday user mavjud emas :('})
        

class UserdataUpdateDeleteView(APIView):
    permission_classes = [IsAuthenticated, ]

    @swagger_auto_schema(tags=['User'])
    def get(self, request, pk):
        userdata = User.objects.get(pk=pk)
        try:
            userdata = User.objects.get(pk=pk)
        except User.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = RegisterUserSerialzier(userdata)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @swagger_auto_schema(request_body=RegisterUserSerialzier, tags=['User'])
    def patch(self, request, pk):
        try:
            userdata = User.objects.get(pk=pk)
        except User.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = RegisterUserSerialzier(instance=userdata, data=request.data, partial=True)
        seri = DataSerializer(instance=userdata, data=request.data, partial=True)
        if serializer.is_valid() and seri.is_valid():
            serializer.save()
            seri.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(tags=['User'])
    def delete(self, request, pk):
        try:
            userdata = User.objects.get(pk=pk)
        except User.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        userdata.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class ChangePasswordView(generics.UpdateAPIView):

    queryset = User.objects.all()
    permission_classes = (IsAuthenticated,)
    serializer_class = ChangePasswordSerializer
    my_tags = ['Change-Password']

    @swagger_auto_schema(request_body=ChangePasswordSerializer, tags=['User'])
    def put(self, request, *args, **kwargs):
        serializer = ChangePasswordSerializer(instance=self.request.user, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({'msg': 'Password successfully updated'}, status=status.HTTP_200_OK)


class VerifyCodeView(APIView): # tel o'zgartirilgandagi verificatsiya
    serializer_class = VerifyCodeSerializer
    permission_classes = [AllowAny]
    queryset = Verification.objects.all()

    @swagger_auto_schema(request_body=VerifyCodeSerializer, tags=['User'])
    def put(self, request, *args, **kwargs):
        data = request.data
        try:
            obj = Verification.objects.get(phone_number=data['phone_number'])
            serializer = VerifyCodeSerializer(instance=obj, data=data)
            if serializer.is_valid():
                serializer.save()
                if serializer.data['step_change_phone'] == 'confirmed':
                    user = request.user
                    user.phone = data['phone']
                    user.save()
                    return Response({'message': 'Your phone number has been successfully changed!'},
                                status=status.HTTP_202_ACCEPTED)
                return Response({'message': 'This phone number has been successfully verified!'},
                                status=status.HTTP_202_ACCEPTED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Verification.DoesNotExist:
            return Response({'error': 'Phone number or verify code incorrect!'}, statusis_pupil=status.HTTP_400_BAD_REQUEST)


class ResetPasswordView(APIView):
    permission_classes = [AllowAny]
    serializer_class = PhoneSRL
    my_tags = ['Password-Reset']

    @swagger_auto_schema(request_body=PhoneSRL, tags=['User'])
    def post(self, request):
        data = request.data
        if data.get('phone_number'):
            phone_number = data['phone_number']
            user = User.objects.filter(phone_number__iexact=phone_number)
            if user.exists():
                user = user.first()
                context = send_sms(phone_number)
                return Response(context, status=status.HTTP_208_ALREADY_REPORTED)
            return Response({'msg': _('User not found!')})
        return Response({'msg': _("Enter phone number")}, status=status.HTTP_400_BAD_REQUEST)


class ResetPasswordVerifyCode(VerifyCodeView):
    my_tags = ['User']

class ResetPasswordConfirm(APIView):
    permission_classes = [AllowAny]
    serializer_class = ResetPasswordSerializer

    @swagger_auto_schema(request_body=ResetPasswordSerializer, tags=['User'])
    def put(self, request, *args, **kwargs):
        try:
            user = User.objects.get(phone_number=request.data['phone_number'])
        except:
            return Response({'error': "User matching query doesn't exist"}, status=status.HTTP_404_NOT_FOUND)

        serializer = ResetPasswordSerializer(instance=user, data=request.data)
        if serializer.is_valid():
            ver = Verification.objects.get(phone_number=request.data['phone_number'])
            user.set_password(request.data['new_password'])
            ver.step_reset = ''
            ver.save()
            user.save()
            return Response({'message': 'Password successfully updated'}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ChangePhoneNumber(APIView):
    queryset = User.objects.all()
    serializer_class = PhoneSRL
    permission_classes = [AllowAny]

    @swagger_auto_schema(request_body=PhoneSRL, tags=['User'])
    def post(self, request, *args, **kwargs):
        phone_number = request.data.get("phone_number")
        if phone_number.isdigit() and len(phone_number) > 8:
            user = User.objects.filter(phone_number__iexact=phone_number)
            if user.exists():
                return Response({
                    "status": False,
                    "detail": "Bu raqam avval registerdan otgan."
                })
            else:
                otp = send_sms(phone_number)
                if 'verify_code' in otp:
                    code = str(otp['verify_code'])
                    try:
                        validate = ValidatedOtp.objects.get(phone_number=phone_number)
                        if validate.validated:
                            validate.otp = code
                            validate.validated = False
                            validate.save()
                        else:
                            pass

                    except ValidatedOtp.DoesNotExist as e:
                        phon = ValidatedOtp.objects.filter(phone_number__iexact=phone_number)
                        if not phon.exists():
                            ValidatedOtp.objects.create(phone_number=phone_number, otp=code, validated=False)
                        else:
                            Response({"phone": "mavjud"})

                return Response({
                    "status": True,
                    "detail": "SMS xabarnoma jo'natildi",
                    "code": otp  # <--vaqtinchalik qo'shildi
                })
        else:
            if len(phone_number) < 8:
                return Response({"detail": "Telefon raqamingizni kod bilan kiriting!"})
            else:
                return Response({
                    "status": False,
                    "detail": "Telefon raqamni kiriting ."
                })


class ChangePhoneNumberVerifyCode(APIView):
    my_tags = ['User']
    serializer_class = VerifyCodeSerializer
    permission_classes = [AllowAny]
    queryset = Verification.objects.all()

    @swagger_auto_schema(request_body=VerifyCodeSerializer, tags=['User'])
    def put(self, request, *args, **kwargs):
        data = request.data
        try:
            obj = Verification.objects.get(phone_number=data['phone_number'])
            serializer = VerifyCodeSerializer(instance=obj, data=data)
            if serializer.is_valid():
                serializer.save()
                if serializer.data['step_change_phone'] == 'confirmed':
                    user = request.user
                    user.phone_number = data['phone_number']
                    user.save()
                    return Response({'message': 'Your phone number has been successfully changed!'},
                                    status=status.HTTP_202_ACCEPTED)
                return Response({'message': 'This phone number has been successfully verified!'},
                                status=status.HTTP_202_ACCEPTED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Verification.DoesNotExist:
            return Response({'error': 'Phone number or verify code incorrect!'},
                            statusis_pupil=status.HTTP_400_BAD_REQUEST)

class ChangePhoneNumberConfirm(APIView):
    permission_classes = [AllowAny]
    serializer_class = PhoneSRL

    @swagger_auto_schema(request_body=PhoneSRL, tags=['User'])
    def put(self, request, *args, **kwargs):
        try:
            user = User.objects.get(phone_number=request.user)
        except:
            return Response({'error': "User matching query doesn't exist"}, status=status.HTTP_404_NOT_FOUND)

        serializer = PhoneSRL(instance=user, data=request.data)
        if serializer.is_valid():
            ver = Verification.objects.get(phone_number=request.data['phone_number'])
            user.phone_number = request.data['phone_number']
            user.save()
            ver.step_reset = ''
            ver.delete()

            updated_user = User.objects.get(phone_number=serializer.data['phone_number'])
            access_token = AccessToken().for_user(updated_user)
            refresh_token = RefreshToken().for_user(updated_user)

            return Response({'message': 'Phone successfully updated',
                             'access': str(access_token),
                             'refresh': str(refresh_token),
                             })
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)













#? ADMIN PATHLAR VIEWLAR
import random
import string    

def generate_random_string(length):
    characters = string.ascii_lowercase + string.digits + string.ascii_uppercase
    return ''.join(random.choice(characters) for _ in range(length))


def password_generate(length):
    l = [111111, 222222, 333333, 444444, 555555, 666666, 7777777, 888888, 999999]
    while True:
        a = random.randint(111111, 999999)
        if a not in l:
            return str(a)

class AddAdminView(APIView):
    permission_classes = [IsAuthenticated, ]

    @swagger_auto_schema(request_body = AdminSRL, tags=['Admin'])
    def post(self, request):
        admin = request.user
        if admin.is_superuser:
            serializer = AdminSRL(data = request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            else:
                return Response(serializer.errors)
        else:
            return Response("Yangi adminni faqat superuser qo'sha oladi")
       
class LoginAdminView(generics.GenericAPIView):
    permission_classes = [AllowAny, ]
    serializer_class = Log

    @swagger_auto_schema(request_body=Log, tags=['Admin'])
    def post(self, request):
        try:
            user = User.objects.get(phone_number=request.data['phone_number'])
            if check_password(request.data['password'], user.password):
                phone = User.objects.get(phone_number=request.data['phone_number'])
                access_token = AccessToken().for_user(phone)
                refresh_token = RefreshToken().for_user(phone)
                return Response({
                    "id": phone.id,
                    "access": str(access_token),
                    "refresh": str(refresh_token),
                })
            else:
                return Response({'Xato': "Noto'g'ri password kiritdingiz :("})

        except:
            return Response({'Xato': 'Bunday user mavjud emas :('})


class AddProtsent(APIView):
    permission_classes = [IsAuthenticated, ]

    @swagger_auto_schema(request_body = Protsentsrl, tags=['Admin'])
    def post(self, request):
        admin = request.user
        if admin.is_superuser or admin.is_staff:
            serializer = Protsentsrl(data = request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({"Message":"Yangi protsent muvaffaqiyatli qo'shildi", 'data':serializer.data})
            else:
                return Response({"Message":"Xatolik mavjud", 'xato':serializer.errors})
        else:
            return Response({"Message":"Uzr bazada bunday admin topilmadi"})
        

class EditTasdiqView(APIView):
    permission_classes = [IsAuthenticated, ]

    @swagger_auto_schema(request_body = EditTasdiqsrl, tags=['Admin'])
    def patch(self, request, id):
        admin = request.user
        if admin.is_superuser:
            product = Product.objects.filter(id=id).first()
            if product:
                product.tasdiq = True
                product.save()
                serializer = ProodcutSerializer(product)
                serialized_data = serializer.data
                if 'prosent' in serialized_data:
                    del serialized_data['prosent']
                return Response({
                    "Message": "Mahsulot satishga tasdiqlandi",
                    'data': serialized_data,
                })
            else:
                return Response({'Message': 'Bunday Product topilmadi'})
        else:
            return Response("Bu api faqat superuser uchun")


class GetSonProduct(APIView):
    permission_classes = [IsAuthenticated, ]

    @swagger_auto_schema(tags=['Admin'])
    def get(self, request):
        admin = request.user
        t_son = 0
        tm_son = 0
        jami = 0
        tasdiqlangan = []
        tasdiqlanmagan = []
        if admin.is_superuser:
            products = Product.objects.all()
            for product in products:
                if product.tasdiq:
                    t_son += 1
                    product_dict = model_to_dict(product)
                    product_dict['protsent'] = [protsent.name for protsent in product.protsent.all()]  # Adjust according to your model
                    tasdiqlangan.append(product_dict)
                else:
                    tm_son += 1
                    product_dict = model_to_dict(product)
                    product_dict['protsent'] = [protsent.name for protsent in product.protsent.all()]  # Adjust according to your model
                    tasdiqlanmagan.append(product_dict)
            jami = t_son + tm_son
            return Response({
                "Message": "Tasdiqlangan va tasdiqlanmagan tovarlar ro'yhati",
                "Jami mahsulotlar soni": str(jami),
                'Tasdiqlanganlar soni': str(t_son),
                'Tasdiqlanganlar': tasdiqlangan,
                'Tasdiqlanmaganlar soni': str(tm_son),
                'Tasdiqlanmaganlar': tasdiqlanmagan
            })
        else:
            return Response({'Message': "Uzr ushbu ma'lumotlar faqat boshliq uchun beriladi"})


class GetAdminProductsView(APIView):
    permission_classes = [IsAuthenticated, ]

    @swagger_auto_schema(tags=['Admin'])
    def get(self, request):
        quantity = {}
        admin = request.user
        if admin.is_superuser:
            print(admin)
            admins = User.objects.all()
            for admin in admins:
                if admin.is_staff:
                    print(admin.username)
                    orders = Product.objects.filter(admin = admin)
                    serialized_orders = list(orders.values())  # Convert queryset to list of dictionaries
                    quantity[admin.username] = serialized_orders
                    print("s",quantity)
                else:
                    continue
            return Response({"Message":"Adminlar qo'shgan mahsulotlar haqida hisobot", 'data':quantity})
        else:
            return Response({"Message":"uzr ushbu ma'lumotlar faqat boshliq uchun beriladi"})













