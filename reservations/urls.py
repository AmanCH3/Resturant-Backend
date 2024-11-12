from django.urls import path
from . import views


urlpatterns = [
    path('reservations/', views.ReservationListCreate.as_view(), name='reservations-list-create'),
]