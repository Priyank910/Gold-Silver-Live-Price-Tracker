from django.contrib import admin
from .models import *

# Register your models here.
@admin.register(signup)
class showsignup(admin.ModelAdmin):
  list_display = ["name", "email", "username", "password"]

