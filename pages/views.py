from itertools import count
import json
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from .forms import RegisterUserForm
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
import ast
import sqlite3
from .models import usuario


def homePageView(request):
    mydb = sqlite3.connect("db.sqlite3")
    curr = mydb.cursor()

    query_progress = '''SELECT minutosJugados, usuario, progresoPorcentual FROM pages_usuario ORDER BY progresoPorcentual DESC'''
    rows1 = curr.execute(query_progress)
    data_progress = []

    counter = 0
    for x in rows1:
        counter += 1
        data_progress.append([counter, x[0], x[1], x[2]])

    return render(request, 'pages/index.html', {'values':data_progress})

def loginView(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('APIs_pages')
        else:
            messages.error(request, ('Bad login'))
            return redirect('login')   
    else:
        return render(request, 'pages/login.html', {})

def signUpView(request):
    if request.method == "POST":
        #form = UserCreationForm(request.POST)
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request,user)
            messages.success(request, ('Registration seccessful'))
            return redirect('APIs_pages') 
    else:
        #form = UserCreationForm()
        form = RegisterUserForm()
    return render(request, 'pages/signup.html', {'form':form})

def dashBoard(request):
    mydb = sqlite3.connect("db.sqlite3")
    curr = mydb.cursor()

    query_progress = '''SELECT nombre, tiempoMinutos FROM instrumento'''
    rows1 = curr.execute(query_progress)
    data_progress = []

    counter = 0
    for x in rows1:

        data_progress.append([  x[0], x[1]])

    return render(request, 'pages/dashBoard.html', {'values':data_progress})

def logout_user(request):
    logout(request)
    messages.success(request, ('Logged out'))
    return redirect('login')

def private_page(request):
    if request.user.is_authenticated:
        return render(request, 'pages/APIs.html')
    else:
        return redirect('login')


####################### UNITY #########################

@csrf_exempt
def change(request):
    if request.method == "POST":
        var = (request.body)#.decode()
        dicc = ast.literal_eval(var.decode('utf-8'))
        print(dicc)
        u = usuario.objects.filter(usuario=(dicc['body']))
        if len(u) > 0:
            print(u[0].toJson())
            userSqliteUpdate = u[0]
            userSqliteUpdate.usuario = dicc['title']
            userSqliteUpdate.save()
            return HttpResponse(str(json.dumps(u[0].toJson())).encode('utf-8')) #JsonResponse(jsonUser)
        else:
            print("Error in change")
            return HttpResponse("Not register")
    else:

        return HttpResponse("Please use POST")

@csrf_exempt
def consultUnity(request):
    if request.method == "POST":
        var = (request.body)#.decode()
        dicc = ast.literal_eval(var.decode('utf-8'))
        #jsonUser = json.loads(var)
        u = usuario.objects.filter(usuario=(dicc['body']))
        if u is not None:
            print(u[0].toJson())
            return HttpResponse(str(json.dumps(u[0].toJson())).encode('utf-8')) #JsonResponse(jsonUser)
        else:
            print("Error in change")
            return HttpResponse("Not register")
    else:
        return HttpResponse("Please use POST")


@csrf_exempt
def registerUnity(request):
    if request.method == "POST":
        var = (request.body)#.decode()
        dicc = ast.literal_eval(var.decode('utf-8'))
        print(dicc)
        
        userNew = dicc['body']
        pswNew = dicc['title']
        userSqliteRegister = usuario()
        userSqliteRegister.progresoPorcentual = 0
        userSqliteRegister.minutosJugados = 0
        userSqliteRegister.usuario = userNew
        userSqliteRegister.password = pswNew
        userSqliteRegister.save()
        return HttpResponse(str(json.dumps(userSqliteRegister.toJson())).encode('utf-8')) #JsonResponse(jsonUser)
    else:
        return HttpResponse("Please use POST")

@csrf_exempt
def loginUnity(request):
    if request.method == "POST":
        var = (request.body)#.decode()
        dicc = ast.literal_eval(var.decode('utf-8'))
        #jsonUser = json.loads(var)
        u = usuario.objects.filter(usuario=(dicc['body']))
        if u is not None:
            print(u[0].toJson())
            return HttpResponse(str(json.dumps(u[0].toJson())).encode('utf-8')) #JsonResponse(jsonUser)
        else:
            print("Error in change")
            return HttpResponse("Not register")
    else:
        return HttpResponse("Please use POST")