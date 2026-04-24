import json
from channels.generic.websocket import AsyncWebsocketConsumer
from channels.db import database_sync_to_async
from .models import Message
from accounts.models import User

class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.other_user_id = int(self.scope['url_route']['kwargs']['user_id'])
        
        # Verify user is authenticated
        if not self.scope['user'].is_authenticated:
            await self.close()
            return
            
        self.user_id = self.scope['user'].id

        # Deterministic group name based on both user IDs
        min_id = min(self.user_id, self.other_user_id)
        max_id = max(self.user_id, self.other_user_id)
        self.room_group_name = f'chat_{min_id}_{max_id}'

        # Join room group
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )

        await self.accept()

    async def disconnect(self, close_code):
        if hasattr(self, 'room_group_name'):
            # Leave room group
            await self.channel_layer.group_discard(
                self.room_group_name,
                self.channel_name
            )

    # Receive message from WebSocket
    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']
        
        if not self.scope['user'].is_authenticated:
            return

        sender_id = self.scope['user'].id

        # Save message to database
        saved_message = await self.save_message(sender_id, self.other_user_id, message)

        # Send message to room group
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'chat_message',
                'message': message,
                'sender': self.scope['user'].username,
                'sender_id': sender_id,
            }
        )

    # Receive message from room group
    async def chat_message(self, event):
        message = event['message']
        sender = event['sender']
        sender_id = event['sender_id']

        # Send message to WebSocket
        await self.send(text_data=json.dumps({
            'message': message,
            'sender': sender,
            'sender_id': sender_id
        }))

    @database_sync_to_async
    def save_message(self, sender_id, receiver_id, text):
        return Message.objects.create(sender_id=sender_id, receiver_id=receiver_id, text=text)
