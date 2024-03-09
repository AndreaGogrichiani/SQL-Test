from . import views
from django.urls import path

urlpatterns = [
    path("errorpage/", views.errorpage),
    path("<str:title>/", views.eventinfo, name='eventinfo'),
]

