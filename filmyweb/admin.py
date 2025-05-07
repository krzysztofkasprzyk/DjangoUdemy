from django.contrib import admin
from .models import Film
# Register your models here.

#admin.site.register(Film)

@admin.register(Film)
class FilmAdmin(admin.ModelAdmin):
    #fields = ["tytul","opis","rok"]
    list_display = ["tytul","opis","rok"]
    search_fields = ["tytul","opis"]