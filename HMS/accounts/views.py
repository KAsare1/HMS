from django.shortcuts import render,redirect
from .forms import NewUserForm, AuthenticationFormWithInactiveUsersOkay
from django.contrib.auth import views, login, authenticate
from django.urls import path
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt

# Create your views here

def login_request(request):
    username = request.POST.get("username")
    password = request.POST.get("password")
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return redirect('/placement/')
        ...
    else:
        print('hello')
        # Return an 'invalid login' error message.
        ...
    form = AuthenticationFormWithInactiveUsersOkay()
    return render (request=request, template_name="login.html", context={"login_form":form})

def register_request(request):
	if request.method == "POST":
		form = NewUserForm(request.POST)
		if form.is_valid():
			user = form.save()
			login(request, user)
			messages.success(request, "Registration successful." )
			return redirect("/placement/")
		messages.error(request, "Unsuccessful registration. Invalid information.")
	form = NewUserForm()
	return render (request=request, template_name="signup.html", context={"register_form":form})