from django.db import models

# Create your models here.
class AutomobilioModelis(models.Model):
    marke = models.CharField(verbose_name="Markė", max_length=100)
    modelis = models.CharField(verbose_name="Model", max_length=100)

    def __str__(self):
        return f'{self.marke} {self.modelis}'

class Automobilis(models.Model):
    valstybinis_nr = models.CharField(verbose_name="Valstybinis_nr", max_length=100)
    vin_kodas = models.CharField(verbose_name="VIN kodas", max_length=100)
    klientas = models.CharField(verbose_name="Klientas", max_length=100)
    automobilio_modelis = models.ForeignKey(to=AutomobilioModelis, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f'{self.marke} {self.modelis} ({self.valstybinis_nr})'


class Paslauga(models.Model):
    pavadinimas = models.CharField(verbose_name="Pavadinimas", max_length=100)
    kaina = models.FloatField(verbose_name="Kaina")

    def __str__(self):
        return f'{self.pavadinimas}'


class Uzsakymas(models.Model):
    data = models.DateTimeField(verbose_name="Data", auto_now_add=True)
    automobilis = models.ForeignKey(to="Automobilis", on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.automobilis.vin_kodas}({self.data})'


class UzsakymoEilute(models.Model):
    uzsakymas = models.ForeignKey(to="Uzsakymas", on_delete=models.CASCADE)
    paslauga = models.ForeignKey(to="paslauga", on_delete=models.SET_NULL, null=True)
    kiekis = models.IntegerField(verbose_name="Kiekis")

    def __str__(self):
        return f'{self.uzsakymas.data}, {self.paslauga} ({self.kiekis}'
