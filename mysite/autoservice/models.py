import datetime

from django.db import models
from django.contrib.auth.models import User
from datetime import date
import pytz
from tinymce.models import HTMLField
from PIL import Image

description = HTMLField()
uts = pytz.UTC

# Create your models here.
class AutomobilioModelis(models.Model):
    marke = models.CharField(verbose_name="Markė", max_length=100)
    modelis = models.CharField(verbose_name="Model", max_length=100)

    def __str__(self):
        return f'{self.marke} {self.modelis}'

    class Meta:
        verbose_name = "Automobilio modelis"
        verbose_name_plural = "Automobilių modeliai"


class Automobilis(models.Model):
    valstybinis_nr = models.CharField(verbose_name="Valstybinis_nr", max_length=100)
    vin_kodas = models.CharField(verbose_name="VIN kodas", max_length=100)
    klientas = models.CharField(verbose_name="Klientas", max_length=100)
    automobilio_modelis = models.ForeignKey(to=AutomobilioModelis, on_delete=models.SET_NULL, null=True)
    photo = models.ImageField('Nuotrauka', upload_to='covers', null=True, blank=True)
    aprasymas = HTMLField(verbose_name="Aprasymas", null=True, blank=True)

    def __str__(self):
        return f'{self.automobilio_modelis.marke} {self.automobilio_modelis.modelis} ({self.valstybinis_nr})'

    class Meta:
        verbose_name = "Automobilis"
        verbose_name_plural = "Automobiliai"


class Paslauga(models.Model):
    pavadinimas = models.CharField(verbose_name="Pavadinimas", max_length=100)
    kaina = models.FloatField(verbose_name="Kaina")

    def __str__(self):
        return f'{self.pavadinimas}'

    class Meta:
        verbose_name = "Paslauga"
        verbose_name_plural = "Paslaugos"


class Uzsakymas(models.Model):
    data = models.DateTimeField(verbose_name="Data", auto_now_add=True)
    terminas = models.DateTimeField(verbose_name="Terminas", null=True)
    automobilis = models.ForeignKey(to="Automobilis", on_delete=models.CASCADE)
    vartotojas = models.ForeignKey(to=User, verbose_name="Vartotojas", on_delete=models.SET_NULL, null=True, blank=True)

    def ar_praejo_terminas(self):
        if self.terminas:
            return self.terminas.replace(tzinfo=pytz.utc) < datetime.datetime.today()
        else:
            return False



    LAON_STATUS = (
        ("p", 'Patvirtinta'),
        ("v", 'Vykdoma'),
        ("a", 'Atšaukta'),
        ("i", 'Įvykdyta'),

    )

    status = models.CharField(
        max_length=1,
        choices=LAON_STATUS,
        blank=True,
        default='p',
        help_text='Statusas',

    )




    def suma(self):
        suma = 0
        eilutes = self.eilutes.all()
        for eilute in eilutes:
            suma += eilute.kaina()
        return suma

    def __str__(self):
        return f'{self.automobilis.vin_kodas}({self.data})'

    class Meta:
        verbose_name = "Užsakymas"
        verbose_name_plural = "Užsakymai"


class UzsakymoEilute(models.Model):
    uzsakymas = models.ForeignKey(to="Uzsakymas", on_delete=models.CASCADE, related_name="eilutes")
    paslauga = models.ForeignKey(to="paslauga", on_delete=models.SET_NULL, null=True)
    kiekis = models.IntegerField(verbose_name="Kiekis")

    def kaina(self):
        return self.paslauga.kaina * self.kiekis

    def __str__(self):
        return f'{self.uzsakymas.data}, {self.paslauga} ({self.kiekis}'

    class Meta:
        verbose_name = "Užsakymo eilutė"
        verbose_name_plural = "Užsakymų eilutės"


class Komentaras(models.Model):
    uzsakymas = models.ForeignKey('Uzsakymas', verbose_name="Užsakymas", on_delete=models.CASCADE, related_name="komentarai", null=True, blank=True)
    vartotojas = models.ForeignKey(to=User, verbose_name="Vartotojas", on_delete=models.CASCADE, null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True)
    tekstas = models.TextField(verbose_name="Tekstas", max_length=1000)

    class Meta:
        verbose_name = "Užsakymas"
        verbose_name_plural = "Užsakymai"
        ordering = ['-date_created']

class Profilis(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profilis')
    nuotrauka = models.ImageField(default="profile_pics/default.png", upload_to="profile_pics")

    def __str__(self):
        return f"{self.user.username} profilis"

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        img = Image.open(self.nuotrauka.path)
        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.nuotrauka.path)

