from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'mysite/header.html', )

def home(request):
    return render(request, 'mysite/home.html', )

def test(request):
    return render(request, 'mysite/test.html', )
def test2(request):
    return render(request, 'mysite/test2.html', )

def git(request):
    return render(request, 'mysite/memo/git.html', )

def idea(request):
    return render(request, 'mysite/humanskill/idea.html', )

def excel(request):
    return render(request, 'mysite/memo/excel.html', )

def java(request):
    return render(request, 'mysite/techskill/java/java.html', )

def javabase(request):
    return render(request, 'mysite/techskill/java/javabase.html', )

def javaconst(request):
    return render(request, 'mysite/techskill/java/javaconst.html', )
