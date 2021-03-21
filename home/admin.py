from django.contrib import admin
from .models import MessageBox


class MessageBoxAdmin(admin.ModelAdmin):
    list_display = ('date', 'first_name', 'email', 'message')
    list_filter = ('first_name', 'date')
    list_per_page = 5
    search_fields = ('first_name', 'last_name', 'email', 'date', 'message')


admin.site.register(MessageBox, MessageBoxAdmin)
