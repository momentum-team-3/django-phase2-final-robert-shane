from django.db.models import Model, CharField, TextField, ManyToManyField

# Create your models here.
class Snippet(Model):
    title = CharField(max_length=200, null=False, blank=False)
    body = TextField(null=False, blank=False)
    description = TextField(null=True, blank=True)
    tags = ManyToManyField("Tag")

class Tag(Model):
    tagname = CharField(max_length=255, null=False, unique=True)
    snippets = ManyToManyField("Snippet")

    