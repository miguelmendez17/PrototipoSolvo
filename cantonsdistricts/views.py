from django.shortcuts import render
from cantonsdistricts.models import Province, Canton, District
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.http import HttpResponse
from django.shortcuts import render
import json
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

provinceList = []
cantonList = []

def Index(request):
    with open('./static/data.json') as file:
        data = json.load(file)
        provinceList = createList('crdist.province',data)
        cantonList = createList('crdist.canton',data)


    page = request.GET.get('page', 1)
    paginator = Paginator(cantonList, 20)
    try:
        users = paginator.page(page)
    except PageNotAnInteger:
        users = paginator.page(1)
    except EmptyPage:
        users = paginator.page(paginator.num_pages)


    return render(request, 'index.html',{'lista': users})


def createList(model,jsonData):
    lista = []
    for client in jsonData:
        if(client['model']==model):
            lista.append(client)
    return lista