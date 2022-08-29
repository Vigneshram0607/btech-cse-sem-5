from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.http import HttpResponseRedirect

from .models import Publisher, Author, Book
from .forms import PublisherForm, AuthorForm, BookForm

# Create your views here.
"""
PUBLISHER:
    name = models.CharField(max_length=25)
    address = models.TextField()
    city = models.CharField(max_length=15)
    country = models.CharField(max_length=15)
    website = models.CharField(max_length=20)
"""
def publisher_view(request):
    if request.method == "POST":
        form = PublisherForm(request.POST)
        if form.is_valid():

            # f_name = form.cleaned_data['name']
            # f_address = form.cleaned_data['address']
            # f_city = form.cleaned_data['city']
            # f_country = form.cleaned_data['country']
            # f_website = form.cleaned_data['website']
            # publisher_obj = Publisher(
            #     name=f_name,
            #     address = f_address,
            #     city = f_city,
            #     country = f_country,
            #     website = f_website,
            # ).save()
            form.save()
            return HttpResponse("<h1>Successfully Added Publisher Details</h1>")
    else:
        form = PublisherForm(request.POST)
        return render(request, 'publisherDisplay.html',context={'form':form})

"""
AUTHOR:
salutation = models.CharField(max_length=15)
    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=25)
    email = models.EmailField()
"""
def author_view(request):
    if request.method == "POST":
        form = AuthorForm(request.POST)
        if form.is_valid():
            f_salutation = form.cleaned_data['salutation']
            f_fn = form.cleaned_data['first_name']
            f_ln = form.cleaned_data['last_name']
            f_email = form.cleaned_data['email']
            author_obj = Author(
                salutation=f_salutation,
                first_name = f_fn,
                last_name = f_ln,
                email = f_email,
            )
            author_obj.save()
            return HttpResponse("<h1>Successfully Added Author Details</h1>")
    else:
        form = AuthorForm(request.POST)
        return render(request, 'authorDisplay.html',context={'form':form})

"""
BOOK:
title = models.CharField(max_length=25)
    authors = models.ManyToManyField(Author)
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE)
    publication_date = models.DateField()
"""
def book_view(request):
    if request.method == "POST":
        form = BookForm(request.POST)
        if form.is_valid():
            f_title = form.cleaned_data['title']
            f_authors = form.cleaned_data['authors']
            f_publisher = form.cleaned_data['publisher']
            f_publication_date=  form.cleaned_data['publication_date']
            book_obj = Book(
                title=f_title,
                authors=f_authors,
                publisher=f_publisher,
                publication_date=f_publication_date,
            )
            book_obj.save()
            return HttpResponse("<h1>Successfully Added Book Details</h1>")
    else:
        form = BookForm(request.POST)
        return render(request, 'bookDisplay.html', context={'form': form})

def retrieve_view(request):
    book = Book.objects.all()
    for i in book:
        print(i.publication_date)
        print(i)
    return render(request, 'bookDisplay.html', {'book':book,})
