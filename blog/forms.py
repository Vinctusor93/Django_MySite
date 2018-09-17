from django import forms
from .models import Manga,Game

class PostForm(forms.ModelForm):
    class Meta:
        model = Manga
        fields = ('name', 'author','year_release','genre','photo','description','status','vote',)
        widgets = {
            'name': forms.TextInput(attrs={'class': 'fieldfumetto'}),
            'author': forms.TextInput(attrs={'class': 'fieldfumetto'}),
            'genre': forms.TextInput(attrs={'class': 'fieldfumetto'}),
            'year_release': forms.NumberInput(attrs={'class': 'fieldfumetto'}),
            'status': forms.Select(attrs={'class': 'fieldfumetto'}),
            'description': forms.Textarea(attrs={'class': 'fieldfumetto'}),
            'vote': forms.Select(attrs={'class': 'fieldfumetto'}),

        }

class GameForm(forms.ModelForm):
    class Meta:
        model = Game
        fields = ('name', 'product_factory','year_release','play_station','genre','photo','description','vote')
        widgets = {
            'name': forms.TextInput(attrs={'class': 'fieldfumetto'}),
            'product_factory': forms.TextInput(attrs={'class': 'fieldfumetto','required':False}),
            'genre': forms.TextInput(attrs={'class': 'fieldfumetto'}),
            'year_release': forms.NumberInput(attrs={'class': 'fieldfumetto'}),
            'play_station': forms.TextInput(attrs={'class': 'fieldfumetto'}),
            'description': forms.Textarea(attrs={'class': 'fieldfumetto'}),
            'vote': forms.Select(attrs={'class': 'fieldfumetto'}),
        }



