from django.contrib import admin
from .models import *

# Register your models here.

@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    pass

@admin.register(Movie) 
class MovieAdmin(admin.ModelAdmin):
    pass