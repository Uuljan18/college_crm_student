
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.urls import reverse_lazy
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)

from .models import Student
from .forms import StudentForm


class StudentListView(ListView):
    model = Student
    template_name = 'users/student_list.html'
    context_object_name = 'students'
    paginate_by = 10

    def get_queryset(self):
        queryset = super().get_queryset()

        search = self.request.GET.get('search', '').strip()
        group = self.request.GET.get('group', '').strip()

        if search:
            queryset = queryset.filter(
                Q(first_name__icontains=search) |
                Q(last_name__icontains=search) |
                Q(middle_name__icontains=search)
            )

        if group:
            queryset = queryset.filter(group=group)

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['search'] = self.request.GET.get(
            'search', ''
        )
        context['selected_group'] = self.request.GET.get(
            'group', ''
        )

        context['groups'] = (
            Student.objects.order_by('group')
            .values_list('group', flat=True)
            .distinct()
        )

        return context


class StudentDetailView(DetailView):
    model = Student
    template_name = 'users/student_detail.html'
    context_object_name = 'student'


class StudentCreateView(LoginRequiredMixin, CreateView):
    model = Student
    form_class = StudentForm
    template_name = 'users/student_form.html'
    success_url = reverse_lazy('student_list')
    extra_context = {
        'page_title': 'Добавить студента'
    }


class StudentUpdateView(LoginRequiredMixin, UpdateView):
    model = Student
    form_class = StudentForm
    template_name = 'users/student_form.html'
    success_url = reverse_lazy('student_list')
    extra_context = {
        'page_title': 'Редактировать студента'
    }


class StudentDeleteView(LoginRequiredMixin, DeleteView):
    model = Student
    template_name = 'users/student_confirm_delete.html'
    success_url = reverse_lazy('student_list')
    context_object_name = 'student'
