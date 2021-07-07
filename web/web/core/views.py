from .models import Task
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .forms import TaskForm
from django.urls import reverse, reverse_lazy
from django.contrib import messages


class TaskListView(ListView):
    model = Task
    template_name = 'index.html'
    context_object_name = 'list_task'


class TaskDetailView(DetailView):
    model = Task
    template_name = 'detail.html'
    context_object_name = 'get_task'


class SuccessMessage:
    @property
    def success_mes(self):
        return False

    def form_valid(self, form):
        messages.success(self.request, self.success_mes)
        return super().form_valid(form)


class TaskCreateView(SuccessMessage, CreateView):
    model = Task
    template_name = 'edit_page.html'
    form_class = TaskForm
    success_url = reverse_lazy('edit')
    success_mes = 'Запись создана'

    def get_context_data(self, **kwargs):
        kwargs['list_task'] = Task.objects.all().order_by('-id')
        return super().get_context_data(**kwargs)


class TaskUpdateView(SuccessMessage, UpdateView):
    model = Task
    template_name = 'edit_page.html'
    form_class = TaskForm
    success_url = reverse_lazy('edit')
    success_mes = 'Запись успешно обновлена'

    def get_context_data(self, **kwargs):
        kwargs['update'] = True
        return super().get_context_data(**kwargs)


class TaskDeleteView(DeleteView):
    model = Task
    template_name = 'edit_page.html'
    success_url = reverse_lazy('edit')
    success_mes = 'Запись успешно удалена'

    def post(self, request, *args, **kwargs):
        messages.success(self.request, self.success_mes)
        return super().post(request)