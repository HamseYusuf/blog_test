from django.urls import path
from .import views

urlpatterns = [
    path("",views.Home ,name="blog-home"),
    path('blog/<int:pk>/' , views.blog_detail , name="blog-detail"),
    path('update/<int:pk>/' , views.blog_update , name="blog-update"),
    path("create-blog/",views.create_blog ,name="blog-create"),
    path("about/",views.About ,name="blog-about")
]
