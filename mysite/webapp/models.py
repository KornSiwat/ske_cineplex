from django.db import models
from multiselectfield import MultiSelectField

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
    img = models.ImageField(upload_to='img/', default='')

    def __str__(self):
        return self.name

class Theater(models.Model):
    theater_id = models.CharField(max_length=10)
    movie = models.ForeignKey(Movie,on_delete=models.CASCADE)
    rows = models.PositiveIntegerField(default=9)
    seats = models.PositiveIntegerField(default=20)
    booked_seat = models.TextField(max_length=999, null=True,blank=True)

    def __str__(self):
        return f'{self.theater_id} showing: {self.movie}'

class Booker(models.Model):
    name = models.CharField(max_length=30)
    theater = models.ForeignKey(Theater,on_delete=models.CASCADE)
    seat = models.CharField(max_length=30)

    def __str__(self):
        return self.name
