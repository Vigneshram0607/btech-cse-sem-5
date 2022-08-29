from django.shortcuts import render,redirect

from library.models import reader
from .forms import add_reader
from library import *
# Create your views here.

def subscript(request):
    if request.method == 'POST':
        form = add_reader(request.POST)
        if form.is_valid():
            name=form.cleaned_data['RName']
            number=form.cleaned_data['RNumber']
            gender=form.cleaned_data['Gender']
            city=form.cleaned_data['City']
            phNo=form.cleaned_data['ContactNumber']
            subscription=form.cleaned_data['Subscription']
            if subscription=="month":
                charges=100
            else:
                charges=1000
            
            subReader=reader(RName=name,
                             RNumber=number,
                             Gender=gender,
                             City=city,
                             ContactNumber=phNo,
                             Subscription=subscription,
                             Charges=charges)

            subReader.save()
            return redirect("topTen")
    else:
        form = add_reader 
    return render(request,"subscribe.html",{'form':form})

def topTen(request):
    post = reader.objects.all()[:10]
    cont= {
        'data': post,
    }
    return render(request,'topTen.html',context=cont)
