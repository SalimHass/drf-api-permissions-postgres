from django.contrib import admin
from .models import Book

# Register your models here.
@admin.register(Book)
class AdminBook(admin.ModelAdmin):
    list_display=["title","summary","author","rate","review","reviewer","date_reviewed","review_updated"]

