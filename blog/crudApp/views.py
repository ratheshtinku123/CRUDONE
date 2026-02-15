from django.shortcuts import render, redirect

from .forms import ExpenseTrackerForm
from .models import ExpenseTracker

# Create your views here.


def getMethod(request):
    datas = ExpenseTracker.objects.all()
    return render(request, 'ExampleOne/ExpenseTable.html', {'datas': datas})

def postMethod(request):
    post = 'post'
    if request.method == 'POST':
        form = ExpenseTrackerForm(request.POST)
        if (form.is_valid()):
            form.save()
            return redirect('/crudApp/getData1/')
        else:
            return "<h1> Something Went Wrong </h1>"
    form = ExpenseTrackerForm
    return render(request,'ExampleOne/ExpenseForm.html', {'form': form, 'post': post})

def deleteMethod(request,id):
    data = ExpenseTracker.objects.get(id=id)
    data.delete()
    return redirect('/crudApp/getData1/')


def updateMethod(request,id):
    update = 'update'
    data = ExpenseTracker.objects.get(id=id)
    if request.method == 'POST':
        form = ExpenseTrackerForm(request.POST, instance=data)
        if(form.is_valid()):
            form.save()
            return redirect('/crudApp/getData1/')
        else:
            return "<h1> Something Went Wrong </h1>"
    form = ExpenseTrackerForm
    return render(request,'ExampleOne/ExpenseForm.html', {'form': form, 'update':update,
                                                           'id': id})


