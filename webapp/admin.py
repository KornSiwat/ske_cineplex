from django.contrib import admin
from .models import Movie,Theater,TicketBooker
# Register your models here.

admin.site.register(Movie)
admin.site.register(Theater)
admin.site.register(TicketBooker)