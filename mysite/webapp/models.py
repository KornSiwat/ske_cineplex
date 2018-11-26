from django.db import models
from multiselectfield import MultiSelectField

class Movie(models.Model):
    name = models.CharField(max_length=50)
    CATEGORIES_CHOICE = (
        ('GE', 'General'),
        ('AC', 'Action'),
        ('AD', 'Adults'),
        ('AV', 'Adventure'),
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
    SEAT = (
        ('A1', 'A1'), ('A2', 'A2'), ('A3', 'A3'), ('A4', 'A5'), ('A6', 'A6'), ('A7', 'A7'), ('A8', 'A8'), ('A9', 'A9'), ('A10', 'A10'),
        ('B1', 'B1'), ('B2', 'B2'), ('B3', 'B3'), ('B4', 'B5'), ('B6', 'B6'), ('B7', 'B7'), ('B8', 'B8'), ('B9', 'B9'), ('B10', 'B10'),
        ('C1', 'C1'), ('C2', 'C2'), ('C3', 'C3'), ('C4', 'C5'), ('C6', 'C6'), ('C7', 'C7'), ('C8', 'C8'), ('C9', 'C9'), ('C10', 'C10'),
        ('D1', 'D1'), ('D2', 'D2'), ('D3', 'D3'), ('D4', 'D5'), ('D6', 'D6'), ('D7', 'D7'), ('D8', 'D8'), ('D9', 'D9'), ('D10', 'D10'),
        ('E1', 'E1'), ('E2', 'E2'), ('E3', 'E3'), ('E4', 'E5'), ('E6', 'E6'), ('E7', 'E7'), ('E8', 'E8'), ('E9', 'E9'), ('E10', 'E10'),
        ('None', 'None'),
    )
    seat = MultiSelectField(choices=SEAT, null=True)

    def __str__(self):
        return f'{self.theater_id} showing: {self.movie}'

class Booker(models.Model):
    name = models.CharField(max_length=30)
    theater = models.ForeignKey(Theater,on_delete=models.CASCADE)
    seat = models.CharField(max_length=30)

    def __str__(self):
        return self.name
