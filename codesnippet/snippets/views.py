from django.shortcuts import render
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from .models import Snippet
from django.urls import reverse_lazy

# Create your views here.
class list_snippet(ListView):
    model = Snippet
    template_name = "snippets/list_snippet.html"

class view_snippet(DetailView):
    model = Snippet
    template_name = "snippets/view_snippet.html"

class add_snippet(CreateView):
    model = Snippet
    fields = ['title', 'body', 'description']
    template_name = "snippets/add_snippet.html"
    success_url = reverse_lazy("list_snippet")

class delete_snippet(DeleteView):
    model = Snippet
    template_name = "snippets/delete_snippet.html"
    success_url = reverse_lazy("list_snippet")

class edit_snippet(UpdateView):
    model = Snippet
    fields = ['title', 'body', 'description']
    template_name = "snippets/edit_snippet.html"
    success_url = reverse_lazy("view_snippet")