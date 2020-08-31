from django.urls import path
from . import views

urlpatterns = [
    path("", views.user_test, name="user_test"),
]