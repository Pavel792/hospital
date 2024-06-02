from .models import Articles
from django.forms import ModelForm, TextInput, DateTimeInput, Textarea


class ArticleForm(ModelForm):
    class Meta:
        model = Articles
        fields = ['num', 'name1', 'about1', 'temp1', 'date1', 'name2', 'about2', 'temp2', 'date2', 'name3', 'about3',
                  'temp3', 'date3', 'name4', 'about4', 'temp4', 'date4']

        widgets = {
            "num": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Номер'
            }),
            "name1": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Имя'
            }),
            "about1": Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Информация'
            }),
            "temp1": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Температура'
            }),
            "date1": DateTimeInput(attrs={
                'class': 'form-control'
            }),
            "name2": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Имя'
            }),
            "about2": Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Информация'
            }),
            "temp2": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Температура'
            }),
            "date2": DateTimeInput(attrs={
                'class': 'form-control'
            }),
            "name3": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Имя'
            }),
            "about3": Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Информация'
            }),
            "temp3": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Температура'
            }),
            "date3": DateTimeInput(attrs={
                'class': 'form-control'
            }),
            "name4": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Имя'
            }),
            "about4": Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Информация'
            }),
            "temp4": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Температура'
            }),
            "date4": DateTimeInput(attrs={
                'class': 'form-control'
            })
        }
