from django.contrib import admin
from .models import Autor, Book, Genre, Language, Status, Bookinstance


admin.site.register(Autor)
admin.site.register(Book)
admin.site.register(Genre)
admin.site.register(Language)
admin.site.register(Status)
admin.site.register(Bookinstance)

