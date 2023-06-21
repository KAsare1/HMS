from django.shortcuts import render,redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm

def login_request(request):
    username = request.POST.get("username")
    password = request.POST.get("password")
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return redirect('/dashboards/')
        ...
    else:
        print('hello')
        # Return an 'invalid login' error message.
        ...
    form = AuthenticationForm()
    return render(request, 'login.html', {'form':form})
