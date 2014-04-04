from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse('<html><head><title>ONEPAGE</title></head><body><h1>Onepage app</h1></body></html>')
    # return render(request, 'index.html')

