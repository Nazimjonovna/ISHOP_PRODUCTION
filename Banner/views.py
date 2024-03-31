from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser
from drf_yasg.utils import swagger_auto_schema
from .models import *
from .serializer import *

# Create your views here.
class BannerView(APIView):
    parser_classes = [MultiPartParser, ]

    def get(self, request):
        banners = Banner.objects.all()
        if banners:
            serializer = BannerSerializer(banners, many = True)
            return Response(serializer.data)
        else:
            return Response("Not found anything")
        
    @swagger_auto_schema(request_body=BannerSerializer)
    def post(self, request):
        serializer = BannerSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)

        
class EditBannerView(APIView):
    parser_classes = [MultiPartParser, ]

    def get(self, request, id):
        banner = Banner.objects.filter(id = id).first()
        if banner:
            serializer = BannerSerializer(banner)
            return Response(serializer.data)
        else:
            return Response("Not found anything")
        
    @swagger_auto_schema(request_body=BannerSerializer)
    def patch(self, request, id):
        banner = Banner.objects.filter(id = id).first()
        if banner:
            serializer = BannerSerializer(instance=banner, data=request.data, partial = True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            else:
                return Response(serializer.errors)
        else:
            return Response("Not found anything")
        
    def delete(self, request, id):
        banner = Banner.objects.filter(id = id).first()
        if banner:
            banner.delete()
            return Response('Moved to crush')
        else:
            return Response("Not found anything")
        

