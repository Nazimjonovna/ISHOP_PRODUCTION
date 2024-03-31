from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.authtoken.models import Token
from drf_yasg.utils import swagger_auto_schema
from .serializer import *
from .models import *

# Create your views here.
class Register(APIView):
    permission_classes = [AllowAny]

    @swagger_auto_schema(request_body=UserSerializer)
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()  # Ensure that this returns a User instance
            print(user)
            if user:
                token = Token.objects.get_or_create(user=user)  # Generate token for user
                return Response({
                    'data': serializer.data,
                    'token': str(token.key)
                })
            else:
                return Response("User could not be created", status=500)  # Indicate failure to create user
        else:
            return Response(serializer.errors, status=400)
         
class LoginView(APIView):
    permission_classes = [AllowAny, ]

    @swagger_auto_schema(request_body=UserSerializer)
    def post(self, request):
        name = request.data.get('name')
        password = request.data.get('password')
        user = User.objects.filter(name = name, password = password).first()
        if user:
            token = Token.objects.get_or_create(user=user)
            return Response({
                'access':str(token)
            })
        else:
            return Response("Not found such kind of user")
        

class SS(APIView):
    permission_classes = [IsAuthenticated, ]

    def get(self, request):
        return Response("dddd")