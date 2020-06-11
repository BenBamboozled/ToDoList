from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.http import HttpResponse, JsonResponse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Item
from django.contrib.auth.models import User
from .forms import AddTaskForm
import datetime

class ItemListView(LoginRequiredMixin, ListView):
    model = Item
    template_name ='toDoList/home.html' #<app>/</model>_<viewtype>.html
    context_object_name = 'tasks'
    ordering = ['-date']

    def get_queryset(self):
        return Item.objects.filter(author=self.request.user)

    

class ItemDetailView(DetailView):
    model = Item


class ItemCreateView(LoginRequiredMixin, CreateView):
    model = Item
    fields = ['task','date']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
class ItemUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Item
    fields = ['task','date']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        item = self.get_object()
        if self.request.user == item.author:
            return True
        return False

class ItemDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Item
    success_url='/'
    def test_func(self):
        item = self.get_object()
        if self.request.user == item.author:
            return True
        return False

def deleteTask(request):
    if request.method == 'POST':
        pk = request.POST['value']

        task = Item.objects.get(id=pk)
        task.delete()

    return JsonResponse('deleted', safe=False)


def about(request):
    return render(request, 'toDoList/about.html')

def complete(request, pk):
    task = Item.objects.get(id = pk)
    
    if(task.complete):
        task.complete = False
    else:
        task.complete = True
    
    task.save()

    return JsonResponse('data', safe=False)

def create(request):
    if request.method == 'POST':
        task = request.POST['task']
        date = request.POST['date'] 

    Item.objects.create(
        task  = task,
        date = date,
        author = request.user
    )


    return JsonResponse('refresh', safe=False)

def clearList(request):
    tasks = Item.objects.filter(author=request.user)

    for task in tasks:
        task.delete()
    

    return JsonResponse('cleared', safe=False)

def getTextFile(request):
    txt = ""
    tasks = Item.objects.filter(author=request.user)

    filename = "to-do-list.txt"

    for task in tasks:
        date = task.date.strftime("%m-%d-%y")
        if task.complete:
            complete = 'Yes'
        else:
            complete = 'No'
        txt += "Task: {0:20} Date: {1:20} Completed: {2} \n".format(task.task, date,complete)

    response = HttpResponse(txt,content_type='text/plain')
    response['Content-Disposition']='attachment; filename{0}'.format(filename)
    return response




