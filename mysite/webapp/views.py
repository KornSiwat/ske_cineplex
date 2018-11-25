from django.shortcuts import render
from django.shortcuts import redirect
from .models import Theater

def default(request):
    return redirect('home/')

def home(request):
    theater_lists = Theater.objects.all()
    return render(request, 'webapp/index.html',{'theater_lists' : theater_lists, 'route' : 'Now Showing',
    })