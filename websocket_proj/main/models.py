from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer
import json


class Check(models.Model):
    vulnerability_name = models.CharField(max_length=200)
    vulnerability_dicription = models.TextField(blank=True, null=True)
    date_of_publication = models.DateTimeField()
    link_to_the_source = models.TextField()
    exploits_and_poc = models.TextField(blank=True, null=True)


# Сигнал для отправки сообщения по WebSocket
@receiver(post_save, sender=Check)
def send_new_check_notification(sender, instance, created, **kwargs):
    if created:
        channel_layer = get_channel_layer()
        async_to_sync(channel_layer.group_send)(
            "check_notifications",  # Имя группы WebSocket
            {
                "type": "new_check_message",
                "message": json.dumps({
                    "vulnerability_name": instance.vulnerability_name,
                    "vulnerability_description": instance.vulnerability_dicription,
                    "date_of_publication": instance.date_of_publication.isoformat(),
                    "link_to_the_source": instance.link_to_the_source,
                    "exploits_and_poc": instance.exploits_and_poc,
                }),
            }
        )
