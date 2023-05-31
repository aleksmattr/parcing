from django.shortcuts import render, redirect
from .parcer import get_vacancies
from .city import cities


def index(request):
    vacancii = get_vacancies()
    context = {
        'data': vacancii,
        'cities': cities
    }
    return render(request, 'services.html', context=context)


def search(request):
    if request.method == 'POST':
        city = request.POST['city']
        s = request.POST['s']
        vacancii = get_vacancies(s=s, city=city)
        context = {
            'cities': cities,
            'data': vacancii
        }
    return render(request, 'services.html', context=context)
