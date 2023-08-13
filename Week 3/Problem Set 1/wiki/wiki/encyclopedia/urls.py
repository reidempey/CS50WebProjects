from django.urls import path

from . import views


urlpatterns = [
    path("", views.index, name="index"),
    path("random_entry", views.random_entry, name="random_entry"),
    path("<str:entry>", views.entries, name="entries")
]
