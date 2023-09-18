from django.contrib import admin
from .models import UserProfile, Customer, Test
# Register your models here.
admin.site.register(UserProfile)
admin.site.register(Customer)
admin.site.register(Test)