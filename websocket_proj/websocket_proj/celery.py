# from __future__ import absolute_import, unicode_literals
# import os
# from celery import Celery
# from celery.schedules import crontab
# from datetime import timedelta

# # set the default Django settings module for the 'celery' program.
# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')

# app = Celery('core')

# # Using a string here means the worker doesn't have to serialize
# # the configuration object to child processes.
# # - namespace='CELERY' means all celery-related config keys should have a `CELERY_` prefix.
# app.config_from_object('django.conf:settings', namespace='CELERY')

# # Load task modules from all registered Django app configs.
# app.autodiscover_tasks()


# app.conf.beat_schedule = {
#     'update-cleaning-status-every-minute': {
#         'task': 'web.tasks.add',
#         # 'schedule': crontab(minute='*/1'),  # Каждую минуту
#         'schedule': timedelta(seconds=5),  # Каждую минуту
#     },
# }

# my_project/celery.py
from __future__ import absolute_import, unicode_literals
import os
from celery import Celery

# Указываем Django настройки
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'websocket_proj.settings')

app = Celery('websocket_proj')

# Загружаем конфигурацию из settings.py с префиксом CELERY_
app.config_from_object('django.conf:settings', namespace='CELERY')

# Автоматически обнаруживаем задачи в приложениях Django
app.autodiscover_tasks()

@app.task(bind=True)
def debug_task():
    print('Request: asdasdasd')
