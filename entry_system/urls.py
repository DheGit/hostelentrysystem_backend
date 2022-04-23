from django.urls import path
from . import views

app_name = "entry_system"
urlpatterns=[
    path("", views.getData, name="getData"),
    path("logentry", views.registerEntry, name="registerEntry"),
    path("logexit", views.registerExit, name="registerExit"),
    path("whosinside/<int:hostel_id>", views.getPeopleInside, name="getPeopleInside"),
]