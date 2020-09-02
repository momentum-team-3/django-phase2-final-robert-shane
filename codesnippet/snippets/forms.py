from django.forms import ModelForm
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
