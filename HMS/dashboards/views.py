from django.shortcuts import render
from dashboards.forms import NursesForms, DoctorForms, LabtechForms
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required
def NursePage(request):
    form = NursesForms(request.POST)
    if form.is_valid():
        print('nurse forms submitted')
        form.save()
    return render(request=request, template_name='nurses.html', context={'form': form})

def DoctorsPage(request):
    form = DoctorForms(request.POST)
    if form.is_valid():
        print("doctor form is valid")
        form.save()
    return render(request=request, template_name='doctor.html', context={'form': form})

def LabTechPage(request):
    form = LabtechForms(request.POST)
    if form.is_valid():
        print('lab forms submitted')
        form.save()
    return render(request=request, template_name='labtech.html', content_type={'form': form})