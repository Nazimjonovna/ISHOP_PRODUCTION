from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework_simplejwt.tokens import AccessToken, RefreshToken
from drf_yasg.utils import swagger_auto_schema
from .serializer import *
from .models import *

# Create your views here.
class Register(APIView):
    permission_classes = [AllowAny]

    @swagger_auto_schema(request_body=AdminSerializer)
    def post(self, request):
        serializer = AdminSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()  # Ensure that this returns a User instance
            print(user)
            if user:
                access = AccessToken.for_user(user)  # Generate token for user
                return Response({
                    'data': serializer.data,
                    'token': str(access)
                })
            else:
                return Response("User could not be created", status=500)  # Indicate failure to create user
        else:
            return Response(serializer.errors, status=400)
         
class LoginView(APIView):
    permission_classes = [AllowAny, ]

    @swagger_auto_schema(request_body=AdminSerializer)
    def post(self, request):
        print("bu request data",request.data)
        name = request.data.get('name')
        password = request.data.get('password')
        print(name, password)
        user = User.objects.filter(name = name, password = password).first()
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