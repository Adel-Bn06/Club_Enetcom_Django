from django.contrib import admin
from django.contrib.auth.models import User
from .models import *
# Register your models here.
admin.site.register(Etudianti)
admin.site.register(PresidentClubi)
admin.site.register(Clubi)
admin.site.register(MembreClubi)


@admin.register(Messages)
class MessageAdmin(admin.ModelAdmin):
    list_display = ('sender', 'recipient', 'timestamp')
    search_fields = ('sender__username', 'recipient__username', 'timestamp')