from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return render(request, 'vitaliteit/vitaliteit_vgz_mindfulness_coach_app.html')