from django.contrib.auth.models import User
from django.shortcuts import render, redirect

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


def new_programmer(request):
    return render(request, 'programmers/add_new_programmer.html', )


def new_programmer_data(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        age = request.POST.get('age')
        language = request.POST.get('language')
        framework = request.POST.get('framework')
        experience = request.POST.get('experience')

        user = User.objects.create_user(
            username=first_name,
            password='aaa12345',
            first_name=first_name,
            last_name=last_name
        )

        programmer = Programmer.objects.create(
            user=user,
            age=age,
            language=language,
            framework=framework,
            experience=experience
        )
        return redirect('home')


def page_not_found_404(request, exception):
    return render(request, 'programmers/page_not_found.html', status=404)
