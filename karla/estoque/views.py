#from django.shortcuts import render

# Create your views here.
#coloquei '#' acima mesmo para adicionar esse abaixo

from django.http import HttpResponse

def inicio(request):
    return HttpResponse("Sistema do Totem funcionando!")