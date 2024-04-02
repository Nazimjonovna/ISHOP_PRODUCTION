from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework_simplejwt.tokens import AccessToken, RefreshToken
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from drf_yasg.utils import swagger_auto_schema
from .serializer import *
from .models import *
from rest_framework_simplejwt.tokens import AccessToken
from rest_framework.response import Response

# Create your views here.
from .models import User  # Import the User model

class Register(APIView):
    permission_classes = [AllowAny]

    # @method_decorator(csrf_exempt)
    @swagger_auto_schema(request_body=AdminSerializer)
    def post(self, request):
            print("bu request data", request.data)
            serializer = AdminSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save() 
            user = User.objects.filter(phone_number = request.data.get('phone_number')).first()
            print(user)
            token = AccessToken.for_user(user)
            return Response({
                'data':serializer.data,
                'access':str(token)
            })
            # return Response("User created successfully")
            # if serializer.is_valid():
            #     print("bu serializer data", serializer.data)
            #     user = serializer.save()  
            #     print(user)
            #     if user:
            #         access = AccessToken.for_user(user)  
            #         return Response({
            #             'data': serializer.data,
            #             'token': str(access)
            #         })
            #     else:
            #         return Response("User could not be created", status=500)  
            # else:
            #     return Response(serializer.errors, status=400)
         

class LoginView(APIView):
    permission_classes = [AllowAny, ]

    @swagger_auto_schema(request_body=LoginSerializer)
    def post(self, request):
        print("bu request data",request.data)
        phone_number = request.data.get('phone_number')
        password = request.data.get('password')
        print(phone_number, password)
        user = User.objects.filter(phone_number = phone_number, password = password).first()
        if user:
            print(user)
            token = AccessToken.for_user(user) 
            return Response({
                'access':str(token)
            })
        else:
            return Response("Not found such kind of user")
        

# class SS(APIView):
#     permission_classes = [IsAuthenticated, ]

#     def get(self, request):
#         return Response("dddd")
    

class UserListView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        print(request.user)
        users = User.objects.all()
        serializer = AdminSerializer(users, many=True)
        return Response(serializer.data)