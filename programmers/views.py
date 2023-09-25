from django.shortcuts import render

from .models import Programmer


# Create your views here.

def index(request):
    programmers = Programmer.objects.all()
    return render(request, 'programmers/index.html', {'programmers': programmers})


def programmer_full_information(request, programmer_id):
    programmer = Programmer.objects.get(pk=programmer_id)
    projects = programmer.project_set.all()
    return render(request, 'programmers/programmer_full_information.html',
                  {'programmer': programmer, 'projects': projects})


def page_not_found_404(request, exception):
    return render(request, 'programmers/page_not_found.html', status=404)
