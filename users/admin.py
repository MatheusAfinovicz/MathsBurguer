from django.contrib import admin
from .models import UserAdress


class UserAdressAdmin(admin.ModelAdmin):
    list_display = ('user', 'city', 'district', 'street', 'number')
    list_filter = ('user', 'city', 'district',)
    list_per_page = 10
    search_fields = ('user', 'street', 'number', 'district', 'city', 'state', 'complement')


admin.site.register(UserAdress, UserAdressAdmin)
