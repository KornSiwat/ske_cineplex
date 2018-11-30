from django import forms
from .models import Booker

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
        }
    ))
    theater = forms.CharField(max_length=10, widget=forms.TextInput(
        attrs={
            'class' : 'booking-seat black',
            'placeholder' : 'None',
        }
    ))
    class Meta:
        model = Booker
        fields = ('name', 'seat', 'theater')
        