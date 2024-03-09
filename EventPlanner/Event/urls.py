from . import views
from django.urls import path

urlpatterns = [
    path("add_event/", views.add_event),
    path("errorpage/", views.errorpage),
    path("<str:title>/", views.eventinfo),
]

