from django.urls import path
from . import views

urlpatterns = [
path("", views.snippet_test, name="snippet_test"),
]