from django.db import models

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
    release = models.DateField()
    img = models.ImageField(upload_to='img/', default='')

    def __str__(self):
        return self.name

class Theater(models.Model):
    theater_id = models.CharField(max_length=10)
    movie = models.ForeignKey(Movie,on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.theater_id} showing: {self.movie}'