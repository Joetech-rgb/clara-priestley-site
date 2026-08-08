from django.contrib.sitemaps import Sitemap
from django.urls import reverse

from .models import Attorney, BlogPost, PracticeArea


class StaticViewSitemap(Sitemap):
    priority = 0.8
    changefreq = "monthly"

    def items(self):
        return [
            "firm:home",
            "firm:about",
            "firm:team_list",
            "firm:practice_area_list",
            "firm:blog_list",
            "firm:testimonials",
            "firm:contact",
        ]

    def location(self, item):
        return reverse(item)


class PracticeAreaSitemap(Sitemap):
    priority = 0.9
    changefreq = "monthly"

    def items(self):
        return PracticeArea.objects.all()

    def location(self, obj):
        return obj.get_absolute_url()


class AttorneySitemap(Sitemap):
    priority = 0.6
    changefreq = "monthly"

    def items(self):
        return Attorney.objects.all()

    def location(self, obj):
        return obj.get_absolute_url()


class BlogPostSitemap(Sitemap):
    priority = 0.5
    changefreq = "weekly"

    def items(self):
        return BlogPost.objects.all()

    def location(self, obj):
        return obj.get_absolute_url()