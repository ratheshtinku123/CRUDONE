from django.shortcuts import render, redirect
from .models import RegistrationData
from .forms import RegistrationForm

# Create your views here.

def getMethod(request):
    datas = RegistrationData.objects.all()
    return render(request,'ExampleFive/RegistrationTable.html',{'datas':datas})

def postMethod(request):
    post = 'post'
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/registrationApp/getData5/')
        else:
            return "<h1> Something Went Wrong </h1>"
    form = RegistrationForm
    return render (request,'ExampleFive/RegistrationForm.html',{'form':form,
                                                                'post':post})

def deleteMethod(request,id):
    datas = RegistrationData.objects.get(id=id)
    datas.delete()
    return redirect('/registrationApp/getData5/')

def updateMethod(request,id):
    update = 'update'
    datas = RegistrationData.objects.get(id=id)
    if request.method == 'POST':
        form = RegistrationForm(request.POST,instance=datas)
        if form.is_valid():
            form.save()
            return redirect('/registrationApp/getData5/')
        else:
            return "<h1> Something Went Wrong </h1>"
    form = RegistrationForm
    return render(request,'ExampleFive/RegistrationForm.html',{'form':form,
                                                               'update':update, 'id':id})

