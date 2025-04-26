from django.contrib import admin

# Register your models here.
from .models import ContactFormSubmission, IndexFormSubmission

admin.site.register(ContactFormSubmission)
admin.site.register(IndexFormSubmission)