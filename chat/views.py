# Create your views here.
from django.shortcuts import render
from .models import Room
from django.utils import timezone
from django.utils.safestring import mark_safe
import json
def index(request):
    return render(request, 'chat/index.html')
    
def room(request, room_name, username = "anonymous"):
    roomName = mark_safe(json.dumps(room_name))
    username = mark_safe(json.dumps(username))
    if Room.objects.filter(name=room_name).exists():
        return render(request, 'chat/room.html', {
            'room_name': room_name,
            'username': username,
        })
    else:
        rm = Room(name=room_name, timestamp=timezone.now())
        rm.save()
        return render(request, 'chat/room.html', {
            'room_name': room_name,
            'username': username,
        })
    