from django.shortcuts import render, get_object_or_404
from .models import Paslauga, Automobilis, Uzsakymas

# Create your views here.
def index(request):
    paslaugu_kiekis = Paslauga.objects.count()
    automobiliu_kiekis = Automobilis.objects.count()
    atliktu_uzsakymu_kiekis = Uzsakymas.objects.filter(status__exact='i').count()

    kontekstas = {
        "paslaugu_kiekis": paslaugu_kiekis,
        "automobiliu_kiekis": automobiliu_kiekis,
        "atliktu_uzsakymu_kiekis": atliktu_uzsakymu_kiekis,
    }
    return render(request, 'index.html', context=kontekstas)


def automobiliai (request):
    automobiliai = Automobilis.objects.all()
    context = {
        'automobiliai' : automobiliai
    }
    return render(request, 'automobiliai.html', context=context)

def automobilis(request, auto_id):
    automobilis = get_object_or_404(Automobilis, pk=auto_id)
    context = {
        'automobilis': automobilis
    }
    return render(request, 'automobilis.html', context=context)
