from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.views import generic
from .models import TodoItem
from django.views.generic import TemplateView


class IndexView(generic.ListView):
    model = TodoItem
    template_name = 'todo/index.html'


def addTodo(request):
    new_item = TodoItem(content=request.POST['content'])
    new_item.save()
    return HttpResponseRedirect(reverse('todo:index'))


def deleteTodo(request, todo_id):
    delete_item = TodoItem.objects.get(id=todo_id)
    delete_item.delete()
    return HttpResponseRedirect(reverse('todo:index'))



