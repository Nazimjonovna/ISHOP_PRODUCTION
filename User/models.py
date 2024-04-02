from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from User.managers import CustomUserManager
from django.core.validators import RegexValidator
from django.core.exceptions import ValidationError
from django.core.validators import MinLengthValidator

# Create your models here.
class User(AbstractBaseUser, PermissionsMixin):
    phone_regex = RegexValidator(regex='d{0,9}', message="Telefon raqamini +998XXXXXXXXX kabi kiriting!")
    phone = models.CharField(validators=[phone_regex], max_length=9, unique=True)
    otp = models.CharField(max_length=4, null=True)
    name = models.CharField(max_length=200)
    password = models.CharField(max_length=1000, validators=[MinLengthValidator(6)])
    is_user = models.BooleanField(default=True)
    is_superadmin = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    is_partner = models.BooleanField(default=False)

    is_staff = models.BooleanField(default=True)
    is_active = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = CustomUserManager()

    USERNAME_FIELD = 'phone'
    EMAIL_FIELD = None

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'

    def __str__(self):
        return self.phone

    def has_perm(self, perm, obj=None):
        return self.is_superuser

    def has_module_perms(self, app_label):
        return self.is_superuser


class Client(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE, null = True, blank = True)
    last_name = models.CharField(max_length=200)
    card = models.IntegerField(null = True)
    card_info = models.CharField(max_length=4, null = True)
    password = models.CharField(max_length=200)
    paspord_raqam = models.CharField(max_length=6, null=True)
    paspord_seria = models.CharField(max_length=3, null=True)
    paspord = models.ImageField(upload_to='pasportlar/', null=True)
    image = models.ImageField(upload_to='rasmlar/', null=True)
    adress = models.TextField(null=True)
    vil = (
        ('Toshkent', 'Toshkent'),
        ('Navoiy', 'Navoiy'),
        ('Buxoro', 'Buxoro'),
        ('Samarqand', 'Samarqand'),
        ('Jizzax', 'Jizzax'),
        ('Xorazm', 'Xorazm'),
        ('Sirdaryo', 'Sirdaryo'),
        ('Namangan', 'Namangan'),
        ("Farg'ona", "Farg'ona"),
        ('Andijon', 'Andijon'),
        ('Qashqadaryo', 'Qashqadaryo'),
        ('Surxandaryo', 'Surxandaryo'),
        ('Nukus', 'Nukus')
    )
    viloyat = models.CharField(max_length=200, choices=vil, null=True)

    class Meta:
        ordering = ['id']

    def __str__(self):
        if self.user and self.user.name:
            return f"{self.user.name}'s Client"
        return "Client"


class ValidatedOtp(models.Model):
    phone_regex = RegexValidator(regex='d{0,9}', message="Telefon raqamini +9989XXXXXXXX kabi kiriting!")
    phone = models.CharField(validators=[phone_regex],max_length=9,unique=True)
    otp = models.CharField(max_length=9, blank=True, null=True)
    count = models.IntegerField(default=0, help_text='Kodni kiritishlar soni:')
    validated = models.BooleanField(default=False, help_text="Shaxsiy kabinetingizni yaratishingiz mumkin!")

    def __str__(self):
        return str(self.phone)

class Verification(models.Model):
    STATUS = (
        ('send', 'send'),
        ('confirmed', 'confirmed'),
    )
    phone = models.CharField(max_length=9, unique=True)
    verify_code = models.SmallIntegerField()
    is_verified = models.BooleanField(default=False)
    step_reset = models.CharField(max_length=10, null=True, blank=True, choices=STATUS)
    step_change_phone = models.CharField(max_length=30, null=True, blank=True, choices=STATUS)

    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.phone} --- {self.verify_code}"

    