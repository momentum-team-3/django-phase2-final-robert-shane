from django.urls import path
from . import views

urlpatterns = [
path("list/", views.list_snippet.as_view(), name="list_snippet"),
path("view/", views.view_snippet.as_view(), name="view_snippet"),


]