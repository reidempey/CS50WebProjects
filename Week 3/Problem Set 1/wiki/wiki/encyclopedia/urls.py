from django.urls import path

from . import views


urlpatterns = [
    path("", views.index, name="index"),
    path("random_entry", views.random_entry, name="random_entry"),
    path("search", views.search, name="search"),
    path("new", views.new, name="new"),
    path("edit", views.edit, name="edit"),
    path("edit/<str:entry>", views.edit_entry, name="edit_entry"),
    path("<str:entry>", views.entries, name="entries")
]
