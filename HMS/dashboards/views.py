from django.shortcuts import redirect, render
from dashboards.forms import NursesForms, DoctorForms, LabtechForms, AppointmentForms, RegisterForms, DocCheckIn, PharmacistForms
from django.contrib.auth.decorators import login_required
from .decorators import allowed_users
from .models import Appointment
# Create your views here.

@login_required
@allowed_users(allowed_roles=['Nurse'])
def NursePage(request):
    form = NursesForms(request.POST)
    if form.is_valid():
        print('nurse forms submitted1')
        form.save()
    return render(request, 'nurses.html', {'form': form})

@login_required
@allowed_users(allowed_roles=['Doctor'])
def DoctorsPage(request):
    form = DoctorForms(request.POST)
    if form.is_valid():
        print("doctor form is valid1")
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
@allowed_users(allowed_roles=['Pharmacist'])
def Pharmacist(request):
    form = PharmacistForms(request.POST)
    if form.is_valid():
        form.save()
    return render(request, 'pharmacist.html', {'form': form})

@login_required
def home_index(request):
    context = {}
    return render(request,'index.html', context)

def fde(request):
    context = {}
    return render(request,'fde.html', context)

def appointmentPage(request):
    form = AppointmentForms(request.POST)
    appointments = Appointment.objects.all
    if form.is_valid():
        form.save()
    return render(request, 'appointments.html', {'form': form, 'appointments': appointments})

def PatientReg(request):
    form = RegisterForms(request.POST)
    if form.is_valid():
        form.save()
    return render(request, 'register.html', {'form': form})

def check_inPage(request):
    form = DocCheckIn(request.POST)
    if form.is_valid():
        form.save()
    else:
        print('hello')
    return render(request, 'check_in.html', {'form': form})

