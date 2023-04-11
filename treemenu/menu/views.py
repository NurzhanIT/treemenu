from django.shortcuts import render

# Create your views here.


def index(request, title):
    return render(request, 'index.html', {'title':title})
