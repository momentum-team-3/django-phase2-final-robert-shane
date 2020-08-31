from django.shortcuts import render
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from .models import Snippet

# Create your views here.
class list_snippet(ListView):
    model = Snippet

class view_snippet(DetailView):
    model = Snippet

class add_snippet(CreateView):
    model = Snippet

class delete_snippet(DeleteView):
    model = Snippet

class edit_snippet(UpdateView):
    model = Snippet