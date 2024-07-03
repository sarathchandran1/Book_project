from django import forms
from.models import Book,Auther


class Autherform(forms.ModelForm):
    class Meta:

        model = Auther
        fields = ['name']

        widgets={
           'title':forms.TextInput(attrs={'class':'form-control','placeholder':'enter the auther'}) 
        }


class Bookform(forms.ModelForm):
    class Meta:

        model = Book
        fields = '__all__'

        widgets={
           
         'title':forms.TextInput(attrs={'class':'form-control','placeholder':'enter the book name'}),
         'auther':forms.Select(attrs={'class':'form-control','placeholder':'enter the book auther'}),
         'price':forms.NumberInput(attrs={'class':'form-control','placeholder':'enter the book price'})
        }


    
