from django.contrib.sitemaps import Sitemap
from medapp.models import *
from django.urls import reverse, NoReverseMatch


class BlogSiteMap(Sitemap):
    changefreq = "weekly"
    priority = 0.8
    protocol = 'https'
    
    def items(self):
        return Blog.objects.all()

    def lastmod(self, obj):
        return obj.updated_at

    def location(self, obj: Blog) -> str:
        return obj.get_absolute_url()

class ServiceSiteMap(Sitemap):
    changefreq = "weekly"
    priority = 1.0
    protocol = 'https'

    def items(self):
        return Service.objects.all()

    def lastmod(self, obj):
        return obj.updated_at

    def location(self, obj: Service) -> str:
        return obj.get_absolute_url()

class DoctorSiteMap(Sitemap):
    changefreq = "weekly"
    priority = 1.0
    protocol = 'https'

    
    def items(self):
        return Doctor.objects.all()

    def lastmod(self, obj):
        return obj.updated_at

    def location(self, obj: Doctor) -> str:
        return obj.get_absolute_url()


class StaticSitemap(Sitemap):
    protocol = 'https'
    priority = 0.9
    changefreq = "monthly"
    i18n = True 

    def items(self):
        return [
            'home', 'about', 'services',
            'contact',  'team',
        ]

    def location(self, item):
        try:
            return reverse(item)
        except NoReverseMatch:
            return reverse('home')

