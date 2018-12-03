from django import forms
from .models import TicketBooker

class CreateBooker(forms.ModelForm):
    name = forms.CharField(max_length=255, widget=forms.TextInput(
        attrs={
            'class' : 'booker-name black',
        }
    ))
    
    tel = forms.CharField(max_length=15, widget=forms.TextInput(
        attrs={
            'class' : 'booker-tel black'
        }
    ))

    seat = forms.CharField(max_length=255, widget=forms.TextInput(
        attrs={
            'class' : 'booking-seat black',
            'placeholder' : '-',
            'id' : 'seat-input-box',
            'readonly' : '',
        }
    ))

    theater = forms.CharField(max_length=255, widget=forms.TextInput(
        attrs={
            'id' : 'theater-field',
            'value' : 'hii'

        }
    ))

    movie = forms.CharField(max_length=255, widget=forms.TextInput(
        attrs={
            'id' : 'movie-field',
            'value' : 'no-movie'

        }
    ))

    showtime = forms.CharField(max_length=255, widget=forms.TextInput(
        attrs={
            'id' : 'showtime-field',
            'value' : '10:40'

        }
    ))

    date = forms.CharField(max_length=255, widget=forms.TextInput(
        attrs={
            'id' : 'date-field',
            'value' : 'today'

        }
    ))



    class Meta:
        model = TicketBooker
        fields = ('name', 'tel', 'seat', 'theater', 'movie', 'showtime','date')
        