from django.shortcuts import render,redirect

from .forms import AppointmentForm
from .models import AppointmentData

# Create your views here.

def getMethod(request):
    details = AppointmentData.objects.all()
    return render(request,'ExampleTwo/AppointmentTable.html',{'details':details})

def postMethod(request):
    post = 'post'
    if request.method == 'POST':
        form = AppointmentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/appointmentApp/getData2/')
        else:
            return "<h1> Something Went Wrong </h1>"
    form = AppointmentForm
    return render(request,'ExampleTwo/AppointmentForm.html',{'form':form,'post':post})

def deleteMethod(request,id):
    details = AppointmentData.objects.get(id=id)
    details.delete()
    return redirect('/appointmentApp/getData2/')

def updateMethod(request,id):
    update = 'update'
    details = AppointmentData.objects.get(id=id)
    if request.method == 'POST':
        form = AppointmentForm(request.POST,instance=details)
        if form.is_valid():
            form.save()
            return redirect('/appointmentApp/getData2/')
        else:
            return "<h1> Something Went Wrong </h1>"

    form = AppointmentForm
    return render(request,'ExampleTwo/AppointmentForm.html',{'form':form,
                                                             'update':update,'id':id})