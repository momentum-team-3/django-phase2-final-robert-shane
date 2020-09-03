from django.forms import ModelForm, Form, ChoiceField, CharField
from .models import Snippet

class Snippet_Form(ModelForm):
    class Meta:
        model = Snippet
        fields = [
            'title',
            'body',
            'language',
        ]

class SearchForm(Form):
    title = CharField(label="Snippet Title", required=False)
    body = CharField(label="Snippet Body", required=False)
    language = CharField(label="Code Language", required=False)


