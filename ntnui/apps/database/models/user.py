from django.db import models
from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from .enums import GENDER_CHOICES, LANGUAGE_CHOICES
from .user_manager import CustomUserManager
from datetime import date


# class UserModel(models.Model):
class UserModel(AbstractBaseUser, PermissionsMixin):
    ''' AUTHENTICATION VARIABLES '''
    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)

    ''' User details '''
    first_name = models.CharField(max_length=40)
    last_name = models.CharField(max_length=40)
    date_of_birth = models.DateField(null=True)
    gender = models.CharField(
        max_length=10, choices=GENDER_CHOICES, default="-")

    ''' Customer details '''
    # Auto-generate ntnui numbers and use as primary key
    ntnui_no = models.AutoField(primary_key=True, editable=False)

    # Customer number from SiT
    customer_no = models.CharField(
        max_length=20, unique=True)

    # Register date from SiT
    register_date = models.DateField(default=date.today)

    # Card number from SiT
    card_no = models.CharField(
        max_length=50, null=True)

    ''' Contract details '''
    contract_no = models.IntegerField(null=True)
    contract_expiry_date = models.DateField(null=True)

    ''' User preferences '''
    language = models.CharField(
        max_length=5, default="no", choices=LANGUAGE_CHOICES)

    ''' Contact details '''
    calling_code = models.IntegerField(null=True)
    phone_no = models.IntegerField(null=True)
    email = models.EmailField(
        max_length=100, verbose_name="e-mail", unique=True)

    ''' User class methods '''

    class Meta:
        ''' Configure the name displayed in the admin panel '''
        verbose_name = "User"
        verbose_name_plural = "Users"

    def __str__(self):
        return self.first_name.title() + " " + self.last_name.title()

    ''' Authentication Constraints '''

    def get_full_name(self):
        """Return the full name for the user"""
        return str(self)

    def get_short_name(self):
        """Return the short name for the user."""
        return self.first_name.title()
