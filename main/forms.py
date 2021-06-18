from .models import Ucheniki
from django.forms import ModelForm, TextInput, DateInput, Textarea


class ContactsForm(ModelForm):
    class Meta:
        model = Ucheniki
        fields = ['email', 'tel']

        widgets = {
            'email': TextInput(attrs={
                'class': 'form-control',
                'id': 'email',
                'placeholder': 'Введите ваш новый электронный адрес',
                'aria-describedby': 'emailHelp',
            }),
            'tel': TextInput(attrs={
                'class': 'form-control',
                'id': 'tel',
                'placeholder': 'Введите ваш новый номер телефона',
                'aria-describedby': 'telHelp',
            })
        }
