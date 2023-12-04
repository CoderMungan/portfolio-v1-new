from django.urls import path
from .views import *

urlpatterns = [
    path("blog", blog_main_response_get, name="blog_main_response_get"),
    path("blog/<slug>", blog_special_theme_get, name="blog_main_response_single_get"),
    path("categoryblog", category_blog_response_get, name="category_blog_response_get"),
    path("article", article_main_response_get, name="article_main_response_get"),
    path(
        "article/<slug>",
        article_special_theme_get,
        name="article_main_response_single_get",
    ),
    path("categoryarticle", category_article_response_get, name="category_article_response_get"),
    path("contact", contact_form_post, name="contact_form_post"),
]