from django import forms
from .models import Manga,Game

class PostForm(forms.ModelForm):
    class Meta:
        model = Manga
        fields = ('name', 'author','genre','photo','description','vote')
        widgets = {
            'name': forms.TextInput(attrs={'class': 'fieldfumetto'}),
            'author': forms.TextInput(attrs={'class': 'fieldfumetto'}),
            'genre': forms.TextInput(attrs={'class': 'fieldfumetto'}),
            'photo': forms.FileInput(attrs={'onchange': "load_image(value);"}),
            'description': forms.Textarea(attrs={'class': 'fieldfumetto'}),
            'vote': forms.Select(attrs={'class': 'fieldfumetto'}),

        }

class GameForm(forms.ModelForm):
    class Meta:
        model = Game
        fields = ('name', 'product_factory','genre','photo','description','vote')
        widgets = {
            'name': forms.TextInput(attrs={'class': 'fieldfumetto'}),
            'product_factory': forms.TextInput(attrs={'class': 'fieldfumetto','required':False}),
            'genre': forms.TextInput(attrs={'class': 'fieldfumetto'}),
            'photo': forms.FileInput(attrs={'onchange': "load_image(value);"}),
            'description': forms.Textarea(attrs={'class': 'fieldfumetto'}),
            'vote': forms.Select(attrs={'class': 'fieldfumetto'}),

        }
