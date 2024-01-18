from django.contrib.sitemaps import Sitemap
from django.urls import reverse


class StaticViewSitemap(Sitemap):
    def items(self):
        return ['frontend:about', 'frontend:services', 'frontend:home', 'frontend:contact', ]

    def location(self, item):
        return reverse(item)
