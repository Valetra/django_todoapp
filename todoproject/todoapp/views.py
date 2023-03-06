from django.shortcuts import render
from .models import TodoListItem
from django.http import HttpResponseRedirect 

def todoappView(request):
    all_todo_items = TodoListItem.objects.all()
    return render(request, 'home.html', {'all_items':all_todo_items})

def addTodoView(request):
    x = request.POST['content']
    new_item = TodoListItem(content = x, user= request.user)
    new_item.save()

    return HttpResponseRedirect('/') 

def deleteTodoView(request, i):
    y = TodoListItem.objects.get(id= i)
    y.delete()
    return HttpResponseRedirect('/')

def completeTodoItemView(request, i):
    y = TodoListItem.objects.get(id= i)
    y.done = True
    y.save()
    return HttpResponseRedirect('/')

def deleteAllCompletedItemsView(request):
    all_todo_items = TodoListItem.objects.all()
    for i in all_todo_items:
        if i.done:
            i.delete()
    return HttpResponseRedirect('/')
