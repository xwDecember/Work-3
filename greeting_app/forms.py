from django import forms

class NameForm(forms.Form):
    name = forms.CharField(
        max_length=100,
        label='Введите ваше имя',
        widget=forms.TextInput(attrs={
            'class': 'form-input',
            'placeholder': 'Ваше имя'
        })
    )