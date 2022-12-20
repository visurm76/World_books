from django.shortcuts import render
from django.http import HttpResponse
from .models import Book, Autor, Bookinstance, Genre
from django.views import generic


# Create your views here.

def index(request):
    # Генерация "количеств"  некоторых главных объектов
    num_books = Book.objects.all().count()
    num_instances = Bookinstance.objects.all().count()

    # Доступные книги (статус= 'На складе')
    # Здесь метод 'all()' применен по умолчанию.
    num_instances_available = Bookinstance.objects.filter(status__exact = 2).count()
    num_autor = Autor.objects.count()

    # Отрисовка НТМL-шаблона index.html с данными
    # внутри переменной context
    return render(request, 'index.html', context={'num_books':num_books, 'num_instances':num_instances,
                                                      'num_instances_available':num_instances_available,
                                                      'num_autor':num_autor},

                  )

class BookListView(generic.ListView):
    model = Book