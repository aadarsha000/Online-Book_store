from django.contrib import admin
from .models import Category, Publication, Author, Book

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', ]
    prepopulated_fields = {'slug':('name',)}

class PublicationAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', ]
    prepopulated_fields = {'slug':('name',)}

class AuthorAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', ]
    prepopulated_fields = {'slug':('name',)}

class BookAdmin(admin.ModelAdmin):
    list_display = ['name', 'author','price', 'publication', 'published_date', 'update_date']
    list_filter = ['name', 'author', 'publication']
    prepopulated_fields = {'slug':('name',)}

admin.site.register(Category, CategoryAdmin)
admin.site.register(Publication, PublicationAdmin)
admin.site.register(Author, AuthorAdmin)
admin.site.register(Book, BookAdmin)