from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'mysite/header.html', )

def home(request):
    return render(request, 'mysite/home.html', )

def test(request):
    return render(request, 'mysite/test.html', )