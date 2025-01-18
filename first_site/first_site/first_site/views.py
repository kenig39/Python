from django.shortcuts import render


def home(request):
    return render(request, 'robotix.html')
def index(request):
    return render(request, 'index.html')
def catalog(request):
    return render(request, 'catalog.html')