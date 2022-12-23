from django.db import models
from django.urls import reverse
from django.core.mail import send_mail

from django.contrib.auth.models import (AbstractBaseUser, BaseUserManager, PermissionsMixin)
from django.utils.translation import gettext_lazy as _

class CustomAccountManager(BaseUserManager):
    def create_superuser(self, email, user_name, password, **other_fields):
        other_fields.setdefault('is_staff', True)
        other_fields.setdefault('is_superuser', True)
        other_fields.setdefault('is_active', True)
        if other_fields.get('is_staff') is not True:
            raise ValueError(
                'Superuser must be assigned to is_staff=True.')
        if other_fields.get('is_superuser') is not True:
            raise ValueError(
                'Superuser must be assigned to is_superuser=True.')
        return self.create_user(email, user_name, password, **other_fields)
    def create_user(self, email, user_name, password, **other_fields):
        if not email:
            raise ValueError(_('You must provide an email address'))
        email = self.normalize_email(email)
        user = self.model(email=email, user_name=user_name,
                          **other_fields)
        user.set_password(password)
        user.save()
        return user


class UserBase(AbstractBaseUser, PermissionsMixin):
    first_name = models.CharField(max_length=200, blank=False)
    last_name = models.CharField(max_length=200, blank=True)
    email = models.EmailField(_('email address'), unique=True)
    user_name = models.CharField(max_length=150, unique=True, blank=True)
    phone_number = models.CharField(max_length=15, blank=True)
    image = models.ImageField(upload_to='accounts_avatars/', blank=True)
    is_active = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_partner = models.BooleanField(default=False)
    age_verified = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    objects = CustomAccountManager()
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["user_name"]
    class Meta:
        verbose_name = "Accounts"
        verbose_name_plural = "Accounts"
    def __str__(self):
        name = f"{self.first_name} {self.last_name}"
        if (len(name) > 1):
            return name
        else:
            return self.email or self.user_name

# Create your models here.
class Music(models.Model):
    title = models.CharField(max_length=30, blank = False)
    content = models.TextField(blank=True)
    image = models.ImageField(blank=True)
    time_created = models.DateTimeField(auto_now=False, auto_now_add=True)
    time_updated = models.DateTimeField(auto_now=True, auto_now_add=False)
    genre = models.ManyToManyField("Genre",blank = True)

    def __str__(self):
        return str(self.title)
    
    def get_absolute_url(self):
        return reverse("detail_view", kwargs={"pk":self.id})

class Genre(models.Model):
    title_genre = models.CharField(max_length=100,blank = True)

    def __str__(self):
        return str(self.title_genre)

# Music ->