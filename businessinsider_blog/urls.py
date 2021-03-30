"""businessinsider_blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.contrib.sitemaps.views import sitemap
from businessinsider_blog.blog import sitemaps as site
from django.views.generic import TemplateView
from businessinsider_blog.blog import views
from businessinsider_blog import settings
from django.contrib.staticfiles.urls import static, staticfiles_urlpatterns

sitemaps = {
    'posts':site.PostSitemap(),
}

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.top_stories, name='homepage'),
    path('search/', views.search_form, name='search'),
    path('trending/<slug:exact_post>/', views.top_stories, {'det':3}, name='story_new'),
    path('news/<slug:exact_post>/', views.top_stories, {'det':4}, name='news'),
    path('local/<str:cat>/<slug:exact_post>/', views.top_stories, {'det':1}, name='stories'),
    path('local/<str:cat>/', views.top_stories, {'det':2}, name='categories'),
    path('sitemap.xml', sitemap, {'sitemaps':sitemaps}, name='django.contrib.sitemaps.views.sitemap')
]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)