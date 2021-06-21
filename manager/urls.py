from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('courses/', views.courses, name='courses'),
    path('books/', views.books, name='books'),
    path('search/', views.search, name='search'),
    path('about/', views.about, name='about'),
    path('blog/', views.blog, name='blog'),
    path('notes/', views.notes, name='notes'),
    path('contact/', views.contact, name='contact'),

]
