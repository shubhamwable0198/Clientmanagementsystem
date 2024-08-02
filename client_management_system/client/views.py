from django.shortcuts import render, redirect
from .forms import ClientInfoForm
from .models import ClientInfo


def addview(request):
    form = ClientInfoForm()
    if request.method == "POST":
        form = ClientInfoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("show")


    return render(request, "client/add.html", {"form": form})


def showview(request):
    obj = ClientInfo.objects.all()
    return render(request, "client/show.html", {"obj": obj})


def updateview(request, pk):
    obj = ClientInfo.objects.get(pk=pk)
    form = ClientInfoForm(instance=obj)
    if request.method == "POST":
        form = ClientInfoForm(request.POST, instance=obj)
        if form.is_valid():
            form.save()
            return redirect("show")


    return render(request, "client/add.html", {"form": form})


def deleteview(request, pk):
    obj = ClientInfo.objects.get(pk=pk)
    obj.delete()
    return redirect("show")



