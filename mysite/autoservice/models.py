from django.db import models

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

    def __str__(self):
        return f'{self.marke} {self.modelis} ({self.valstybinis_nr})'


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
    automobilis = models.ForeignKey(to="Automobilis", on_delete=models.CASCADE)

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
    uzsakymas = models.ForeignKey(to="Uzsakymas", on_delete=models.CASCADE, related_name=) #Nebaigat
    paslauga = models.ForeignKey(to="paslauga", on_delete=models.SET_NULL, null=True)
    kiekis = models.IntegerField(verbose_name="Kiekis", max_length=50)


    def kaina(self):
        return  self.paslauga.kaina * self.kiekis

    def __str__(self):
        return f'{self.uzsakymas.data}, {self.paslauga} ({self.kiekis}'

    class Meta:
        verbose_name = "Užsakymo eilutė"
        verbose_name_plural = "Užsakymų eilutės"
