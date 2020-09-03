from django.forms import ModelForm, Form, ChoiceField, CharField
from .models import Snippet

class Snippet_Form(ModelForm):
    class Meta:
        model = Snippet
        fields = [
            'title',
            'body',
            'description',
            'tags',
        ]

class SearchForm(Form):
    search_type = (("includes", "includes"), ("starts with", "starts with"), ("exact match", "exact match"))
    title = CharField(label="Snippet Title")
    title_search = ChoiceField(label="Search title by", choices=search_type, initial="includes")
    body = CharField(label="Snippet Body")
    body_search = ChoiceField(label="Search body by", choices=search_type, initial="includes")
    language = CharField(label="Code Language")
    language_search = ChoiceField(label="Search by code language", choices=search_type, initial="exact match")


