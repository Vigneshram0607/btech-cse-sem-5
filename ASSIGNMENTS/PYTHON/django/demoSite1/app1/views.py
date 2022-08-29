from django.shortcuts import render

from django.http import HttpResponse
# Create your views here.
def wrong_dob(request):
    return HttpResponse("<h1>Please enter ur DOB / check ur URL</h1>")

def welcome(request):
    print(request.user)
    print(request)
    return HttpResponse("<h1>Welcome Message</h1>")

def personal_data(request):
    title =  "<h1 style='background-color: black; color: orange; text-align:center;'>PERSONAL DATA</h1>"

    name = "<p><strong>NAME: </strong> Vignesh Ram</p>"
    course = "<p><strong>COURSE: </strong> Computer Science</p>"
    regno = "<p><strong>REG NUM: </strong> 223003109</p>"
    result_text = title + name + course + regno
    return HttpResponse(result_text)

def dashboard(request):
    title = "<h1 style='background-color: black; color: orange; text-align:center;'>DASHBOARD</h1>"
    wel_msg = "<p><strong>Welcome Message link: </strong> http://127.0.0.1:8000/welcome/ </p>"
    pers_msg = "<p><strong>Personal Data link: </strong> http://127.0.0.1:8000/personaldata/ </p>"
    dob = "<p><strong>Personal Data link: </strong> http://127.0.0.1:8000/myapp/ </p>"
    admin_link = "<p><strong>Admin Interface link: </strong> http://127.0.0.1:8000/admin/ </p>"

    result_txt = title + admin_link + wel_msg + pers_msg + dob
    return HttpResponse(result_txt)

def dob(request, day, month, year):
    title = "<h1 style='background-color: black; color: orange; text-align:center;'>DATE OF BIRTH</h1>"
    msg = "<p>You've entered <strong> %s-%s-%s </strong></p>"%(day, month, year)
    result_txt = title+msg
    return HttpResponse(result_txt)

