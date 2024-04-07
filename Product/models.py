from django.db import models

# Create your models here.
class Parametr(models.Model):
    name_en = models.CharField(max_length = 200, null=True, blank=True)
    name_ru = models.CharField(max_length = 200, null=True, blank=True)
    name_uz = models.CharField(max_length = 200)
    position = models.IntegerField(null=True, blank=True)
    
    def __str__(self) -> str:
        return self.name_en
    
class Category(models.Model):
    description_en = models.CharField(max_length = 200, null=True, blank=True)
    description_ru = models.CharField(max_length = 200, null=True, blank=True)
    description_uz = models.CharField(max_length = 200)
    is_active = models.BooleanField(null=True, blank=True)
    name_en = models.CharField(max_length = 200, null=True, blank=True)
    name_ru = models.CharField(max_length = 200, null=True, blank=True)
    name_uz = models.CharField(max_length = 200)
    parent_id = models.IntegerField(null=True, blank=True)
    position = models.IntegerField(null=True, blank=True)
    seo_description_en = models.CharField(max_length = 200, null=True, blank=True)
    seo_description_ru = models.CharField(max_length = 200, null=True, blank=True)
    seo_description_uz = models.CharField(max_length = 200)
    seo_title_en = models.CharField(max_length = 200, null=True, blank=True)
    seo_title_ru = models.CharField(max_length = 200, null=True, blank=True)
    seo_title_uz = models.CharField(max_length = 200)
    url = models.CharField(max_length = 200)
    image_file = models.ImageField(upload_to='category/')

    def __str__(self) -> str:
        return self.name_en
    
class News(models.Model):
    description_en = models.CharField(max_length = 200, null=True, blank=True)
    description_ru = models.CharField(max_length = 200, null=True, blank=True)
    description_uz = models.CharField(max_length = 200)
    name_en = models.CharField(max_length = 200, null=True, blank=True)
    name_ru = models.CharField(max_length = 200, null=True, blank=True)
    name_uz = models.CharField(max_length = 200)
    position = models.IntegerField(null=True, blank=True)
    image_file = models.ImageField(upload_to='news/')

    def __str__(self) -> str:
        return self.name_en
    
class Brand(models.Model):
    description_en = models.CharField(max_length = 200, null=True, blank=True)
    description_ru = models.CharField(max_length = 200, null=True, blank=True)
    description_uz = models.CharField(max_length = 200)
    is_active = models.BooleanField(null=True, blank=True)
    name_en = models.CharField(max_length = 200)
    name_ru = models.CharField(max_length = 200, null=True, blank=True)
    name_uz = models.CharField(max_length = 200, null=True, blank=True)
    letter = models.CharField(max_length = 9, blank=True, null=True)
    position = models.IntegerField(null=True, blank=True)
    seo_description = models.CharField(max_length = 200)
    seo_title = models.CharField(max_length = 200)
    image_file = models.ImageField(upload_to='brand/')

    def __str__(self) -> str:
        return self.name_en
    
    def save(self, *args, **kwargs):
        if self.name_en:
            self.letter = self.name_en[0].upper()
        super().save(*args, **kwargs)
    
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
    description_en = models.CharField(max_length = 200, null=True, blank=True)
    description_ru = models.CharField(max_length = 200, null=True, blank=True)
    description_uz = models.CharField(max_length = 200)
    name_en = models.CharField(max_length = 200, null=True, blank=True)
    name_ru = models.CharField(max_length = 200, null=True, blank=True)
    name_uz = models.CharField(max_length = 200)

    def __str__(self) -> str:
        return self.name_en
    
class Product(models.Model):
    brand_id = models.ForeignKey(Brand, on_delete = models.CASCADE)
    description_en = models.CharField(max_length = 200, null=True, blank=True)
    description_ru = models.CharField(max_length = 200, null=True, blank=True)
    description_uz = models.CharField(max_length = 200)
    is_active = models.BooleanField(null=True, blank=True)
    is_new = models.BooleanField(null=True, blank=True)
    is_top = models.BooleanField(null=True, blank=True)
    name_en = models.CharField(max_length = 200, null=True, blank=True)
    name_ru = models.CharField(max_length = 200, null=True, blank=True)
    name_uz = models.CharField(max_length = 200)
    parent_id = models.ForeignKey(Category, on_delete = models.CASCADE, null=True, blank=True)
    position = models.IntegerField(null=True, blank=True)
    price = models.FloatField()
    seo_description_en = models.CharField(max_length = 200,null=True, blank=True)
    seo_description_ru = models.CharField(max_length = 200, null=True, blank=True)
    seo_description_uz = models.CharField(max_length = 200)
    seo_title_en = models.CharField(max_length = 200, null=True, blank=True)
    seo_title_ru = models.CharField(max_length = 200, null=True, blank=True)
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







