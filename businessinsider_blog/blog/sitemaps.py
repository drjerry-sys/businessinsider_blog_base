from django.contrib.sitemaps import Sitemap
from django.urls import reverse
from .models import Post


class PostSitemap(Sitemap):
    changefreq = 'daily'
    priority = 1.0

    def items(self):
        return Post.objects.all()

    def lastmod(self, obj):
        return obj.updated

    # def location(self, item):
    #     return