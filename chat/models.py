from django.db import models
from django.contrib.auth import get_user_model

class Room(models.Model):
    name = models.CharField(blank=False, max_length = 128, unique = True)
    timestamp = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.name


class Message(models.Model):
    room = models.ForeignKey(Room, related_name='message_room', on_delete=models.CASCADE, default = -1)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.room.name +' @ '+ self.timestamp.strftime('%Y-%m-%d %H:%I:%S') + ': '+self.content

    def last_30_messages(self, room_name):
        return Message.objects.filter(room=room_name).order_by('timestamp').all()[:30]

