from django.shortcuts import render,redirect
from constructionapp.models import Member,Properties
from constructionapp.forms import MemberForm,PropertyForm
from django.http import HttpResponse
from django.contrib import messages

# Create your views here.

def home(request):
    all_members=Member.objects.all()
    return render(request,'home.html',{'all':all_members})

def propertyhome(request):
    all=Properties.objects.all()
    return render(request,'propertyhome.html',{'all':all})

def join(request):
    if request.method=='POST':
        form = MemberForm(request.POST)
        if form.is_valid():
            form.save()

        else:
            fname=request.POST['fname']
            lname=request.POST['lname']
            age=request.POST['age']
            email=request.POST['email']
            passwd=request.POST['passwd']
            landproperty=request.POST['landproperty']
            messages.success(request,('there was an error'))
            return render(request,'join.html',{
                                               'fname':fname,
                                               'lname':lname,
                                               'age':age,
                                               'email':email,
                                               'passwd':passwd,
                                               'landproperty':landproperty}
                          )

        messages.success(request, ('Your form is submitted'))
        return HttpResponse('ADD propertyhome to url')
    else:
        return render(request,'join.html',{})


def property(request):
    if request.method == 'POST':
        form=PropertyForm(request.POST)
        if form.is_valid():
            form.save()

        else:
            address=request.POST['address']
            city=request.POST['citys']
            landsq=request.POST['landsq']
            price=request.POST['price']

            messages.success(request, ('there was an error'))
            return render(request, 'propeties.html', {
                                                 'city':city,
                                                 'address': address,
                                                 'landsq': landsq,
                                                 'price': price
                                                 }
                          )

        messages.success(request, ('Your details are submitted'))
        return HttpResponse('returnhome')
    else:
        return render(request, 'properties.html', {})

