from django.contrib import admin
from user.models import User


class UserAdmin(admin.ModelAdmin):

    list_display=['email', 'is_active', 'is_staff']

    list_display_links = ['email','is_active']

    readonly_fields = ['email','password']

    list_filter = ['email', 'is_staff']


admin.site.register(User,UserAdmin)

# Register your models here.
