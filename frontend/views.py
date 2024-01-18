from django.shortcuts import render


# Create your views here.

def HomeView(request):
    return render(request, 'frontend/home.html')


def AboutView(request):
    return render(request, 'frontend/about.html')


def ServicesView(request):
    return render(request, 'frontend/services.html')


def ContactView(request):
    return render(request, 'frontend/contact.html')


def error_404_view(request, exception):
    return render(request, 'frontend/404.html')
