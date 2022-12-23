from django.contrib import admin
from .models import Music
from .models import Genre
# Register your models here.
admin.site.register(Music)
admin.site.register(Genre)