from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("api/tickets/", views.ticket_api, name="ticket_api"),
]
