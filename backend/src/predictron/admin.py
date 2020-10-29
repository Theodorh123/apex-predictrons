from django.contrib import admin
from .models import User

# Register your models here.

class UserAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'email', 'address', 'phone_number', 'sex', 'date_of_birth', 'occupation']

admin.site.register(User, UserAdmin)
