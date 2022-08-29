from django.shortcuts import render,redirect

from .forms import BloodDonorForm
from .models import BloodDonor
from django.http import HttpResponse
from django.http import HttpResponseRedirect

# Create your views here.

def newDonor(request):
    # res = "<h1>This is New Donor</h1>"
    # form = BloodDonorForm(request.POST)
    # return HttpResponse(BloodDonor.objects.all())
    if request.method == 'POST':
        form = BloodDonorForm(request.POST)
        if form.is_valid():
            f_name = form.cleaned_data['name']
            f_age = form.cleaned_data['age']
            f_blood_group = form.cleaned_data['blood_group']
            f_gender = form.cleaned_data['gender']
            f_city = form.cleaned_data['city']
            f_phonenumber = form.cleaned_data['phonenumber']
            model_obj = BloodDonor(
                name=f_name,
                age=f_age,
                blood_group = f_blood_group,
                gender = f_gender,
                city = f_city,
                phonenumber=f_phonenumber,
            )
            model_obj.save()
            # return HttpResponse("<h1>Successfully Added Donor Details</h1>")
            # return render(request, 'donor_added.html', context={'form': form})

            return render(request, 'donor_added.html')

            # return redirect('addDonor')
    else:
        form = BloodDonorForm
        return render(request, 'newDonor.html',context={'form':form})

def searchDonor(request):
    if request.method == 'POST':
        searched = request.POST.get('searched')
        donor_data = BloodDonor.objects.filter(name__contains=searched)
        # print(donor_data)
        return render(request, 'search_results.html', context={'searched':searched,'donor_data':donor_data},)
    else:
        return render(request, 'search_results.html', context={})

