from django.shortcuts import render
from .models import Theater

def index(request):
    theater_lists = Theater.objects.all()
    return render(request, 'webapp/index.html',{'theater_lists' : theater_lists})