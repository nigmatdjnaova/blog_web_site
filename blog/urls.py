from django.contrib import admin
from django.urls import path
from common.views import index,about,portfolio,blog, blog_detail
from django.conf import settings
from django.conf.urls.static import static 

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", index),
    path("about/" , about),
    path("portfolio/", portfolio),
    path("blog/", blog, name='blog'),
    path("blog/<int:pk>/", blog_detail, name="blog_detail"),
    

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
