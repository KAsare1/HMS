from django.urls import path
from django.contrib.auth.urls import views


from . import views

urlpatterns = [
    path("", views.DoctorsPage, name="doc"),
]
