from django.urls import path
from . import views

app_name = "entry_system"
urlpatterns=[
    path("", views.getData, name="getData"),
]