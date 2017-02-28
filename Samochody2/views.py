from django.http import HttpResponse
from django.db import connection
import json
from django.conf.urls.static import static

from django.shortcuts import render, redirect
from django.template.defaultfilters import random
from django.views.generic import TemplateView
from random import *


def api_next_question(request):
    result = {"dupa": "dupa222"}
    return HttpResponse(json.dumps(result), content_type='application/json')


def hotel(request):
    return render(request, 'hotel.html', {'1_choice': 'Wszystkie', '2_choice': "Warszawa", '3_choice': "Gdank",
                                          '4_choice': "Krakow", '5_choice': "Wroclaw", '6_choice': "kjkj",
                  'ifActivePlaces' : "active"},
                  )

def hotel_selected(request):
    return render(request, 'hotel_details.html', {'1_choice': 'Podsumowanie', '2_choice': "Lokalizacja", '3_choice': "Personel",
                                          '4_choice': "kjnjnj", '5_choice': "Zasady", '6_choice': "Inne",

                                          '7_choice': "Podsumowanie", '8_choice': "Rozmowa",
                                          '9_choice': "Testy", '10_choice': "Referencje", '11_choice': "CV i dokumenty",
                    'ifActivePlaces' : "active"})

def table_activities(request):
    return render(request, 'table_activities.html', {'ifActiveTable_activities' : "active"})

def food(request):
    return render(request, 'food.html', {})

def interior_design(request):
    return render(request, 'interior_design.html', {'ifActiveInterior' : "active"})

def costs(request):
    return render(request, 'costs.html', {'ifActiveCosts' : "active"})

def location_map(request):
    return render(request, 'location_map.html', {'ifActiveLocation_map' : "active"})

def contact(request):
    return render(request, 'contact.html', {'ifActiveContact' : "active"})

def social_media(request):
    return render(request, 'social_media.html', {})


def index(request):
    return render(request, 'index-contact.html', {})

