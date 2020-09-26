from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth import get_user_model
from .models import Profile
from webapp.models import Review, Product


class ProfileInline(admin.StackedInline):
    model = Profile
    exclude = []


class ProfileAdmin(UserAdmin):
    inlines = [ProfileInline]


User = get_user_model()
admin.site.unregister(User)

admin.site.register(User, ProfileAdmin)
admin.site.register(Review)
admin.site.register(Product)


