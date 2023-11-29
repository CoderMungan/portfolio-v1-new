from django.db import models
from autoslug import AutoSlugField

# Create your models here.
class LabelCategory(models.Model):
    name = models.CharField(("Label Name"), max_length=50)

    class Meta:
        verbose_name_plural = "Label Category"

    def __str__(self) -> str:
        return self.name

class CategoryBlog(models.Model):
    name = models.CharField(("Category Name"), max_length=50)
    slug = AutoSlugField(populate_from='name', editable=False, always_update=True, blank=True)

    class Meta:
        verbose_name_plural = "Category Blog"
    
    def __str__(self) -> str:
        return self.name
    

class Blog(models.Model):
    category = models.ForeignKey(CategoryBlog, verbose_name=("Category"), on_delete=models.CASCADE)
    title = models.CharField(("Title"), max_length=200)
    content = models.TextField(("Content"))
    createAt = models.DateTimeField(("Create At"), auto_now=True, auto_now_add=False)
    label = models.ManyToManyField(LabelCategory, verbose_name=("Label's"))
    slug = AutoSlugField(populate_from='title', editable=False, always_update=True, blank=True)

    class Meta:
        verbose_name_plural = "Blog"

    def __str__(self) -> str:
        return self.title
    

class Article(models.Model):
    title = models.CharField(("Article Title"), max_length=50)
    content = models.TextField(("Article Content"))
    createAt = models.DateTimeField(("Created at"), auto_now=True, auto_now_add=False)
    label = models.ManyToManyField(LabelCategory, verbose_name=("Label's"))
    slug = AutoSlugField(populate_from='title', editable=False, always_update=True, blank=True)

    class Meta:
        verbose_name_plural = "Article"

    def __str__(self) -> str:
        return self.title