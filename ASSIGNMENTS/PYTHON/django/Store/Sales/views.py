from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.http import HttpResponseRedirect

from .models import Sale, Store, Product
from .forms import SaleForm, StoreForm, ProductForm

# Create your views here.
"""
SALE:
date = models.DateField()
    store_id = models.ForeignKey(Store,on_delete=models.CASCADE)
    product_id = models.ForeignKey(Product,on_delete=models.CASCADE)
    units_sold = models.IntegerField()

"""
def sale_view(request):
    if request.method == 'POST':
        form = SaleForm(request.POST)
        if form.is_valid():
            f_date = form.cleaned_data['date']
            f_sid = form.cleaned_data['store_id']
            f_pid = form.cleaned_data['product_id']
            f_units = form.cleaned_data['units_sold']
            sale_obj = Sale(
                date=f_date,
                store_id = f_sid,
                product_id = f_pid,
                units_sold = f_units,
            ).save()
            return HttpResponse("<h1>Successfully Added Sales Details</h1>")
        else:
            return HttpResponse("<h1>ERROR</h1>")
    else:
        form = SaleForm(request.POST)
        return render(request, 'addSales.html',context={'form':form})


def product_view(request):
    pass

def store_view(request):
    pass
