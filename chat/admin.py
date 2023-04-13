from django.contrib import admin

from .models import Thread, Message


@admin.register(Thread)
class ThreadAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'created', 'updated')
    ordering = ('updated', 'created')


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ("sender", "text", "thread", "created", "is_read")
    ordering = ('created', 'sender', 'is_read')
    search_fields = ("text", )
