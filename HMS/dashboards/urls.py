from django.urls import path
from django.contrib.auth.urls import views


from . import views

urlpatterns = [
    path("doc/", views.DoctorsPage, name="doc"),
    path("nurse/", views.NursePage, name='nurse'),
    path("labtech/", views.LabTechPage, name='labtech'),
]
