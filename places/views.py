from django.shortcuts import render
from django.http import HttpResponse
from .models import Places


def places(request):
    data = Places.objects.all()
    return render(request, 'places.html', {'data': data})

