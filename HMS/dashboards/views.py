from django.shortcuts import render
from dashboards.forms import NursesForms, DoctorForms, LabtechForms
from django.contrib.auth.decorators import login_required
from .decorators import allowed_users
from django import template
# Create your views here.

@login_required
@allowed_users(allowed_roles=['Nurse'])
def NursePage(request):
    form = NursesForms(request.POST)
    if form.is_valid():
        print('nurse forms submitted')
        form.save()
    return render(request, 'nurses.html', {'form': form})

@login_required
@allowed_users(allowed_roles=['Doctor'])
def DoctorsPage(request):
    form = DoctorForms(request.POST)
    if form.is_valid():
        print("doctor form is valid")
        form.save()
    return render(request, 'doctor.html', {'form': form})

@login_required
@allowed_users(allowed_roles=['Lab technician'])
def LabTechPage(request):
    form = LabtechForms(request.POST)
    if form.is_valid():
        print('lab forms submitted')
        form.save()
    return render(request, 'labtech.html', {'form': form})

@login_required
def home_index(request):
    context = {}
    return render(request,'index.html', context)



register = template.Library() 
@register.filter(name='has_group') 
def has_group(user, group_name):
    return user.groups.filter(name=group_name).exists() 