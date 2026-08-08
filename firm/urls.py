from django.urls import path

from . import views

app_name = "firm"

urlpatterns = [
    path("", views.home, name="home"),
    path("about/", views.about, name="about"),
    path("team/", views.team_list, name="team_list"),
    path("team/<slug:slug>/", views.attorney_detail, name="attorney_detail"),
    path("practice-areas/", views.practice_area_list, name="practice_area_list"),
    path("practice-areas/<slug:slug>/", views.practice_area_detail, name="practice_area_detail"),
    path("blog/", views.blog_list, name="blog_list"),
    path("blog/<slug:slug>/", views.blog_detail, name="blog_detail"),
    path("testimonials/", views.testimonials, name="testimonials"),
    path("contact/", views.contact, name="contact"),
]