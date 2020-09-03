from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Snippet
from django.urls import reverse_lazy
import copy
from .forms import Snippet_Form, SearchForm

# Create your views here.
class list_snippet(ListView):
    model = Snippet
    template_name = "snippets/list_snippet.html"


class list_user_snippet(LoginRequiredMixin, ListView):
    login_url = "login_user"
    model = Snippet
    template_name = "snippets/list_user_snippet.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["object_list"] = Snippet.objects.filter(self.request.user==object.snippet_of)

    
class view_snippet(DetailView):
    model = Snippet
    template_name = "snippets/view_snippet.html"


class add_snippet(LoginRequiredMixin, CreateView):
    login_url = "login_user"
    model = Snippet
    fields = ['title', 'body', 'language']
    template_name = "snippets/add_snippet.html"
    success_url = reverse_lazy("list_snippet")

class delete_snippet(LoginRequiredMixin, DeleteView):
    login_url = "login_user"
    model = Snippet
    template_name = "snippets/delete_snippet.html"
    success_url = reverse_lazy("list_snippet")

class edit_snippet(LoginRequiredMixin, UpdateView):
    login_url = "login_user"
    model = Snippet
    fields = ['title', 'body', 'language']
    template_name = "snippets/edit_snippet.html"
    def get_success_url (self):
        return f"/snippets/view/{self.kwargs['pk']}"


def copy_snippet(request, pk):
    snippet = Snippet.objects.get(pk)
    copy = copy.deepcopy(snippet)
    if request.method == "GET":
        form = Snippet_Form(instance=snippet)
    else:
        form = Snippet_Form(data=request.POST, instance=copy)
        if form.is_valid():
            form.save()
            return redirect("list_user_snippet")
    return render(request, "snippets/copy_snippet.html", {
        "form": form,
        "copy": copy
    })


def search_snippet(request):
    if request.method == "GET":
        form = SearchForm()
        return render(request, "snippets/search_snippet.html", {"form": form})
    else:
        title_search = request.POST["title"]
        body_search = request.POST["body"]
        language_search = request.POST["language"]
        if title_search:
            results = Snippet.objects.filter(title__contains=title_search)
        elif body_search:
            results = Snippet.objects.filter(body__contains=body_search)
        elif language_search:
            results = Snippet.objects.filter(language__contains=language_search)
        return render(request, "snippets/search_results.html", {"results": results})
        