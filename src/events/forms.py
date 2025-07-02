from django.forms import CharField, Form, TextInput


class SearchNameForm(Form):
    name = CharField(
        widget=TextInput(
            attrs={
                "class": "form-control",
                "type": "text",
                "placeholder": "Название мероприятия",
            }
        )
    )
