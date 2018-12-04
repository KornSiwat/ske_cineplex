from django.db import models

class Movie(models.Model):
    name = models.CharField(max_length=50)
    CATEGORIES_CHOICE = (
        ('GE', 'General'),
        ('AC', 'Action'),
        ('AD', 'Adults'),
        ('AV', 'Adventure'),
        ('FS', 'Fantasy'),
        ('HR', 'Horror'),
        ('KD', 'Kids'),
    )
    categorie = models.CharField(
        max_length=2,
        choices=CATEGORIES_CHOICE,
        default='GE',
    )

    description = models.TextField(max_length=999, null=True)
    release = models.DateField()
    img = models.CharField(max_length=255, null=True)

    def __str__(self):
        return self.name

class Theater(models.Model):
    theater_id = models.CharField(max_length=10)
    movie = models.ForeignKey(Movie,on_delete=models.CASCADE)
    rows = models.PositiveIntegerField(default=9)
    seats = models.PositiveIntegerField(default=20)
    first_show = models.CharField(max_length=50, default='10:40')
    showtimes = models.CharField(max_length=50, default='10:40,12:10,13:30,14:40,16:30,17:50')

    def __str__(self):
        return f'{self.theater_id} showing: {self.movie}'


class TicketBooker(models.Model):
    name = models.CharField(max_length=30)
    tel = models.CharField(max_length=15, null=True)
    theater = models.CharField(max_length=10)
    movie = models.CharField(max_length=50, null=True)
    seat = models.CharField(max_length=255)
    showtime = models.CharField(max_length=10, default='10:40')
    date = models.CharField(max_length=50, null=True)

    def __str__(self):
        return f'{self.theater}: {self.movie} {self.date} Seat: {self.seat} Booked by {self.name} Tel:{self.tel} '
