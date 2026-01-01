from django.contrib import admin
from about.models import About, CollaborateRequest
from django_summernote.admin import SummernoteModelAdmin

# Register your models here.


@admin.register(About)
class AboutAdmin(SummernoteModelAdmin):
    """
    Adds rich-text editing of content in admin panel.
    """
    summernote_fields = ('content',)

@admin.register(CollaborateRequest)
class CollabourateRequestAdmin(admin.ModelAdmin):
    """
    Lists message and read fields for display in admin panel.
    """

    list_display = ('message', 'read',)
