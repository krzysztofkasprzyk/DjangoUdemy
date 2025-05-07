from django.shortcuts import render
from django.http import HttpResponse
from .models import Film

# Create your views here.
def wszystkie_filmy(request):
    #return HttpResponse("To jest nasz 1 test strony test/")

    wszystkie = Film.objects.all()
    return render(request,'filmy.html',{'filmy': wszystkie})