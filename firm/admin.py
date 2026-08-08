from django.contrib import admin

from .models import Attorney, BlogPost, ContactInquiry, PracticeArea, Testimonial


@admin.register(PracticeArea)
class PracticeAreaAdmin(admin.ModelAdmin):
    list_display = ("name", "slug", "order")
    prepopulated_fields = {"slug": ("name",)}
    ordering = ("order", "name")


@admin.register(Attorney)
class AttorneyAdmin(admin.ModelAdmin):
    list_display = ("name", "title", "order")
    prepopulated_fields = {"slug": ("name",)}
    filter_horizontal = ("practice_areas",)
    ordering = ("order", "name")


@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    list_display = ("client_name", "case_type", "is_featured")
    list_filter = ("is_featured",)


@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    list_display = ("title", "practice_area", "published_at", "is_published")
    list_filter = ("is_published", "practice_area")
    prepopulated_fields = {"slug": ("title",)}
    search_fields = ("title", "excerpt", "body")


@admin.register(ContactInquiry)
class ContactInquiryAdmin(admin.ModelAdmin):
    list_display = ("name", "email", "practice_area", "status", "created_at")
    list_filter = ("status", "practice_area")
    search_fields = ("name", "email", "message")
    readonly_fields = ("created_at",)