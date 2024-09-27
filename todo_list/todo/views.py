from django.forms import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib import messages
from .models import Task
# Create your views here.

# DANH SÁCH CÁC PHẦN TỬ
class TaskList(ListView):
    model = Task
    context_object_name = 'tasks'

# XEM CHI TIẾT CÁC PHẦN TỬ TRONG DANH SÁCH
class TaskDetail(DetailView):
    model = Task
    context_object_name = 'task'

# THÊM MỚI PHẦN TỬ VÀO DANH SÁCH
class TaskCreate(CreateView):
    model = Task
    fields = ['title','description','completed']
    success_url = reverse_lazy('tasks')

    def form_valid(self, form):
        form.instance.user = self.request.user
        messages.success(self.request, "The task was created successfully.")
        return super(TaskCreate,self).form_valid(form)
#  CẬP NHẬT PHẦN TỬ TRONG DANH SÁCH
class TaskUpdate(UpdateView):
    model = Task
    fields = ['title','description','completed']
    success_url = reverse_lazy('tasks')
    
    def form_valid(self, form):
        messages.success(self.request, "The task was update successfully.")
        return super(TaskUpdate,self).form_valid(form)
    
def home(request):
    return render(request, 'home.html')