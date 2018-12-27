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
    cantons = pagination(cantonList, page)
    return render(request, 'index.html',{'cantonsList': cantons})

#solo se ejecutará una vez. Este carga los datos
def onInit():
    with open('./static/data.json') as file:
        data = json.load(file)
        createAllLists(data)

#crea las listas a partir del json: provincias, cantones y provincias.
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
    
#busca la provincia para un distrito
def searchProvinceAuxDistrict(cantonName, List):
    for element in List:
        if(element['fields']['name']==cantonName):
            return element['provinceName']
    return ""

#busca un canton o una provincia por medio del codigo.
def searchCantonOrProvinceName(code,List):
    for element in List:
        if(str(element['pk'])==str(code)):
            return element['fields']['name']
    return ""

#se elimina el canton con respecto al pk
def DeleteCanton(request,pk):
    for element in cantonList:
        codeCanton = str(element['pk'])
        if(codeCanton==str(pk)):
            for distrit in districtList:
                codeCantonInDistrict = str(distrit['fields']['canton'])
                if(codeCantonInDistrict == codeCanton):
                    districtList.remove(distrit)
            cantonList.remove(element)
    page = request.GET.get('page', 1)
    cantons = pagination(cantonList, page)
    return render(request, 'index.html',{'cantonsList': cantons})

#se elimina el distrito con respecto al pk
def DeleteDistrict(request,pk):
    for distrit in districtList:
        districtPK = str(distrit['pk'])
        if(districtPK == str(pk)):
            districtList.remove(distrit)
    page = request.GET.get('page', 1)
    district = pagination(districtList, page)
    return render(request, 'baseDistricts.html',{'districtsList': district})

# es el inicio de la opción de buscar distritos-
def IndexDistricts(request):
    page = request.GET.get('page', 1)
    district = pagination(districtList, page)
    return render(request, 'baseDistricts.html',{'districtsList': district})

#busca cantones. Con respecto a los filtros de búsqueda
def searchCantons(request):
    auxList = []
    #aquí está el valor del filtro
    filterRadioBTN = request.POST.get('radios')
    searchText = request.POST.get('searchText')
    for element in cantonList:
        if(filterRadioBTN=="Province"):
            if(searchText==element['provinceName']):
                auxList.append(element)
        elif(filterRadioBTN=="Canton"):
            if(searchText== element['fields']['name']):
                auxList.append(element)
        else:
            auxList = cantonList
    page = request.GET.get('page', 1)
    cantons = pagination(auxList, page)
    return render(request, 'index.html',{'cantonsList': cantons})

#busca distritos. Con respecto a los filtros de búsqueda
def searchDistricts(request):
    auxList = []
    #aquí está el valor del filtro
    filterRadioBTN = request.POST.get('radioD')
    searchTextDistricts = request.POST.get('searchTextDistricts')

    for element in districtList:
        if(filterRadioBTN=="Province"):
            if(searchTextDistricts==element['provinceName']):
                auxList.append(element)
        elif(filterRadioBTN=="Canton"):
            if(searchTextDistricts== element['cantonName']):
                auxList.append(element)
        elif(filterRadioBTN=="District"):
            if(searchTextDistricts== element['fields']['name']):
                auxList.append(element) 
        else:
            auxList = districtList
    page = request.GET.get('page', 1)
    district = pagination(auxList, page)
    return render(request, 'baseDistricts.html',{'districtsList': district})

#metodo auxiliar para la paginación
def pagination(anyList, page):
    paginator = Paginator(anyList, 20)
    try:
        listaPaginated = paginator.page(page)
    except PageNotAnInteger:
        listaPaginated = paginator.page(1)
    except EmptyPage:
        listaPaginated = paginator.page(paginator.num_pages)
    return listaPaginated