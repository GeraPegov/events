from django.forms import Form, CharField, TextInput

class AuthorizationForm(Form):
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

class RefreshTokenForm(Form):
    refresh_token = CharField(
        widget=TextInput(
            attrs={
                "class": "form-control",
                "type": "text",
                "placeholder": "Refresh token"
            }
        )
    )