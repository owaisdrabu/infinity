from django.shortcuts import render
from django.http import HttpResponse
from .models import Stones


def stones(request):
    data = Stones.objects.all()
    return render(request, 'stones.html', {'data': data})


