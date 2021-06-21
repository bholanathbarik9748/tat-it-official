from django.shortcuts import render

# Create your views here.


def index(request):
    return render(request, 'index.html')


def courses(request):
    return render(request, 'courses.html')


def search(request):
    return render(request, 'search.html')


def books(request):
    return render(request, 'books.html')


def about(request):
    return render(request, 'about.html')


def blog(request):
    return render(request, 'blog.html')


def notes(request):
    return render(request, 'notes.html')

def contact(request):
    return render(request, 'contact.html')
