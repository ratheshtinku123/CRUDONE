from django.shortcuts import render,redirect

from .forms import inventorystockdataForm
from .models import inventorystockdata

# Create your views here.

def getMethod(request):
    datas = inventorystockdata.objects.all()
    return render(request, 'ExampleFour/InventoryStockTable.html', {'datas': datas})

def postMethod(request):
    post = 'post'
    if request.method == 'POST':
        form = inventorystockdataForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/inventorystockApp/getData4/')
        else:
            return "<h1> Something Went Wrong </h1>"

    form = inventorystockdataForm
    return render(request, 'ExampleFour/InventoryStockForm.html', {'form': form,
                                                                   'post': post})

def deleteMethod(request,id):
    data = inventorystockdata.objects.get(id=id)
    data.delete()
    return redirect('/inventorystockApp/getData4/')

def updateMethod(request,id):
    update = 'update'
    data = inventorystockdata.objects.get(id=id)
    if request.method == 'POST':
        form = inventorystockdataForm(request.POST, instance=data)
        if form.is_valid():
            form.save()
            return redirect('/inventorystockApp/getData4/')
        else:
            return "<h1> Something Went Wrong </h1>"

    form = inventorystockdataForm
    return render(request, 'ExampleFour/InventoryStockForm.html', {'form': form,
                                                                   'update':update,'id':id})
