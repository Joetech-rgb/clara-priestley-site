from django import forms

from .models import ContactInquiry


class ContactInquiryForm(forms.ModelForm):
    class Meta:
        model = ContactInquiry
        fields = ["name", "email", "phone", "practice_area", "message"]
        widgets = {
            "name": forms.TextInput(attrs={"placeholder": "e.g. Sarah Mensah"}),
            "email": forms.EmailInput(attrs={"placeholder": "you@yourcompany.com"}),
            "phone": forms.TextInput(attrs={"placeholder": "e.g. +233 24 000 0000"}),
            "message": forms.Textarea(attrs={"rows": 5, "placeholder": "Tell us a little about your situation and what kind of help you're looking for..."}),
        }