# Create your views here.
from django.shortcuts import render
from .models import Room
from django.utils import timezone
def index(request):
    return render(request, 'chat/index.html')
    
def room(request, room_name):
    if Room.objects.filter(name=room_name).exists():
        return render(request, 'chat/room.html', {
            'room_name': room_name
        })
    else:
        rm = Room(name=room_name, timestamp=timezone.now())
        rm.save()
        return render(request, 'chat/room.html', {
            'room_name': room_name
        })
    