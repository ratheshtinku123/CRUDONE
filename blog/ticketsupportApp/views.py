from django.shortcuts import render,redirect
from .models import TicketTracker
from .forms import TicketTrackerForm

# Create your views here.


def getMethod(request):
        details = TicketTracker.objects.all()
        return render(request, "ExampleThree/TicketTable.html", {"details":details})

def postMethod(request):
    post = 'post'
    if request.method == 'POST':
        form = TicketTrackerForm(request.POST)
        if(form.is_valid()):
            form.save()
            return redirect('/ticketsupportApp/getData3/')
        else:
            return "<h1> Something Went Wrong </h1>"
    form = TicketTrackerForm
    return render(request, "ExampleThree/TicketForm.html", {"form":form,"post":post})

def deleteMethod(request, id):
    data = TicketTracker.objects.get(id=id)
    data.delete()
    return redirect('/ticketsupportApp/getData3/')

def updateMethod(request,id):
    update = 'update'
    data = TicketTracker.objects.get(id=id)
    if request.method == 'POST':
        form = TicketTrackerForm(request.POST, instance = data)
        if(form.is_valid()):
            form.save()
            return redirect('/ticketsupportApp/getData3/')
        else:
            return "<h1> Something Went Wrong </h1>"
    form = TicketTrackerForm
    return render (request, "ExampleThree/TicketForm.html", {"form":form,
                                                            'update':update,'id':id })