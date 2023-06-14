from django.urls import path
from django.contrib.auth.urls import views


from . import views

urlpatterns = [
    path("login/", views.login_request, name="login"),
    path("register/", views.register_request, name="register"),
]