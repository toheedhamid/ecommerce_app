from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return render(request, 'shop/index.html')


def about(request):
    return HttpResponse("we are at about ")


def contact(request):
    return HttpResponse("we are at contact ")


def tracker(request):
    return HttpResponse("we are at contact ")


def search(request):
    return HttpResponse("we are at search ")


def productview(request):
    return HttpResponse("we are at productview ")


def checkout(request):
    return HttpResponse("we are at checkout ")
