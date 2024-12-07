# import json
# from channels.generic.websocket import AsyncWebsocketConsumer
# from channels.db import database_sync_to_async
# from .models import Check
# from django.db.models import Q


# class TaskConsumer(AsyncWebsocketConsumer):
#     async def connect(self):
#         self.room_group_name = 'task_group'

#         await self.channel_layer.group_add(
#             self.room_group_name,
#             self.channel_name
#         )

#         await self.accept()


#     async def disconnect(self, close_code):
#         # Удаление из группы при отключении клиента
#         await self.channel_layer.group_discard(
#             'task_group',
#             self.channel_name
#         )


#     async def receive(self, text_data):
#         try:
#             data = json.loads(text_data)
#             telegram_user_id = data.get('user')
#             task_id = data.get('task_id')

#             if telegram_user_id and task_id:
#                 # user = await database_sync_to_async(Check.objects.get)(
#                 #     telegram_user_id=telegram_user_id,
#                 # )

#                 response_data = {
#                     'type': 'send_message',
#                     'action': 'parsing finished',
#                 }

#                 await self.channel_layer.group_send(self.room_group_name, response_data)
#         except json.JSONDecodeError:
#             print("Invalid JSON format")


#     async def send_message(self, res):
#         """ Receive message from room group """
#         await self.send(text_data=json.dumps({
#             "payload": res,
#         }))

import json
from channels.generic.websocket import AsyncWebsocketConsumer

class TaskConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.group_name = "check_notifications"

        # Присоединение к группе
        await self.channel_layer.group_add(
            self.group_name,
            self.channel_name
        )
        await self.accept()

    async def disconnect(self, close_code):
        # Отключение от группы
        await self.channel_layer.group_discard(
            self.group_name,
            self.channel_name
        )

    # Получение сообщения из группы
    async def new_check_message(self, event):
        message = event['message']

        # Отправка сообщения в WebSocket
        await self.send(text_data=message)
