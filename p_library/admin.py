from django.contrib import admin
from .models import Book, Author, Redaction, Friend

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    pass


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):

    @staticmethod
    def author_full_name(obj):
        return obj.author.full_name

    list_display = ('title', 'author_full_name',)
    fields = ('ISBN', 'title', 'description', 'year_release', 'author', 'price', 'copy_count', 'redaction')
    
    
@admin.register(Redaction)
class RedactionAdmin(admin.ModelAdmin):
    pass

@admin.register(Friend)
class Friend(admin.ModelAdmin):

    @staticmethod
    def friend_name(obj):
        return obj.friend.name
    list_display = ('name', 'surname', 'book', 'data')
    fields = ('name', 'surname', 'book', 'data')