from django.contrib import admin
from .models import Movie,Theater,Booker
# Register your models here.

admin.site.register(Movie)
admin.site.register(Theater)
admin.site.register(Booker)