from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework_simplejwt.tokens import AccessToken, RefreshToken
from drf_yasg.utils import swagger_auto_schema
from .serializer import *
from .models import *

# Create your views here.
class AdminRegister(APIView):
    permission_classes = [AllowAny, ]

    @swagger_auto_schema(request_body=AdminSerializer)
    def post(self, request):
        serializer = AdminSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()

            # Generate JWT tokens for admin
            access_token = AccessToken.for_user(user)
            refresh_token = RefreshToken.for_user(user)

            return Response({
                'data': serializer.data,
                'access': str(access_token),
                'refresh': str(refresh_token)
            })
        else:
            return Response(serializer.errors)
        

class LoginView(APIView):
    permission_classes = [AllowAny, ]

    @swagger_auto_schema(request_body=AdminSerializer)
    def post(self, request):
        name = request.data.get('name')
        password = request.data.get('password')
        user = Admin.objects.filter(name = name, password = password).first()
        print(user)
        if user:
            access = AccessToken.for_user(user)
            refresh = RefreshToken.for_user(user)
            return Response({
                'access':str(access)
            })
        else:
            return Response("Not found such kind of user")
        

class SS(APIView):
    permission_classes = [IsAuthenticated, ]

    def get(self, request):
        return Response("dchjnsd")