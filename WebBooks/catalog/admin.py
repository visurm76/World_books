from django.contrib import admin
from .models import Autor, Book, Genre, Language, Status, Bookinstance

# admin.site.register(Autor)
# admin.site.register(Book)
admin.site.register(Genre)
admin.site.register(Language)
admin.site.register(Status)
# admin.site.register(Bookinstance)


@admin.register(Autor)
class AutorAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'data_of_birth', 'data_of_death')


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'genre', 'language', 'display_autor')
    list_filter = ('genre', 'autor')



@admin.register(Bookinstance)
class BookinstanceAdmin(admin.ModelAdmin):
    list_filter = ('book', 'status')
    fieldsets = (('Экземпляр книги', {'fields': ('book', 'imprint', 'inv_nom')}), ('Статус окончание его действия', {'fields': ('status', 'due_back')}),)


