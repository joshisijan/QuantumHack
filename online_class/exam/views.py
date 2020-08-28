from django.shortcuts import render

def exam_view(request):
    context = {

    }

    return render(request, 'exam.html', context)
