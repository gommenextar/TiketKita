from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("flights/", views.category_page, {"mode": "flight"}, name="flights"),
    path("trains/", views.category_page, {"mode": "train"}, name="trains"),
    path("ships/", views.category_page, {"mode": "ship"}, name="ships"),
    path("hotels/", views.category_page, {"mode": "hotel"}, name="hotels"),
    path("trips/<str:mode>/<int:ticket_id>/", views.trip_detail, name="trip_detail"),
    path("api/tickets/", views.ticket_api, name="ticket_api"),
]
