from django.db import models

# Create your models here.
class About(models.Model):
    description_en = models.CharField(max_length = 200)
    description_ru = models.CharField(max_length = 200)
    description_uz = models.CharField(max_length = 200)
    name_en = models.CharField(max_length = 200)
    name_ru = models.CharField(max_length = 200)
    name_uz = models.CharField(max_length = 200)
    position = models.CharField(max_length = 200)
    type = models.CharField(max_length = 200)
    image_file = models.ImageField(upload_to='about/')

    def __str__(self) -> str:
        return self.name_en