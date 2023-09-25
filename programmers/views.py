from django.shortcuts import render


# Create your views here.

def index(request):
    return render(request, 'programmers/index.html')


def page_not_found_404(request, exception):
    return render(request, 'programmers/page_not_found.html', status=404)
