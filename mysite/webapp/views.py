from django.shortcuts import render
from django.shortcuts import redirect
from .models import Theater, Movie

def default(request):
    return redirect('home/')

def home(request):
    theater_lists = Theater.objects.all()
    return render(request, 'webapp/index.html',{'theater_lists' : theater_lists, 'route' : 'Now Showing',
    })

def movie(request):
    movie_lists = Movie.objects.all().order_by('name')
    return render(request, 'webapp/movie.html',{'movie_lists' : movie_lists, 'route' : 'Movies',
    })

def movie_info(request, id):
    movie = Movie.objects.get(id=id)
    return render(request, 'webapp/movie_info.html',{ 'movie' : movie , 'route' : 'Movie Info'
    })