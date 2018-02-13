from django.contrib import admin
from .models import Paper, User, PaperUser
# Register your models here.


@admin.register(Paper)
class PaperAdmin(admin.ModelAdmin):
    list_display = ('url', 'stance', 'title', 'body', 'referrer')
    pass


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    pass


@admin.register(PaperUser)
class PaperUserAdmin(admin.ModelAdmin):
    list_display = ('url', 'referrer', 'referree')
    pass
