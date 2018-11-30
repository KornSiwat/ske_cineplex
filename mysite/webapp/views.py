from django.shortcuts import render
from django.shortcuts import redirect
from .models import Theater
from .models import Movie
from .models import TicketBooker
from string import ascii_uppercase
from datetime import datetime
from .forms import CreateBooker

def default(request):
    return redirect('home/')

def home(request):
    theater_lists = Theater.objects.all()
    return render(request, 'webapp/index.html',
            {'theater_lists' : theater_lists,
            'route' : 'Now Showing',
    })

def movie(request):
    movie_lists = Movie.objects.all().order_by('name')
    return render(request, 'webapp/movie.html', 
            {'movie_lists' : movie_lists, 
            'route' : 'Movies',
    })

def movie_info(request, id):
    movie = Movie.objects.get(id=id)
    return render(request, 'webapp/movie_info.html',
            { 'movie' : movie , 
            'route' : 'Movie Info',
    })

def booking(request, id):
    theater = Theater.objects.get(id=id)
    form = CreateBooker(request.POST, instance=None)
    if request.method == 'POST':
        if form.is_valid():
            TicketBooker = form.save(commit=False)
            TicketBooker.theater = theater.theater_id
            TicketBooker.save()
            return redirect (home)
    elif request.method == "GET":
        rows = ascii_uppercase[:theater.rows]
        rows = [x for x in rows]
        rows = rows[::-1]
        day = datetime.now().day
        month = datetime.now().month
        year = datetime.now().year
        today = f'{day}, {month}, {year}'
        showtimes = ['11:40','12:30']
        booked = theater.booked_seat
        booked = booked.split(',')
        seats_list = []
        for i,row in enumerate(rows):
            seats_list.append([])
            for seat_no in range(1,theater.seats+1):
                if f'{row}{seat_no}' in booked:
                    seats_list[i].append(f'{row}booked')
                else:
                    seats_list[i].append(f'{row}{seat_no}')

        return render(request, 'webapp/booking.html',
                {   'theater' : theater , 
                    'route' : f'Seats Booking',
                    'rows' : rows,
                    'seats' : range(1,theater.seats+1),
                    'today' : today,
                    'showtimes' : showtimes,
                    'seats_list' : seats_list,
                    'form' : form
                })

def branches(request):
    return render(request, 'webapp/branches.html', { 'route': 'Branches'})

def contact(request):
    return render(request, 'webapp/contact.html', { 'route': 'Contact'})