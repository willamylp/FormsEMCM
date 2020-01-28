from django.shortcuts import render
from urllib import request
from django.contrib.auth.decorators import login_required


def principal(request):
    return render(request, 'principal.html')

