from django.contrib import admin

# Register your models here.
from django.contrib.auth.models import User

from manager.models import Book, Comment

class CommentAdmin(admin.StackedInline):
    model = Comment
    extra = 2

class BookAdmin(admin.ModelAdmin):
    inlines = [CommentAdmin]

admin.site.register(Book, BookAdmin)