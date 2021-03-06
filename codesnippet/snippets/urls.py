from django.urls import path
from . import views

urlpatterns = [
path("list/", views.list_snippet.as_view(), name="list_snippet"),
path("view/<int:pk>", views.view_snippet.as_view(), name="view_snippet"),
path("add/", views.add_snippet, name="add_snippet"),
path("edit/<int:pk>", views.edit_snippet.as_view(), name="edit_snippet"),
path("delete/<int:pk>", views.delete_snippet.as_view(), name="delete_snippet"),
path("listuser/", views.list_user_snippet.as_view(), name="list_user_snippet"),
path("copy/<int:pk>", views.copy_snippet, name="copy_snippet"),
path("search/", views.search_snippet, name="search_snippet"),
]