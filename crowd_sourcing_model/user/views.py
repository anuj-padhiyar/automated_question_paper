from __future__ import unicode_literals

from django.shortcuts import render
from django.http import JsonResponse
from django.views.generic.base import View


# Create your views here.
def user(request):
    return JsonResponse({'code': 200, 'msg': 'Your Balance Amount is: 2,00,000 Rs/-'})

def login(request):
    return render(request, 'user/login.html',{})