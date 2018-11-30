from django import forms
from .models import TicketBooker

class CreateBooker(forms.ModelForm):
    name = forms.CharField(max_length=20, widget=forms.TextInput(
        attrs={
            'class' : 'booker-name black'
        }
    ))

    seat = forms.CharField(max_length=10, widget=forms.TextInput(
        attrs={
            'class' : 'booking-seat black',
            'placeholder' : 'None',
            'id' : 'seat-input-box'
        }
    ))
    theater = forms.CharField(max_length=10, widget=forms.TextInput(
        attrs={
            'class' : 'booking-seat black',
            'placeholder' : 'None',
        }
    ))
    class Meta:
        model = TicketBooker
        fields = ('name', 'seat', 'theater')
        