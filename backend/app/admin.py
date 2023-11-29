from django.contrib import admin
from .models import *


class CategoryBlogAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']

class CategoryArticleAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']

class BlogAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug']

class ArticleAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug']

admin.site.register(LabelCategory)
admin.site.register(CategoryBlog, CategoryBlogAdmin)
admin.site.register(CategoryArticle, CategoryArticleAdmin)
admin.site.register(Blog, BlogAdmin)
admin.site.register(Article)