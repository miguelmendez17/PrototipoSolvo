from django.shortcuts import render
from cantonsdistricts.models import Province, Canton, District
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.http import HttpResponse
from django.shortcuts import render
import json
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

provinceList = []
cantonList = []
districtList = []

onInitCount = 0

def IndexCantons(request):
    global onInitCount
    #esta función es para que entre solo una vez durante la ejecución.
    #es decir, carga los datos a la aplicación solo una vez.
    if(onInitCount==0):
        onInit()
        onInitCount+=1

    page = request.GET.get('page', 1)
    paginator = Paginator(cantonList, 20)
    try:
        cantons = paginator.page(page)
    except PageNotAnInteger:
        cantons = paginator.page(1)
    except EmptyPage:
        cantons = paginator.page(paginator.num_pages)
    return render(request, 'index.html',{'cantonsList': cantons})

def onInit():
    with open('./static/data.json') as file:
        data = json.load(file)
        createAllLists(data)

def createAllLists(jsonData):
    for data in jsonData:
        if(data['model']=='crdist.province'):
            provinceList.append(data)
        elif(data['model']=='crdist.canton'):
            provinceCode = data['fields']['province']
            data['provinceName']= searchCantonOrProvinceName(provinceCode, provinceList)
            cantonList.append(data)
        elif(data['model']=='crdist.district'):
            cantonCode = data['fields']['canton']
            data['cantonName'] = searchCantonOrProvinceName(cantonCode, cantonList)
            data['provinceName'] = searchProvinceAuxDistrict(data['cantonName'],cantonList)
            districtList.append(data)
    
def searchProvinceAuxDistrict(cantonName, List):
    for element in List:
        if(element['fields']['name']==cantonName):
            return element['provinceName']
    return ""

def searchCantonOrProvinceName(code,List):
    for element in List:
        if(str(element['pk'])==str(code)):
            return element['fields']['name']
    return ""


def IndexDistricts(request):
    page = request.GET.get('page', 1)
    paginator = Paginator(districtList, 20)
    try:
        district = paginator.page(page)
    except PageNotAnInteger:
        district = paginator.page(1)
    except EmptyPage:
        district = paginator.page(paginator.num_pages)
    return render(request, 'baseDistricts.html',{'districtsList': district})


def filter(request):
    print("filter")