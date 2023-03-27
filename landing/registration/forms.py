from .models import Captain
from django.forms import ModelForm, TextInput, Textarea, IntegerField

class RegisterForm(ModelForm):
    class Meta:
        model = Captain
        fields = ["name_surname", "pro_potok", "name_surname1", "name_surname2", "name_surname3", "name_surname4", "name_surname5", "pro_potok1", "pro_potok1", "pro_potok2", "pro_potok3", "pro_potok4", "pro_potok5"]
        widgets = {"name_surname": TextInput(attrs={'class': 'form-control', 'placeholder': 'Имя и фамилия (Иванов Иван)'}),
                   "name_surname1": TextInput(attrs={'class': 'form-control', 'placeholder': 'Имя и фамилия (Иванов Иван)'}),
                   "name_surname2": TextInput(attrs={'class': 'form-control', 'placeholder': 'Имя и фамилия (Иванов Иван)'}),
                   "name_surname3": TextInput(attrs={'class': 'form-control', 'placeholder': 'Имя и фамилия (Иванов Иван)'}),
                   "name_surname4": TextInput(attrs={'class': 'form-control', 'placeholder': 'Имя и фамилия (Иванов Иван)'}),
                   "name_surname5": TextInput(attrs={'class': 'form-control', 'placeholder': 'Имя и фамилия (Иванов Иван)'}),
                   }
