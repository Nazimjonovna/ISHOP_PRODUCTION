from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser
from drf_yasg.utils import swagger_auto_schema
from .serializer import *
from .models import *

# Create your views here.
#! PARAMETR
class ParametrView(APIView):
    parser_classes = [MultiPartParser, ]

    def get(self, request):
        parametrs = Parametr.objects.all()
        if parametrs:
            serializer = ParametrSerializer(parametrs, many = True)
            return Response(serializer.data)
        else:
            return Response("Not found anything")
        
    @swagger_auto_schema(request_body=ParametrSerializer)
    def post(self, request):
        serializer = ParametrSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
        
class EditParametrView(APIView):
    parser_classes = [MultiPartParser, ]

    def get(self, request, id):
        parametr = Parametr.objects.filter(id = id).first()
        if parametr:
            serializer = ParametrSerializer(parametr)
            return Response(serializer.data)
        else:
            return Response("Not found anything")
        
    @swagger_auto_schema(request_body=ParametrSerializer)
    def patch(self, request, id):
        parametr = Parametr.objects.filter(id = id).first()
        if parametr:
            serializer = ParametrSerializer(instance=parametr, data = request.data, partial = True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            else:
                return Response(serializer.errors)
        else:
            return Response("Not found anything")
        

    def delete(self, request, id):
        parametr = Parametr.objects.filter(id = id).first()
        if parametr:
            parametr.delete()
            return Response("Deleted")
        else:
            return Response("Not found anything")
        





#!CATEGORY
# // ! CATEGORY
class CategoryView(APIView):
    parser_classes = [MultiPartParser, ]

    def get(self, request):
        categories = Category.objects.all()
        if categories:
            serializer = CategorySerializer(categories, many = True)
            return Response(serializer.data)
        else:
            return Response("Not found anything")
        
    @swagger_auto_schema(request_body=CategorySerializer)
    def post(self, request):
        serializer = CategorySerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
        
        
class EditCategoryView(APIView):
    parser_classes = [MultiPartParser, ]

    def get(self, request, id):
        parametr = Category.objects.filter(id = id).first()
        if parametr:
            serializer = CategorySerializer(parametr)
            return Response(serializer.data)
        else:
            return Response("Not found anything")
        
    @swagger_auto_schema(request_body=CategorySerializer)
    def patch(self, request, id):
        parametr = Category.objects.filter(id = id).first()
        if parametr:
            serializer = CategorySerializer(instance=parametr, data = request.data, partial = True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            else:
                return Response(serializer.errors)
        else:
            return Response("Not found anything")
        

    def delete(self, request, id):
        parametr = Category.objects.filter(id = id).first()
        if parametr:
            parametr.delete()
            return Response("Deleted")
        else:
            return Response("Not found anything")
        

    # tekshir#####
class FilterCategory(APIView):
    parser_classes = [MultiPartParser, ]

    @swagger_auto_schema(request_body=CategorySerializer)
    def post(self, request):
        name = request.data.get('name')
        categories = Category.objects.all()
        if categories:
            for category in categories:
                if category.name_en == name or category.name_ru == name or category.name_uz == name:
                    serializer = CategorySerializer(category)
                elif category.name_en != name or category.name_ru != name or category.name_uz != name:
                    continue
                else:
                    return Response("Not found such kind of category")
            return Response(serializer.data)
        else:
            return Response("Not found anything")
        








#! NEWS
class NewsView(APIView):
    parser_classes = [MultiPartParser, ]

    def get(self, request):
        news = News.objects.all()
        if news:
            serializer = NewsSerializer(news, many = True)
            return Response(serializer.data)
        else:
            return Response('Not found anything')
        
    @swagger_auto_schema(request_body=NewsSerializer)
    def post(self, request):
        serializer = NewsSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
        
class EditNewsView(APIView):
    parser_classes = [MultiPartParser, ]

    def get(self, request, id):
        new = News.objects.filter(id = id).first()
        if new:
            serializer = NewsSerializer(new)
            return Response(serializer.data)
        else:
            return Response("Not found anything")
        
    @swagger_auto_schema(request_body=NewsSerializer)
    def patch(self, request, id):
        new = News.objects.filter(id = id).first()
        if new:
            serializer = NewsSerializer(instance=new, data = request.data, partial = True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            else:
                return Response(serializer.errors)
        else:
            return Response("Not found anything")
        

    def delete(self, request, id):
        new = News.objects.filter(id = id).first()
        if new:
            new.delete()
            return Response("Deleted")
        else:
            return Response("Not found anything") 

        
            



#! BRAND
class BrandView(APIView):
    parser_classes = [MultiPartParser, ]

    def get(self, request):
        brand = Brand.objects.all()
        if brand:
            serializer = BrandSerializer(brand, many = True)
            return Response(serializer.data)
        else:
            return Response('Not found anything')
        
    @swagger_auto_schema(request_body=BrandSerializer)
    def post(self, request):
        serializer = BrandSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
        
class EditBrandView(APIView):
    parser_classes = [MultiPartParser, ]

    def get(self, request, id):
        brand = Brand.objects.filter(id = id).first()
        if brand:
            serializer = BrandSerializer(brand)
            return Response(serializer.data)
        else:
            return Response("Not found anything")
        
    @swagger_auto_schema(request_body=BrandSerializer)
    def patch(self, request, id):
        brand = Brand.objects.filter(id = id).first()
        if brand:
            serializer = BrandSerializer(instance=brand, data = request.data, partial = True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            else:
                return Response(serializer.errors)
        else:
            return Response("Not found anything")
        

    def delete(self, request, id):
        brand = Brand.objects.filter(id = id).first()
        if brand:
            brand.delete()
            return Response("Deleted")
        else:
            return Response("Not found anything") 
        





#! CONTACT
class ContactView(APIView):
    parser_classes = [MultiPartParser, ]

    def get(self, request):
        contact = Contact.objects.all()
        if contact:
            serializer = ContactSerializer(contact, many = True)
            return Response(serializer.data)
        else:
            return Response("Not found anything")
        
    @swagger_auto_schema(request_body=CategorySerializer)
    def post(self, request):
        serializer = CategorySerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
        
class EditContactView(APIView):
    parser_classes = [MultiPartParser, ]

    def get(self, request, id):
        contact = Contact.objects.filter(id = id).first()
        if contact:
            serializer = ContactSerializer(contact)
            return Response(serializer.data)
        else:
            return Response("Not found anything")

    @swagger_auto_schema(request_body=CategorySerializer)   
    def patch(self, request, id):
        contact = Contact.objects.filter(id = id).first()
        if contact:
            serializer = ContactSerializer(instance=contact, data = request.data, partial = True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            else:
                return Response(serializer.errors)
        else:
            return Response("Not found anything")
        

    def delete(self, request, id):
        contact = Contact.objects.filter(id = id).first()
        if contact:
            contact.delete()
            return Response("Deleted")
        else:
            return Response("Not found anything") 
        





#! PublicOffer
class PublicOfferView(APIView):
    parser_classes = [MultiPartParser, ]

    def get(self, request):
        offer = PublicOffer.objects.all()
        if offer:
            serializer = PublicOfferSerializer(offer, many = True)
            return Response(serializer.data)
        else:
            return Response("Not found anything")

    @swagger_auto_schema(request_body=PublicOfferSerializer) 
    def post(self, request):
        serializer = PublicOfferSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
        
class EditPublicOfferView(APIView):
    parser_classes = [MultiPartParser, ]

    def get(self, request, id):
        offer = PublicOffer.objects.filter(id = id).first()
        if offer:
            serializer = PublicOfferSerializer(offer)
            return Response(serializer.data)
        else:
            return Response("Not found anything")

    @swagger_auto_schema(request_body=PublicOfferSerializer)    
    def patch(self, request, id):
        offer = PublicOffer.objects.filter(id = id).first()
        if offer:
            serializer = PublicOfferSerializer(instance=offer, data = request.data, partial = True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            else:
                return Response(serializer.errors)
        else:
            return Response("Not found anything")
        

    def delete(self, request, id):
        offer = PublicOffer.objects.filter(id = id).first()
        if offer:
            offer.delete()
            return Response("Deleted")
        else:
            return Response("Not found anything") 
        







#! MEDIA
class MediaView(APIView):
    parser_classes = [MultiPartParser, ]

    @swagger_auto_schema(request_body=MediaSerializer) 
    def post(self, request):
        serializer = MediaSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
        

class EditMediaView(APIView):
    parser_classes = [MultiPartParser, ]

    @swagger_auto_schema(request_body=MediaSerializer) 
    def patch(self, request, id):
        offer = Media.objects.filter(id = id).first()
        if offer:
            serializer = MediaSerializer(instance=offer, data = request.data, partial = True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            else:
                return Response(serializer.errors)
        else:
            return Response("Not found anything")
        
    def delete(self, request, id):
        offer = Media.objects.filter(id = id).first()
        if offer:
            offer.delete()
            return Response("Deleted")
        else:
            return Response("Not found anything") 
        
    
#! PRODUCT
class ProductView(APIView):
    parser_classes = [MultiPartParser, ]

    @swagger_auto_schema(request_body=ProodcutSerializer) 
    def post(self, request):
        serializer = ProodcutSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
        
    def get(self, request):
        products = Product.objects.all()
        if products:
            medias = Media.objects.all()
            if medias:
                for media in medias:
                    pass

class EditProductView(APIView):
    parser_classes = [MultiPartParser, ]
    
    def get(self, request, id):
        product = Product.objects.filter(id = id).first()
        rasm = []
        if product:
            medias = Media.objects.all()
            for media in medias:
                if media.product_id == id:
                    rasm.append(media)
            serializer = ProodcutSerializer(product)
            seri = MediaSerializer(rasm, many = True)
            return Response({"product":serializer.data, 'rasm':seri.data})
        else:
            return Response("Not found such kind of product")
        
    @swagger_auto_schema(request_body=ProodcutSerializer)
    def patch(self, request, id):
        product = Product.objects.filter(id = id).first()
        if product:
            serializer = ProodcutSerializer(instance=product, data = request.data, partial = True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            else:
                return Response(serializer.errors)
        else:
            return Response("Not found anything")
        
    def delete(self, request, id):
        product = Product.objects.filter(id = id).first()
        if product:
            product.delete()
            return Response("Deleted")
        else:
            return Response("Not found anything") 
        



