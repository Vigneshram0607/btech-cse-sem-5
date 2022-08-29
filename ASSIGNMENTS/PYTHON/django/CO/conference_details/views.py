from django.shortcuts import render
from .models import ConferenceDetails

def index_view(request):
    data = ConferenceDetails.objects.all()
    return render(request, 'index.html',{'details':data})


def FillForm_view(request):
    if request.method == 'POST':
        title = request.POST['conference_name']
        date = request.POST['conference_date']
        deadline = request.POST['conference_deadline']
        indian_author = request.POST['indian_author']
        foreign_author = request.POST['foreign_author']
        ConferenceDetails.objects.create(Title=title,
                                         Date=date,
                                         Deadline=deadline,
                                         Indianuthor=indian_author,
                                         Foreignauthor=foreign_author)

    return render(request, 'form.html')

def deleteForm_view(request):
    if request.method == 'POST':
        data = ConferenceDetails.objects
    pass