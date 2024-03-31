from django.db import models

# Create your models here.
class Parametr(models.Model):
    name_en = models.CharField(max_length = 200)
    name_ru = models.CharField(max_length = 200)
    name_uz = models.CharField(max_length = 200)
    position = models.IntegerField()
    
    def __str__(self) -> str:
        return self.name_en
    
class Category(models.Model):
    description_en = models.CharField(max_length = 200)
    description_ru = models.CharField(max_length = 200)
    description_uz = models.CharField(max_length = 200)
    is_active = models.BooleanField()
    name_en = models.CharField(max_length = 200)
    name_ru = models.CharField(max_length = 200)
    name_uz = models.CharField(max_length = 200)
    parent_id = models.IntegerField()
    position = models.IntegerField()
    seo_description_en = models.CharField(max_length = 200)
    seo_description_ru = models.CharField(max_length = 200)
    seo_description_uz = models.CharField(max_length = 200)
    seo_title_en = models.CharField(max_length = 200)
    seo_title_ru = models.CharField(max_length = 200)
    seo_title_uz = models.CharField(max_length = 200)
    url = models.CharField(max_length = 200)
    image_file = models.ImageField(upload_to='category/')

    def __str__(self) -> str:
        return self.name_en
    
class News(models.Model):
    description_en = models.CharField(max_length = 200)
    description_ru = models.CharField(max_length = 200)
    description_uz = models.CharField(max_length = 200)
    name_en = models.CharField(max_length = 200)
    name_ru = models.CharField(max_length = 200)
    name_uz = models.CharField(max_length = 200)
    position = models.IntegerField()
    image_file = models.ImageField(upload_to='news/')

    def __str__(self) -> str:
        return self.name_en
    
class Brand(models.Model):
    description_en = models.CharField(max_length = 200)
    description_ru = models.CharField(max_length = 200)
    description_uz = models.CharField(max_length = 200)
    is_active = models.BooleanField()
    name_en = models.CharField(max_length = 200)
    name_ru = models.CharField(max_length = 200)
    name_uz = models.CharField(max_length = 200)
    letter = models.CharField(max_length = 9)
    position = models.IntegerField()
    seo_description = models.CharField(max_length = 200)
    seo_title = models.CharField(max_length = 200)
    image_file = models.ImageField(upload_to='brand/')

    def __str__(self) -> str:
        return self.name_en
    
class Contact(models.Model):
     address = models.CharField(max_length = 200) 
     email = models.CharField(max_length = 200)
     is_main = models.BooleanField()
     latitude = models.CharField(max_length = 200)
     longitude = models.CharField(max_length = 200)
     name_en = models.CharField(max_length = 200)
     name_ru = models.CharField(max_length = 200)
     name_uz = models.CharField(max_length = 200)
     phone = models.CharField(max_length = 200)
     working_hours = models.CharField(max_length = 200)

     def __str__(self) -> str:
         return self.name_en
     
class PublicOffer(models.Model):
    description_en = models.CharField(max_length = 200)
    description_ru = models.CharField(max_length = 200)
    description_uz = models.CharField(max_length = 200)
    name_en = models.CharField(max_length = 200)
    name_ru = models.CharField(max_length = 200)
    name_uz = models.CharField(max_length = 200)

    def __str__(self) -> str:
        return self.name_en
    
class Product(models.Model):
    brand_id = models.ForeignKey(Brand, on_delete = models.CASCADE)
    description_en = models.CharField(max_length = 200)
    description_ru = models.CharField(max_length = 200)
    description_uz = models.CharField(max_length = 200)
    is_active = models.BooleanField()
    is_new = models.BooleanField()
    is_top = models.BooleanField()
    name_en = models.CharField(max_length = 200)
    name_ru = models.CharField(max_length = 200)
    name_uz = models.CharField(max_length = 200)
    parent_id = models.ForeignKey(Category, on_delete = models.CASCADE)
    position = models.IntegerField()
    price = models.FloatField()
    seo_description_en = models.CharField(max_length = 200)
    seo_description_ru = models.CharField(max_length = 200)
    seo_description_uz = models.CharField(max_length = 200)
    seo_title_en = models.CharField(max_length = 200)
    seo_title_ru = models.CharField(max_length = 200)
    seo_title_uz = models.CharField(max_length = 200)
    url = models.CharField(max_length = 200)
    image_file = models.ImageField(upload_to='product/')

    def __str__(self) -> str:
        return self.name_en
    

class Media(models.Model):
    product_id = models.ForeignKey(Product, on_delete = models.CASCADE)
    position = models.IntegerField()
    type = models.CharField(max_length = 200)
    file = models.ImageField(upload_to='product/')

    def __str__(self) -> str:
        return self.type







