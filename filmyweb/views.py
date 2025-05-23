from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import Film
from .forms import FilmForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.shortcuts import render, redirect

# Create your views here.


def wszystkie_filmy(request):
    #return HttpResponse("To jest nasz 1 test strony test/")
    wszystkie = Film.objects.all()
    return render(request,'filmy.html',{'filmy': wszystkie})
@login_required
def nowy_film(request):
    czy_nowy = True
    form = FilmForm(request.POST or None, request.FILES or None)

    if form.is_valid():
        form.save()
    return render(request, 'film_form.html', {'form': form,'nowy': czy_nowy})

@login_required
def edytuj_film(request,id):
    czy_nowy=False
    film =  get_object_or_404(Film, pk=id)
    form = FilmForm(request.POST or None, request.FILES or None, instance=film)

    if form.is_valid():
        form.save()
        return redirect(wszystkie_filmy)
    return render(request, 'film_form.html', {'form': form,'nowy': czy_nowy})
@login_required
def usun_film(request,id):
    film =  get_object_or_404(Film, pk=id)

    if request.method == "POST":
        film.delete()
        return redirect(wszystkie_filmy)

    return render(request, 'potwierdz.html', {'film': film})

@login_required
def user_logout(request):
    logout(request)
    return render(request, 'registration/logout.html')