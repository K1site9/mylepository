from django.shortcuts import render
from . import models
from django.views import View
from django.utils import timezone
# Create your views here.
def search(request):
    w = request.GET.get('word')
    d = {
        'word' : w,
        'article_qs' : models.Article.objects.filter(title__contains=w).order_by('primaryNum')
    }
    return render(request, 'mysite/search.html', d)

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

def javaaccess(request):
    return render(request, 'mysite/techskill/java/javaaccess.html', )

def javageneric(request):
    return render(request, 'mysite/techskill/java/javageneric.html', )

def javacollection(request):
    return render(request, 'mysite/techskill/java/javacollection.html', )

def javaexception(request):
    return render(request, 'mysite/techskill/java/javaexception.html', )

def javaramuda(request):
    return render(request, 'mysite/techskill/java/javaramuda.html', )

def javathread(request):
    return render(request, 'mysite/techskill/java/javathread.html', )

def javadate(request):
    return render(request, 'mysite/techskill/java/javadate.html', )

class homeView(View):
    def get(self, request, *args, **kwargs):
        d = {
            'article_qs': models.Article.objects.all().order_by('-updateTime')[:5]
        }
        return render(request, 'mysite/home.html', d)

    def post(self, request, *args, **kwargs):
        p = request.POST.get('input')
        url = request.POST.get('url')
        if p is None:
            models.Question(text=p, updateTime=timezone.now()).save()
        d = {
            'article_qs': models.Article.objects.all().order_by('-updateTime')[:5],
            'input' : p
        }

        return render(request, 'mysite/home.html', d)

class mysiteView(View):
    def get(self, request, *args, **kwargs):
        d = {
            'article_qs': models.Article.objects.all().order_by('-updateTime')[:5]
        }
        return render(request, 'mysite/mysite.html', d)

def kihonjouhou(request):
    return render(request, 'mysite/memo/kihonjouhou.html', )