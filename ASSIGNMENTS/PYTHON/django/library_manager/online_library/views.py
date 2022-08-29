from django.shortcuts import render,redirect

from .models import ReaderModel
from .forms import AddReaderForm
from django.http.response import HttpResponse


# Create your views here.

def SubscribeView(request):
    if request.method == 'POST':
        form = AddReaderForm(request.POST)
        if form.is_valid():
            f_name = form.cleaned_data['RName']
            f_number = form.cleaned_data['RNumber']
            f_gender = form.cleaned_data['Gender']
            f_city = form.cleaned_data['City']
            f_contactnumber = form.cleaned_data['ContactNumber']
            f_subscription = form.cleaned_data['Subscription']
            if f_subscription == "Month":
                f_charges = 100
            else:
                f_charges = 1000
            model_obj = ReaderModel(
                RName=f_name,
                RNumber=f_number,
                Gender=f_gender,
                City=f_city,
                ContactNumber=f_contactnumber,
                Subscription=f_subscription,
                Charges=f_charges
            )
            model_obj.save()
            # return HttpResponse('<h1>This is Subscribe View</h1>')
            return redirect('display_readers')
    else:
        form = AddReaderForm
    return render(request, 'subscribe.html', {'form':form})

def DisplayReadersView(request):
    post = ReaderModel.objects.all()[:10]
    cont = {
        'data': post,
    }
    return render(request, 'displayReaders.html', context=cont)
    # return HttpResponse('<h1>This is DisplayReadersView View</h1>')