from django.conf import settings
from django.contrib import messages
from django.core.mail import send_mail
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse

from .forms import ContactInquiryForm
from .models import Attorney, BlogPost, PracticeArea, Testimonial


def home(request):
    context = {
        "practice_areas": PracticeArea.objects.all()[:6],
        "attorneys": Attorney.objects.all()[:3],
        "testimonials": Testimonial.objects.filter(is_featured=True)[:3],
        "posts": BlogPost.objects.filter(is_published=True)[:3],
    }
    return render(request, "firm/home.html", context)


def about(request):
    return render(request, "firm/about.html", {"attorneys": Attorney.objects.all()[:3]})


def team_list(request):
    return render(request, "firm/team_list.html", {"attorneys": Attorney.objects.all()})


def attorney_detail(request, slug):
    attorney = get_object_or_404(Attorney, slug=slug)
    return render(request, "firm/attorney_detail.html", {"attorney": attorney})


def practice_area_list(request):
    return render(request, "firm/practice_area_list.html", {"practice_areas": PracticeArea.objects.all()})


def practice_area_detail(request, slug):
    practice_area = get_object_or_404(PracticeArea, slug=slug)
    return render(request, "firm/practice_area_detail.html", {"practice_area": practice_area})


def blog_list(request):
    posts = BlogPost.objects.filter(is_published=True)
    return render(request, "firm/blog_list.html", {"posts": posts})


def blog_detail(request, slug):
    post = get_object_or_404(BlogPost, slug=slug, is_published=True)
    return render(request, "firm/blog_detail.html", {"post": post})


def testimonials(request):
    return render(request, "firm/testimonials.html", {"testimonials": Testimonial.objects.all()})


def contact(request):
    if request.method == "POST":
        form = ContactInquiryForm(request.POST)
        if form.is_valid():
            inquiry = form.save()
            send_mail(
                subject="We've received your enquiry - Clara Priestley LLP",
                message=(
                    f"Hi {inquiry.name},\n\n"
                    "Thank you for reaching out to Clara Priestley LLP. "
                    "We've received your enquiry and a member of our team will be in touch shortly.\n\n"
                    "Your message:\n"
                    f"{inquiry.message}\n\n"
                    "Clara Priestley LLP"
                ),
                from_email=None,
                recipient_list=[inquiry.email],
                fail_silently=False,
            )

            send_mail(
                subject=f"New website enquiry from {inquiry.name}",
                message=(
                    f"New contact form submission received.\n\n"
                    f"Name: {inquiry.name}\n"
                    f"Email: {inquiry.email}\n"
                    f"Phone: {getattr(inquiry, 'phone', '') or 'Not provided'}\n"
                    f"Practice Area: {getattr(inquiry, 'practice_area', '') or 'Not specified'}\n\n"
                    f"Message:\n{inquiry.message}\n"
                ),
                from_email=None,
                recipient_list=[settings.FIRM_NOTIFICATION_EMAIL],
                fail_silently=False,
            )

            messages.success(request, "Thanks - your enquiry has been received. Check your email for confirmation.")
            return redirect(reverse("firm:contact"))
    else:
        form = ContactInquiryForm()
    return render(request, "firm/contact.html", {"form": form})


def robots_txt(request):
    from django.http import HttpResponse
    lines = [
        "User-agent: *",
        "Allow: /",
        "Sitemap: https://clarapriestley.com/sitemap.xml",
    ]
    return HttpResponse("\n".join(lines), content_type="text/plain")