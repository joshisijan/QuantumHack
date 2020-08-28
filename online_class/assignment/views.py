from django.shortcuts import render, HttpResponse
from .forms import *
from .models import *


def assignment_home(request):
    assignments = Assignment.objects.all()
    context = {
        'assignments' : assignments
    }

    return render(request, 'assignment/assignment_home.html', context)


def assignment_add(request):
    if request.method == 'POST':
        form = AssignmentAddForm(request.POST, request.FILES)
        if form.is_valid():
            assignment = form.save(commit=False)
            assignment.owner = request.user
            assignment.save()
            return redirect('assignment_home')
    else:
        form = AssignmentAddForm()
    
    return render(request, 'assignment/assignment_add.html', {'form':form})

def assignment_update(request):
    pass


