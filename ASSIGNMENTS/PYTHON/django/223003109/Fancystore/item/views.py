from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.http import HttpResponseRedirect

from .forms import FancystoreForm
from .models import FancyStoreModel
# Create your views here.

# THis function is used to display the links
def home_view(request):
    return render(request, 'home.html')

# This is used to update items
def update_item(request, id):
    print(id)
    item = FancyStoreModel.objects.get(item_id=id)
    print(item)
    form = FancystoreForm(instance=item)
    if request.method == 'POST':
        form = FancystoreForm(instance=item)
        if form.is_valid():
            form.save()
            return redirect('/display')
    context = {
        'form':form,
    }
    return render(request, 'insert.html', {'form': form})

# This is used to insert item data
def insert_item(request):
    if request.method == "POST":
        form = FancystoreForm(request.POST)
        if form.is_valid():
            price = form.cleaned_data['price']
            if int(price) < 0:
                return render(request, 'exception.html', context={'form': form})
            else:
                form.save()
                return render(request, 'item_added.html', context={'form': form})
    else:
        form = FancystoreForm(request.POST)
        return render(request, 'insert.html', context={'form': form})


# this is used to delete items
def delete_item(request, id):
    item = FancyStoreModel.objects.get(item_id=id)
    print(item)

    if request.method == 'POST':
        item.delete()
        return redirect('/display')
    return render(request, 'delete.html', {"item": item,"id":id })


# this is used to display items
def display_view(request):
    items = FancyStoreModel.objects.all()
    return render(request, 'display.html',{"items":items,})


