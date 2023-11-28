from django.contrib import admin
from .models import *

# Register your models here.
class CategoryBlogAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']

class BlogAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug']

admin.site.register(LabelCategory)
admin.site.register(CategoryBlog, CategoryBlogAdmin)
admin.site.register(Blog, BlogAdmin)