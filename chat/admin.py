from django.contrib import admin

from .models import Message
from .models import Room

class RatingAdmin(admin.ModelAdmin):
    readonly_fields = ('timestamp',)

admin.site.register(Room,RatingAdmin)
admin.site.register(Message, RatingAdmin)

