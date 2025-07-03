from django.forms import Form, CharField, TextInput

class RegistrationForm(Form):
    login = CharField(
        widget=TextInput(
            attrs={
            "class": "form-control",
            "type": "text",
            "placeholder": "Логин"
        }))
    
    password = CharField(   
        widget=TextInput(
            attrs={
                "class": "form-control",
                "type": "text",
                "placeholder": "Пароль"
        }))