from django.shortcuts import render, HttpResponse, redirect
from .forms import *
from .models import *


def home(request):
    if request.user.is_authenticated:
        if request.user.is_teacher:
            return redirect('teachers:assignment_page')
        else:
            return redirect('students:assignment_page')
    return redirect('login')


def assignment_home(request):
    assignments = Assignment.objects.filter(owner_id = request.user.id)
    num = int(0)
    context = {
        'assignments' : assignments,
        'num' : num
    }

    return render(request, 'teachers/assignment_home.html', context)


def assignment_add(request):
    if request.method == 'POST':
        form = AssignmentAddForm(request.POST, request.FILES)
        if form.is_valid():
            assignment = form.save(commit=False)
            assignment.owner = request.user
            assignment.save()
            return redirect('teachers:assignment_page')
    else:
        form = AssignmentAddForm()
    
    return render(request, 'teachers/assignment_add.html', {'form':form})


def assignment_update(request, pk):
    assignment = Assignment.objects.get(pk=pk)
    if request.method == 'POST':
        form = AssignmentAddForm(request.POST, request.FILES)
        if form.is_valid():
            assignment = form.save(commit=False)
            assignment.owner = request.user
            assignment.save()
            return redirect('assignment_page')
    else:
        form = AssignmentAddForm(instance=assignment)
    
    return render(request, 'teachers/assignment_update.html', {'form':form, 'assignment':assignment})


def assignment_delete(request,pk):
    assignment = Assignment.objects.get(pk=pk)
    assignment.delete()

    return redirect('teachers:assignment_page')



def submitted_assignment(request,pk):
    answers = StudentAnswer.objects.filter(assignment__id = pk)
    print(pk)
    context ={
        'answers': answers,
    }
    
    return render(request, 'teachers/submitted_assignment.html', context)





def student_assignment_home(request):
    sem = request.user.student.sem

    assignments = Assignment.objects.filter(subject__sem = sem)
    num = int(0)
    context = {
        'assignments' : assignments,
        'num' : num
    }

    return render(request, 'students/assignment_home.html', context)


def student_assignment_upload(request):
    if request.method == 'POST':
        form = AssignmentSubmitForm(request.POST, request.FILES)
        if form.is_valid():
            studentanswer = form.save(commit=False)
            studentanswer.student = request.user
            studentanswer.save()
            return redirect('students:assignment_page')
    else:
        form = AssignmentSubmitForm()
    
    return render(request, 'students/assignment_upload.html', {'form':form})
        



