from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser
from drf_yasg.utils import swagger_auto_schema
from .serializer import *
from .models import *

# Create your views here.
class AboutView(APIView):
    parser_classes = [MultiPartParser, ]

    def get(self, request):
        abouts = About.objects.all()
        if abouts:
            serializer = AboutSerializer(abouts, many = True)
            return Response(serializer.data)
        else:
            return Response("Not found anything")
        
    @swagger_auto_schema(request_body=AboutSerializer)
    def post(self, request):
        serializer = AboutSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
        
class EditAboutView(APIView):
    parser_classes = [MultiPartParser, ]

    def get(self, request, id):
        about = About.objects.filter(id = id).first()
        if about:
            serializer = AboutSerializer(about)
            return Response(serializer.data)
        else:
            return Response("Not found such kind of about")

    @swagger_auto_schema(request_body=AboutSerializer) 
    def patch(self, request, id):
        about = About.objects.filter(id = id).first()
        if about:
            serializer = AboutSerializer(instance=about, data=request.data, partial = True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            else:
                return Response(serializer.errors)
        else:
            return Response("Not found such kind of about")
        
    def delete(self, request, id):
        about = About.objects.filter(id = id).first()
        if about:
            about.delete()
            return Response("Deleted")
        else:
            return Response("Not found such kind of about")
        

    