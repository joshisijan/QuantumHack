from django.shortcuts import render

def assignment_view(request):
    context = {

    }

    return render(request, 'assignment.html', context)
