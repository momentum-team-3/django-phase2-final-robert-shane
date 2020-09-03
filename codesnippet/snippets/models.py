from django.db.models import Model, CharField, TextField, ManyToManyField, ForeignKey, CASCADE
from users.models import User

# Create your models here.
class Snippet(Model):
    title = CharField(max_length=200, null=False, blank=False)
    body = TextField(null=False, blank=False)
    description = TextField(null=True, blank=True)
    language = CharField(max_length=50, default="HTML", null=False, blank=False)
    tags = ManyToManyField("Tag")
    snippet_of = ForeignKey(User, on_delete=CASCADE, blank=True, null=True)

class Tag(Model):
    tagname = CharField(max_length=255, null=False, unique=True)
    snippets = ManyToManyField("Snippet")

    