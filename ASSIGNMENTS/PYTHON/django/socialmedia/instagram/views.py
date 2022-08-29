from django.shortcuts import render

from django.http import HttpResponse
# Create your views here.
from .models import *
from datetime import datetime
from django.template import loader

def memepage(request):
    return HttpResponse("This is MEMEPAGE response!")

def likes(request, count):
    text = "LIKES: %s"%(count)
    return HttpResponse(text)

def home_view(request):
    return render(request, 'dashboard.html', {})

def crudops(request):
    print("CRUDOPS")
    # Create Entry
    # create_obj = Instagram(
    #     username='username11',
    #     password='password11',
    #     description='this is description11'
    # )
    # create_obj.save()

    #
    # Read all Entries
    # read_obj = Instagram.objects.all()
    # read_html = "<h3>Reading All DATA Entries In Instagram DB:</h3><br>"
    # for data in read_obj:
    #     read_html+=data.username+"<br>"

    # Reading Sepcific Entry:
    # rajinikanth = Instagram.objects.get(username='Rajinikanth')
    # read_html+="<br>Reading Entry-1: "+rajinikanth
    # return HttpResponse(read_html)

    # # DELETE:
    # del_data = Instagram.objects.get(username='demo1')
    # read_html="<br>Deleting Entry"
    # del_data.delete()
    #
    # return HttpResponse(read_html)


from django.http import HttpResponseRedirect

def login(request):
    if request.method == 'POST':
        Instagram(
            name = request.POST.get('name'),
            regnum=request.POST.get('regnum'),

        ).save()
        return HttpResponseRedirect('users/')
    else:
        return render(request, "login.html")



def users(request):
    """
    # CREATING AN ENHANCED VIEW FUNCTION - METHOD:1
    post = Instagram.objects.all()
    temp = loader.get_template('users.html')
    context = {
        'data':post,
    }
    return HttpResponse(temp.render(context))
    """
    # CREATING AN ENHANCED VIEW FUNCTION - METHOD:2 [SHORTCUT]
    post = Instagram.objects.all()
    cont= {
        'data': post,
    }
    return render(request,'users.html',context=cont)
