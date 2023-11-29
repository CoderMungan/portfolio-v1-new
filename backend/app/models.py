from django.db import models
from autoslug import AutoSlugField


# LabelCategory ORM Start
class LabelCategory(models.Model):
    name = models.CharField(("Label Name"), max_length=50)

    class Meta:
        verbose_name_plural = "Label Category"

    def __str__(self) -> str:
        return self.name
# LabelCategory ORM End


# CategoryBlog ORM Start
class CategoryBlog(models.Model):
    name = models.CharField(("Category Name"), max_length=50)
    slug = AutoSlugField(
        populate_from="name", editable=False, always_update=True, blank=True
    )

    class Meta:
        verbose_name_plural = "Category Blog"

    def __str__(self) -> str:
        return self.name
# CategoryBlog ORM End


# CategoryArticle ORM Start
class CategoryArticle(models.Model):
    name = models.CharField(("Category Name"), max_length=50)
    slug = AutoSlugField(
        populate_from="name", editable=False, always_update=True, blank=True
    )

    class Meta:
        verbose_name_plural = "Category Article"

    def __str__(self) -> str:
        return self.name
# CategoryArticle ORM End


# Blog ORM Start
class Blog(models.Model):
    category = models.ForeignKey(
        CategoryBlog, verbose_name=("Category"), on_delete=models.CASCADE
    )
    title = models.CharField(("Title"), max_length=200)
    content = models.TextField(("Content"))
    createAt = models.DateTimeField(("Create At"), auto_now=True, auto_now_add=False)
    label = models.ManyToManyField(LabelCategory, verbose_name=("Label's"))
    image = models.ImageField(
        ("Image"),
        upload_to="Blog",
        height_field=None,
        width_field=None,
        max_length=None,
        blank=True,
    )
    slug = AutoSlugField(
        populate_from="title", editable=False, always_update=True, blank=True
    )

    class Meta:
        verbose_name_plural = "Blog"

    def __str__(self) -> str:
        return self.title
# Blog ORM End


# Article ORM Start
class Article(models.Model):
    category = models.ForeignKey(
        CategoryArticle, verbose_name=("Category"), on_delete=models.CASCADE
    )
    title = models.CharField(("Article Title"), max_length=50)
    content = models.TextField(("Article Content"))
    createAt = models.DateTimeField(("Created at"), auto_now=True, auto_now_add=False)
    label = models.ManyToManyField(LabelCategory, verbose_name=("Label's"))
    image = models.ImageField(
        ("Image"),
        upload_to="Article",
        height_field=None,
        width_field=None,
        max_length=None,
        blank=True,
    )
    slug = AutoSlugField(
        populate_from="title", editable=False, always_update=True, blank=True
    )

    class Meta:
        verbose_name_plural = "Article"

    def __str__(self) -> str:
        return self.title
# Article ORM End
