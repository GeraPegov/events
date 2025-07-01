from django.forms import Form, TextInput, CharField

class SearchNameForm(Form):
    name = CharField(
        widget=TextInput(attrs={
            "class": "form-control",
            "type": "text",
            "placeholder": "Название мероприятия",
        })
    )