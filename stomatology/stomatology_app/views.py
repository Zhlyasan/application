from django.shortcuts import render
from .models import *
# Create your views here.
from django.http import HttpResponse
def index(request):
    # bbs = Doctor.objects.order_by('-published')
    docs = Doctor.objects.all()
    sessions = Session.objects.order_by('-date_time')
    worklists = Worklist.objects.all()
    return render(request, "stomatology_app/index.html", {'docs': docs, 'sessions': sessions, 'worklists': worklists})

# def index(request):
#     return HttpResponse("Привет! Это твое первое приложение!")
