from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser
from drf_yasg.utils import swagger_auto_schema
from rest_framework.permissions import AllowAny, IsAuthenticated
from .serializer import *
from .models import *

# Create your views here.
#! PARAMETR
class ParametrView(APIView):
    parser_classes = [MultiPartParser, ]
    permission_class = [IsAuthenticated]

    @swagger_auto_schema(tags=['Parametr'])
    def get(self, request):
            parametrs = Parametr.objects.all()
            if parametrs:
                serializer = ParametrSerializer(parametrs, many = True)
                return Response(serializer.data)
            else:
                return Response("Not found anything")
        
    @swagger_auto_schema(request_body=ParametrSerializer, tags=['Parametr'])
    def post(self, request):
        admin = request.user
        if admin.is_superuser or admin.is_staff:
            serializer = ParametrSerializer(data = request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            else:
                return Response(serializer.errors)
        else:
            return Response("You have not such kind of permission")
        
class EditParametrView(APIView):
    parser_classes = [MultiPartParser, ]
    permission_class = [IsAuthenticated]

    @swagger_auto_schema(tags=['Parametr'])
    def get(self, request, id):
        admin = request.user
        if admin.is_superuser or admin.is_staff:
            parametr = Parametr.objects.filter(id = id).first()
            if parametr:
                serializer = ParametrSerializer(parametr)
                return Response(serializer.data)
            else:
                return Response("Not found anything")
        else:
            return Response("You have not such kind of permission")
        
    @swagger_auto_schema(request_body=ParametrSerializer, tags=['Parametr'])
    def patch(self, request, id):
        admin = request.user
        if admin.is_superuser or admin.is_staff:
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
        else:
            return Response("You have not such kind of permission")
        

    def delete(self, request, id):
        admin = request.user
        if admin.is_superuser or admin.is_staff:
            parametr = Parametr.objects.filter(id = id).first()
            if parametr:
                parametr.delete()
                return Response("Deleted")
            else:
                return Response("Not found anything")
        else:
            return Response("You have not such kind of permission")
        





#!CATEGORY
# // ! CATEGORY
class CategoryView(APIView):
    parser_classes = [MultiPartParser, ]
    permission_class = [IsAuthenticated]

    @swagger_auto_schema(tags=['Category'])
    def get(self, request):
            categories = Category.objects.all()
            if categories:
                serializer = CategorySerializer(categories, many = True)
                return Response(serializer.data)
            else:
                return Response("Not found anything")
        
    @swagger_auto_schema(request_body=CategorySerializer, tags=['Category'])
    def post(self, request):
        admin = request.user
        if admin.is_superuser or admin.is_staff:
            serializer = CategorySerializer(data = request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            else:
                return Response(serializer.errors)
        else:
            return Response("You have not such kind of permission")
        
        
class EditCategoryView(APIView):
    parser_classes = [MultiPartParser, ]
    permission_class = [IsAuthenticated]

    @swagger_auto_schema(tags=['Category'])
    def get(self, request, id):
        admin = request.user
        if admin.is_superuser or admin.is_staff:
            parametr = Category.objects.filter(id = id).first()
            if parametr:
                serializer = CategorySerializer(parametr)
                return Response(serializer.data)
            else:
                return Response("Not found anything")
        else:
            return Response("You have not such kind of permission")
        
    @swagger_auto_schema(request_body=CategorySerializer, tags=['Category'])
    def patch(self, request, id):
        admin = request.user
        if admin.is_superuser or admin.is_staff:
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
        else:
            return Response("You have not such kind of permission")
        

    @swagger_auto_schema(tags=['Category'])
    def delete(self, request, id):
        admin = request.user
        if admin.is_superuser or admin.is_staff:
            parametr = Category.objects.filter(id = id).first()
            if parametr:
                parametr.delete()
                return Response("Deleted")
            else:
                return Response("Not found anything")
        else:
            return Response("You have not such kind of permission")
        

    # tekshir#####
class FilterCategory(APIView):
    parser_classes = [MultiPartParser, ]
    permission_class = [AllowAny]

    @swagger_auto_schema(request_body=CategorySerializer, tags=['Category'])
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
    permission_class = [IsAuthenticated]

    @swagger_auto_schema(tags=['News'])
    def get(self, request):
            news = News.objects.all()
            if news:
                serializer = NewsSerializer(news, many = True)
                return Response(serializer.data)
            else:
                return Response('Not found anything')
        
    @swagger_auto_schema(request_body=NewsSerializer, tags=["News"])
    def post(self, request):
        admin = request.user
        if admin.is_superuser or admin.is_staff:
            serializer = NewsSerializer(data = request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            else:
                return Response(serializer.errors)
        else:
            return Response("You have not such kind of permission")
        
class EditNewsView(APIView):
    parser_classes = [MultiPartParser, ]
    permission_class = [IsAuthenticated]

    @swagger_auto_schema(tags=['News'])
    def get(self, request, id):
        admin = request.user
        if admin.is_superuser or admin.is_staff:
            new = News.objects.filter(id = id).first()
            if new:
                serializer = NewsSerializer(new)
                return Response(serializer.data)
            else:
                return Response("Not found anything")
        else:
            return Response("You have not such kind of permission")
        
    @swagger_auto_schema(request_body=NewsSerializer, tags=['News'])
    def patch(self, request, id):
        admin = request.user
        if admin.is_superuser or admin.is_staff:
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
        else:
            return Response("You have not such kind of permission")
        
    @swagger_auto_schema(tags=['News'])
    def delete(self, request, id):
        admin = request.user
        if admin.is_superuser or admin.is_staff:
            new = News.objects.filter(id = id).first()
            if new:
                new.delete()
                return Response("Deleted")
            else:
                return Response("Not found anything")
        else:
            return Response("You have not such kind of permission") 

        
            



#! BRAND
class BrandView(APIView):
    parser_classes = [MultiPartParser, ]
    permission_class = [IsAuthenticated]

    @swagger_auto_schema(tags=['Brand'])
    def get(self, request):
            brand = Brand.objects.all()
            if brand:
                serializer = BrandSerializer(brand, many = True)
                return Response(serializer.data)
            else:
                return Response('Not found anything')
        
    @swagger_auto_schema(request_body=BrandSerializer, tags=['Brand'])
    def post(self, request):
        admin = request.user
        if admin.is_superuser or admin.is_staff:
            serializer = BrandSerializer(data = request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            else:
                return Response(serializer.errors)
        else:
            return Response("You have not such kind of permission") 
        
class EditBrandView(APIView):
    parser_classes = [MultiPartParser, ]
    permission_class = [IsAuthenticated]

    @swagger_auto_schema(tags=['Brand'])
    def get(self, request, id):
        admin = request.user
        if admin.is_superuser or admin.is_staff:
            brand = Brand.objects.filter(id = id).first()
            if brand:
                serializer = BrandSerializer(brand)
                return Response(serializer.data)
            else:
                return Response("Not found anything")
        else:
            return Response("You have not such kind of permission") 
        
    @swagger_auto_schema(request_body=BrandSerializer, tags=['Brand'])
    def patch(self, request, id):
        admin = request.user
        if admin.is_superuser or admin.is_staff:
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
        else:
            return Response("You have not such kind of permission")
        

    @swagger_auto_schema(tags=['Brand'])
    def delete(self, request, id):
        admin = request.user
        if admin.is_superuser or admin.is_staff:
            brand = Brand.objects.filter(id = id).first()
            if brand:
                brand.delete()
                return Response("Deleted")
            else:
                return Response("Not found anything") 
        else:
            return Response("You have not such kind of permission")
        





#! CONTACT
class ContactView(APIView):
    parser_classes = [MultiPartParser, ]
    permission_class = [IsAuthenticated]

    @swagger_auto_schema(tags=['Contact'])
    def get(self, request):
            contact = Contact.objects.all()
            if contact:
                serializer = ContactSerializer(contact, many = True)
                return Response(serializer.data)
            else:
                return Response("Not found anything")
        
    @swagger_auto_schema(request_body=CategorySerializer, tags=['Contact'])
    def post(self, request):
        admin = request.user
        if admin.is_superuser or admin.is_staff:
            serializer = CategorySerializer(data = request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            else:
                return Response(serializer.errors)
        else:
            return Response("You have not such kind of permission")
        
class EditContactView(APIView):
    parser_classes = [MultiPartParser, ]
    permission_class = [IsAuthenticated]

    @swagger_auto_schema(tags=['Contact'])
    def get(self, request, id):
        admin = request.user
        if admin.is_superuser or admin.is_staff:
            contact = Contact.objects.filter(id = id).first()
            if contact:
                serializer = ContactSerializer(contact)
                return Response(serializer.data)
            else:
                return Response("Not found anything")
        else:
            return Response("You have not such kind of permission")

    @swagger_auto_schema(request_body=CategorySerializer, tags=['Contact'])   
    def patch(self, request, id):
        admin = request.user
        if admin.is_superuser or admin.is_staff:
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
        else:
            return Response("You have not such kind of permission")
        
    @swagger_auto_schema(tags=['Contact'])
    def delete(self, request, id):
        admin = request.user
        if admin.is_superuser or admin.is_staff:
            contact = Contact.objects.filter(id = id).first()
            if contact:
                contact.delete()
                return Response("Deleted")
            else:
                return Response("Not found anything") 
        else:
            return Response("You have not such kind of permission")
        





#! PublicOffer
class PublicOfferView(APIView):
    parser_classes = [MultiPartParser, ]
    permission_class = [IsAuthenticated]

    @swagger_auto_schema(tags=['PublicOfferView'])
    def get(self, request):
            offer = PublicOffer.objects.all()
            if offer:
                serializer = PublicOfferSerializer(offer, many = True)
                return Response(serializer.data)
            else:
                return Response("Not found anything")


    @swagger_auto_schema(request_body=PublicOfferSerializer, tags=['PublicOffer']) 
    def post(self, request):
        admin = request.user
        if admin.is_superuser or admin.is_staff:
            serializer = PublicOfferSerializer(data = request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            else:
                return Response(serializer.errors)
        else:
            return Response("You have not such kind of permission")
        
class EditPublicOfferView(APIView):
    parser_classes = [MultiPartParser, ]
    permission_class = [IsAuthenticated]

    @swagger_auto_schema(tags=['PublicOffer'])
    def get(self, request, id):
        admin = request.user
        if admin.is_superuser or admin.is_staff:
            offer = PublicOffer.objects.filter(id = id).first()
            if offer:
                serializer = PublicOfferSerializer(offer)
                return Response(serializer.data)
            else:
                return Response("Not found anything")
        else:
            return Response("You have not such kind of permission")

    @swagger_auto_schema(request_body=PublicOfferSerializer, tags=['PublicOffer'])    
    def patch(self, request, id):
        admin = request.user
        if admin.is_superuser or admin.is_staff:
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
        else:
            return Response("You have not such kind of permission")
        

    @swagger_auto_schema(tags=['PublicOffer'])
    def delete(self, request, id):
        admin = request.user
        if admin.is_superuser or admin.is_staff:
            offer = PublicOffer.objects.filter(id = id).first()
            if offer:
                offer.delete()
                return Response("Deleted")
            else:
                return Response("Not found anything") 
        else:
            return Response("You have not such kind of permission")
        







#! MEDIA
class MediaView(APIView):
    parser_classes = [MultiPartParser, ]
    permission_class = [IsAuthenticated]

    @swagger_auto_schema(request_body=MediaSerializer, tags=['Product']) 
    def post(self, request):
        admin = request.user
        if admin.is_superuser or admin.is_staff:
            serializer = MediaSerializer(data = request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            else:
                return Response(serializer.errors)
        else:
            return Response("You have not such kind of permission")
        

class EditMediaView(APIView):
    parser_classes = [MultiPartParser, ]
    permission_class = [IsAuthenticated]

    @swagger_auto_schema(request_body=MediaSerializer, tags=['Product']) 
    def patch(self, request, id):
        admin = request.user
        if admin.is_superuser or admin.is_staff:
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
        else:
            return Response("You have not such kind of permission")
        
    @swagger_auto_schema(tags=['Product'])
    def delete(self, request, id):
        admin = request.user
        if admin.is_superuser or admin.is_staff:
            offer = Media.objects.filter(id = id).first()
            if offer:
                offer.delete()
                return Response("Deleted")
            else:
                return Response("Not found anything") 
        else:
            return Response("You have not such kind of permission")
        
    
#! PRODUCT
class ProductView(APIView):
    parser_classes = [MultiPartParser, ]
    permission_class =[IsAuthenticated]

    @swagger_auto_schema(request_body=ProodcutSerializer, tags=['Product']) 
    def post(self, request):
        admin = request.user
        if admin.is_superuser or admin.is_staff:
            serializer = ProodcutSerializer(data = request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            else:
                return Response(serializer.errors)
        else:
            return Response("You have not such kind of permission")
        
    @swagger_auto_schema(tags=['Product'])
    def get(self, request):
        products = Product.objects.all()
        if products:
            medias = Media.objects.all()
            if medias:
                for media in medias:
                    pass

class EditProductView(APIView):
    parser_classes = [MultiPartParser, ]
    permission_class = [IsAuthenticated]
    
    @swagger_auto_schema(tags=['Product'])
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
        
    @swagger_auto_schema(request_body=ProodcutSerializer, tags=['Product'])
    def patch(self, request, id):
        admin = request.user
        if admin.is_superuser or admin.is_staff:
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
        else:
            return Response("You have not such kind of permission")
        
    @swagger_auto_schema(tags=['Product'])
    def delete(self, request, id):
        admin = request.user
        if admin.is_superuser or admin.is_staff:
            product = Product.objects.filter(id = id).first()
            if product:
                product.delete()
                return Response("Deleted")
            else:
                return Response("Not found anything") 
        else:
            return Response("You have not such kind of permission")
        



