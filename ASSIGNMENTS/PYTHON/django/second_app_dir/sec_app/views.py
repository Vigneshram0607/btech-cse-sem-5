from django.shortcuts import render

# Create your views here.
from django.http import  HttpResponse

def hello(request):
    text = """<h1>THIS IS HELLO!</h1>"""
    return HttpResponse(text)

