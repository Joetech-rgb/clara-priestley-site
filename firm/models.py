from django.db import models
from django.urls import reverse


class PracticeArea(models.Model):
    name = models.CharField(max_length=120)
    slug = models.SlugField(unique=True)
    summary = models.CharField(max_length=240)
    description = models.TextField()
    icon = models.CharField(
        max_length=40,
        blank=True,
        help_text="Optional short label/emoji used as a visual marker.",
    )
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ["order", "name"]

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("firm:practice_area_detail", kwargs={"slug": self.slug})


class Attorney(models.Model):
    name = models.CharField(max_length=120)
    slug = models.SlugField(unique=True)
    title = models.CharField(max_length=120)
    bio = models.TextField()
    email = models.EmailField(blank=True)
    phone = models.CharField(max_length=40, blank=True)
    photo = models.ImageField(upload_to="attorneys/", blank=True, null=True)
    practice_areas = models.ManyToManyField(PracticeArea, related_name="attorneys", blank=True)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ["order", "name"]
        verbose_name_plural = "attorneys"

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("firm:attorney_detail", kwargs={"slug": self.slug})


class Testimonial(models.Model):
    client_name = models.CharField(max_length=120)
    client_photo = models.ImageField(upload_to="testimonials/", blank=True, null=True)
    quote = models.TextField()
    case_type = models.CharField(max_length=120, blank=True)
    is_featured = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.client_name} — {self.case_type or 'General'}"


class BlogPost(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    excerpt = models.CharField(max_length=300)
    body = models.TextField()
    practice_area = models.ForeignKey(
        PracticeArea, on_delete=models.SET_NULL, null=True, blank=True, related_name="posts"
    )
    published_at = models.DateTimeField()
    is_published = models.BooleanField(default=True)

    class Meta:
        ordering = ["-published_at"]

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("firm:blog_detail", kwargs={"slug": self.slug})


class ContactInquiry(models.Model):
    STATUS_NEW = "new"
    STATUS_CONTACTED = "contacted"
    STATUS_CLOSED = "closed"
    STATUS_CHOICES = [
        (STATUS_NEW, "New"),
        (STATUS_CONTACTED, "Contacted"),
        (STATUS_CLOSED, "Closed"),
    ]

    name = models.CharField(max_length=120)
    email = models.EmailField()
    phone = models.CharField(max_length=40, blank=True)
    practice_area = models.ForeignKey(
        PracticeArea, on_delete=models.SET_NULL, null=True, blank=True, related_name="inquiries"
    )
    message = models.TextField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default=STATUS_NEW)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return f"{self.name} ({self.created_at:%Y-%m-%d})"
