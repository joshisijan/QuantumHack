from django.shortcuts import render, redirect, HttpResponse
from .forms import *
from .models import *


def exam_view(request):
    if request.user.is_authenticated:
        if request.user.is_teacher:
            return redirect('exam_page_details_teacher')
        else:
            return redirect('exam_page_details_student')
    return redirect('login')

'''

Teachers Views

'''

def exam_home(request):
    exams = ExamQuestions.objects.all()
    num = int(0)
    context = {
        'exams': exams,
        'num': num
    }

    return render(request, 'teachers/exam_home.html', context)


def exam_add(request):
    if request.method == 'POST':
        form = ExamQuestionAddForm(request.POST, request.FILES)
        if form.is_valid():
            exam = form.save(commit=False)
            exam.owner = request.user
            exam.save()
            return redirect('exam_page_details_teacher')
    else:
        form = ExamQuestionAddForm()
    
    return render(request, 'teachers/exam_add.html', {'form':form})



def exam_update(request, pk):
    exam = ExamQuestions.objects.get(pk=pk)
    if request.method == 'POST':
        form = examAddForm(request.POST, request.FILES)
        if form.is_valid():
            exam = form.save(commit=False)
            exam.owner = request.user
            exam.save()
            return redirect('exam_page_details')
    else:
        form = ExamQuestionAddForm(instance=exam)
    
    return render(request, 'teachers/exam_update.html', {'form':form, 'exam':exam})


def exam_delete(request,pk):
    exam = ExamQuestions.objects.get(pk=pk)
    exam.delete()

    return redirect('exam_page_details_teacher')

'''

Student Views

'''

def student_exam_home(request):
    return HttpResponse("Student_exam")


def exam_submit(request, pk):
    pass