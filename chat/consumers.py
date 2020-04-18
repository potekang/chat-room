# chat/consumers.py
import json
from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer
from .models import Message, Room
class ChatConsumer(WebsocketConsumer):
    def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = 'chat_%s' % self.room_name

        # Join room group
        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name,
            self.channel_name
        )

        self.accept()

    def disconnect(self, close_code):
        # Leave room group
        async_to_sync(self.channel_layer.group_discard)(
            self.room_group_name,
            self.channel_name
        )

    # Receive message from WebSocket
    def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']
        command = text_data_json['command']
        if command == 'fetch_history':
            hty_messages = Message.last_30_messages(self, Room.objects.get(name=self.room_name))
            for message in hty_messages:
                self.send(text_data=json.dumps(self.message_to_json(message)))
            return
        username = text_data_json['username']
        if(username == None):
            username = "anonymous"
        message = Message.objects.create(
            room=Room.objects.get(name=self.room_name),
            content = message,
            username = username,
            )
        # Send message to room group
        async_to_sync(self.channel_layer.group_send)(
            self.room_group_name,
            {
                'type': 'chat_message',
                'message': self.message_to_json(message)
            }
        )

    def message_to_json(self, message):
        return {
            'room' :message.room.name,
            'message': message.content,
            'username': message.username,
            'timestamp':message.timestamp.strftime('%Y-%m-%d %H:%I:%S')
        }

    # Receive message from room group
    def chat_message(self, event):
        message = event['message']
        # Send message to WebSocket
        self.send(text_data=json.dumps(message))