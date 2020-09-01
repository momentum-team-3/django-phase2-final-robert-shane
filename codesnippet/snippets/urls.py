from django.urls import path
from . import views

urlpatterns = [
path("list/", views.list_snippet.as_view(), name="list_snippet"),
path("view/<int:pk>", views.view_snippet.as_view(), name="view_snippet"),
path("add/", views.add_snippet.as_view(), name="add_snippet"),


]