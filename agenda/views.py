from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return render(request, 'agenda/agenda_index.html')