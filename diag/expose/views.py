from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request, 'index.html')

def show_url_info(request):
    info_str = request.GET['info_str']
    return HttpResponse(str(info_str).upper())

def show_url_info_NB(request, info_str):
    return HttpResponse(str(info_str).upper())
