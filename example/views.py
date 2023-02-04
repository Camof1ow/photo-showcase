# example/views.py
from datetime import datetime
from django.shortcuts import render, get_object_or_404

def index(request):
    return render(request, 'index.html')


def api(request):
    return None