from django.shortcuts import render
from django_tables2 import RequestConfig
from .models import Person
from .tables import PersonTable

def person_list(request):
    table = PersonTable(Person.objects.all())

    return render(request, 'people.html', {
        'table': table
    })