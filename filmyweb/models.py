from django.db import models

# Create your models here.
class Film(models.Model):
    tytul = models.CharField(max_length=64, blank=False, unique=True)
    rok = models.PositiveSmallIntegerField(default=2000)
    opis = models.TextField(default="Opis filmu")
    premiera = models.DateField(null=True,blank=True)
    imdb_rating = models.DecimalField(decimal_places=2,max_digits=4,null=True,blank=True)

    plakat = models.ImageField(upload_to="plakaty",null=True,blank = True)



    def __str__(self):
        return self.tytul_z_rokiem()

    def tytul_z_rokiem(self):
        """
        tytul_z_rokiem funkcja
        :return: zwraca tytul z rokiem w nawiasie

        """
        return f"{self.tytul} ({self.rok})"