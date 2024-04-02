from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework_simplejwt.tokens import AccessToken, RefreshToken
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from drf_yasg.utils import swagger_auto_schema
from .serializer import *
from .models import *

# Create your views here.
class Register(APIView):
    permission_classes = [AllowAny]

    @method_decorator(csrf_exempt)
    @swagger_auto_schema(request_body=AdminSerializer)
    def post(self, request):
        serializer = AdminSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()  
            print(user)
            if user:
                access = AccessToken.for_user(user)  
                return Response({
                    'data': serializer.data,
                    'token': str(access)
                })
            else:
                return Response("User could not be created", status=500)  
        else:
            return Response(serializer.errors, status=400)
         
class LoginView(APIView):
    permission_classes = [AllowAny, ]

    @swagger_auto_schema(request_body=AdminSerializer)
    def post(self, request):
        print("bu request data",request.data)
        phone = request.data.get('phone')
        password = request.data.get('password')
        print(phone, password)
        user = User.objects.filter(phone = phone, password = password).first()
        if user:
            print(user)
            token = AccessToken.for_user(user) 
            return Response({
                'access':str(token)
            })
        else:
            return Response("Not found such kind of user")
        

class SS(APIView):
    permission_classes = [IsAuthenticated, ]

    def get(self, request):
        return Response("dddd")