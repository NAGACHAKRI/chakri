from django.shortcuts import render
from .models import todoitem
from django.http import HttpResponseRedirect



def show(request):
    all_todoitems=todoitem.objects.all()
    return render(request,"todo/show.html",{"all_todoitems":all_todoitems})


def add(request):
    all_todoitems=todoitem.objects.all()
    return render(request,"todo/add.html",{"all_todoitems":all_todoitems})


def delete(request):
    all_todoitems=todoitem.objects.all()
    return render(request,"todo/delete.html",{"all_todoitems":all_todoitems})


def home(request):
     all_todoitems=todoitem.objects.all()
     return render(request,"todo/home.html",{"all_todoitems":all_todoitems})

def todo(request):
    all_todoitems=todoitem.objects.all()
    return render(request,"todo/index.html",{"all_todoitems":all_todoitems})

def addtodo(request):
    c=request.POST["content"]
    new_item=todoitem(content=c)
    new_item.save()
    all_todoitems=todoitem.objects.all()
    return HttpResponseRedirect("/todo/")

def deletetodo(request,todo_id):
    ch=todoitem.objects.get(id=todo_id)
    ch.delete()
    return HttpResponseRedirect("/todo/")

def updatetodo(request,uptodo_id):
    schedule=todoitem.objects.get(id=uptodo_id)
    new_schedule=request.POST["new_schedule"]
    schedule.content=new_schedule
    schedule.save()
    return HttpResponseRedirect("/todo/")


    
