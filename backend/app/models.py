from django.db import models

# Create your models here.
class CategoryBlog(models.Model):
    name = models.CharField(("Category Name"), max_length=50)
    slug = models.SlugField(("Slug"))


class Blog(models.Model):
    name = models.ForeignKey(CategoryBlog, verbose_name=("Category Name"), on_delete=models.CASCADE)
    title = models.CharField(("Title"), max_length=200)
    content = models.TextField(("Content"))
    createAt = models.DateTimeField(("Create At"), auto_now=True, auto_now_add=True)

