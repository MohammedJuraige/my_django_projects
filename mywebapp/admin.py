# mywebapp/admin.py
from django.contrib import admin
from ckeditor.widgets import CKEditorWidget
from django.db import models
from django_summernote.admin import SummernoteModelAdmin
from .models import Post, Page

# Register Page model
@admin.register(Page)
class PageAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.TextField: {'widget': CKEditorWidget},
    }
    list_display = ('title', 'slug')
    prepopulated_fields = {'slug': ('title',)}


# Register Post model using the PostAdmin class
@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):
    # Enable Summernote for 'content' field
    summernote_fields = ('content',)

    # Optional: customize the admin panel
    list_display = ('title', 'created_at', 'updated_at')
    prepopulated_fields = {'slug': ('title',)}
