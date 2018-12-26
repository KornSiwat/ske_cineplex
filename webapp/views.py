from django.shortcuts import render
from django.shortcuts import redirect
from .models import Theater
from .models import Movie
from .models import TicketBooker as TicketBookerModel
from string import ascii_uppercase
from datetime import datetime
from .forms import CreateBooker

def default(request):
    return redirect('home/')

def home(request):
    theater_lists = Theater.objects.all()
    return render(request, 'webapp/home.html',
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

def flatten(input):
    new_list = []
    for i in input:
        if isinstance(i, str) == True:
            new_list.append(i)
        else:
            for j in i:
                new_list.append(j)
    return new_list

def update_seat(request, id, showtime):
    theater = Theater.objects.get(id=id)
    day = datetime.now().day
    month = datetime.now().month
    year = datetime.now().year
    today = f'{day}/{month}/{year}'
    rawbooked = list(TicketBookerModel.objects.filter(theater=theater.theater_id,showtime=showtime,date=today).values_list('seat', flat=True))
    booked = []
    for i in rawbooked:
        if ',' in i:
            booked.append(i.split(','))
        else:
            booked.append(i)
    booked = flatten(booked)
    rows = ascii_uppercase[:theater.rows]
    rows = [x for x in rows]
    rows = rows[::-1]
    showtimes = theater.showtimes.split(',')
    seats_list = []
    for i,row in enumerate(rows):
        seats_list.append([])
        for seat_no in range(1,theater.seats+1):
            if f'{row}{seat_no}' in booked:
                seats_list[i].append(f'{row}booked')
            else:
                seats_list[i].append(f'{row}{seat_no}')
    return render(request, 'webapp/includes/seat_selection.html',
                {   'rows' : rows,
                    'seats' : range(1,theater.seats+1),
                    'showtimes' : showtimes,
                    'seats_list' : seats_list,})

def booking(request, id):
    theater = Theater.objects.get(id=id)
    form = CreateBooker(request.POST)
    day = datetime.now().day
    month = datetime.now().month
    year = datetime.now().year
    today = f'{day}/{month}/{year}'
    if request.method == 'POST':
        if form.is_valid():
            TicketBooker = form.save(commit=False)
            TicketBooker.theater = theater.theater_id
            TicketBooker.save()
            return redirect(home)
        else:
            return render(request, 'webapp/includes/error.html')
    elif request.method == "GET":
        theater = Theater.objects.get(id=id)
        rawbooked = list(TicketBookerModel.objects.filter(theater=theater.theater_id,showtime=theater.first_show,date=today).values_list('seat', flat=True))
        booked = []
        for i in rawbooked:
            if ',' in i:
                booked.append(i.split(','))
            else:
                booked.append(i)
        booked = flatten(booked)
        rows = ascii_uppercase[:theater.rows]
        rows = [x for x in rows]
        rows = rows[::-1]
        first_show = theater.first_show
        showtimes = theater.showtimes.split(',')
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
                    'first_show' : first_show,
                    'showtimes' : showtimes,
                    'seats_list' : seats_list,
                    'form' : form,
                })

def history(request):
    return render(request, 'webapp/history.html',{
        'route' : 'History',
    })

def update_history(request, name, tel):
    try:
        history = TicketBookerModel.objects.filter(name=name,tel=tel).order_by('date','showtime')
    except TicketBookerModel.DoesNotExist:
        history = 'Not Found'
    return render(request, 'webapp/includes/history_detail.html', {
        'history' : history,
    })

def branches(request):
    return render(request, 'webapp/branches.html', { 'route': 'Branches'})

def contact(request):
    return render(request, 'webapp/contact.html', { 'route': 'Contact'})