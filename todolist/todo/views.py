from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from django.views.generic.edit import UpdateView
from django.views.generic.edit import DeleteView
from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Task
# Create your views here.

def home(request):
    return render(request,'home.html')


class TasksList(LoginRequiredMixin,ListView):
    model = Task
    context_object_name = 'tasks'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(TasksList, self).get_context_data(**kwargs)
        context['tasks'] =context['tasks'].filter(user = self.request.user)
        return context


class TaskDetail(LoginRequiredMixin,DetailView):
    model = Task
    context_object_name = 'task'

    def get_queryset(self):
        base_qs = super(TaskDetail, self).get_queryset()
        return base_qs.filter(user = self.request.user)

class TaskCreate(LoginRequiredMixin,CreateView):
    model = Task
    fields = ['title', 'description','completed',]
    success_url = reverse_lazy('tasks')

    def form_valid(self, form):
        form.instance.user = self.request.user
        messages.success(self.request,  "🎉 The task was created succefully.")
        return super(TaskCreate,self).form_valid(form)



class TaskUpdate(LoginRequiredMixin,UpdateView):
    model = Task
    fields = ['title', 'description', 'completed']
    success_url = reverse_lazy('tasks')

    def form_valid(self, form):
        messages.success(self.request, "🎉 The task was updated succefully.")
        return super(TaskUpdate, self).form_valid(form)

    def get_queryset(self):
        base_qs = super(TaskUpdate, self).get_queryset()
        return base_qs.filter(user = self.request.user)


class TaskDelete(LoginRequiredMixin,DeleteView):
    model = Task
    context_object_name = 'task'
    success_url = reverse_lazy('tasks')

    def form_valid(self, form):
        messages.success(self.request, "🎉 The task was deleted succefully.")
        return super(TaskDelete, self).form_valid(form)

    def get_queryset(self):
        base_qs = super(TaskDelete, self).get_queryset()
        return base_qs.filter(user = self.request.user)
