from django import forms
from .models import TicketBooker

class CreateBooker(forms.ModelForm):
    name = forms.CharField(max_length=255, widget=forms.TextInput(
        attrs={
            'class' : 'booker-name black'
        }
    ))

    seat = forms.CharField(max_length=255, widget=forms.TextInput(
        attrs={
            'class' : 'booking-seat black',
            'placeholder' : 'None',
            'id' : 'seat-input-box',
            'readonly' : '',
        }
    ))

    theater = forms.CharField(max_length=255, widget=forms.TextInput(
        attrs={
            'class' : 'booking-seat black',
            'placeholder' : 'None',
            'id' : 'theater-field',
            'value' : 'hii'

        }
    ))
    class Meta:
        model = TicketBooker
        fields = ('name', 'seat', 'theater')
        