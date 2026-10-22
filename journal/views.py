from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.shortcuts import render, redirect, get_object_or_404
from .models import Groups, Student, Grade
from .forms import GroupForm, StudentForm, GradeForm
# Create your views here.
def index_view(request):
    return render(request, 'journal/index.html')

def contacts_view(request):
    return render(request, 'journal/contacts.html')

def about_view(request):
    return render(request, 'journal/about.html')

def students(request):
    all_students = Student.objects.all()

    context = {
        'page_title': 'Список студентов',
        'students_list': all_students,
    }

    return render(request, 'journal/students.html', context)

class GroupListView(ListView):
    model = Groups
    template_name = 'journal/groups.html'
    context_object_name = 'groups_list'

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.order_by('name')


class GroupDetailView(DetailView):
    model = Groups
    template_name = 'journal/group_detail.html'
    context_object_name = 'group'

class GroupCreateView(CreateView):
    model = Groups
    form_class = GroupForm
    template_name = 'journal/groups_form.html'
    success_url = reverse_lazy('groups')

class GroupUpdateView(UpdateView):
    model = Groups
    form_class = GroupForm
    template_name = 'journal/groups_form.html'
    success_url = reverse_lazy('groups')

class GroupDeleteView(DeleteView):
    model = Groups
    template_name = 'journal/groups_delete_confirm.html'
    success_url = reverse_lazy('groups')

def group_detail_view(request, group_id):
    group = get_object_or_404(Groups, pk=group_id)
    students = Student.objects.filter(group=group)

    if request.method == 'POST':
        form = GradeForm(request.POST)
        if form.is_valid():
            Grade.objects.create(
                value=form.cleaned_data['value'],
                student=form.cleaned_data['student'],
                subject=form.cleaned_data['subject'],
            )
            return redirect('group_detail', group_id=group_id)
    else:
        form = GradeForm()

    form.fields['student'].queryset = students
    grades = Grade.objects.filter(student__in=students)
    context = {
        'form': form,
        'student': students,
        'group': group,
        'grades': grades,
    }

    return render(request, 'journal/group_detail.html', context)


def student_detail_view(request, student_id):
    student = Student.objects.get(pk=student_id)
    context = {
        'student': student
    }

    return render(request, 'journal/student_detail.html', context)

def groups_add_view(request):
    if request.method == 'POST':
        form = GroupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('groups')
    else:
        form = GroupForm()

    context = {
            'form': form
            }
    return render(request, 'journal/groups_form.html', context)

def students_add_view(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('students')
    else:
        form = StudentForm()

    context = {
        'form': form
    }
    return render(request, 'journal/students_form.html', context)

def group_edit_view(request, group_id):
    group = get_object_or_404(Groups, pk=group_id)

    if request.method == 'POST':
        form = GroupForm(request.POST, instance=group)
        if form.is_valid():
            form.save()
            return redirect('group_detail', group_id=group_id)
    else:
        form = GroupForm(instance=group)

    context = {
        'form': form,
        'group': group,
    }
    return render(request, 'journal/groups_form.html', context)

def students_edit_view(request, student_id):
    student = get_object_or_404(Student, pk=student_id)
    if request.method == 'POST':
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return redirect('students')
    else:
        form = StudentForm(instance=student)

    context = {
        'form': form,
        'student': student,
    }
    return render(request, 'journal/students_form.html', context)

def groups_delete_view(request, group_id):
    group = get_object_or_404(Groups, pk=group_id)

    if request.method == 'POST':
        group.delete()
        return redirect('groups')
    context = {
        'group': group,
    }
    return render(request, 'journal/groups_delete_confirm.html', context)

def student_delete_view(request, student_id):
    student = get_object_or_404(Student, pk=student_id)

    if request.method == 'POST':
        student.delete()
        return redirect('students')

    context = {
        'student': student,
    }
    return render(request, 'journal/students_delete_confirm.html', context)

def grade_add_view(request):
    if request.method == 'POST':
        form = GradeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = GradeForm()

    context = {
        'form': form,
        'page_title': 'Выставить новую оценку'
    }
    return render(request, 'journal/grade_form.html', context)

