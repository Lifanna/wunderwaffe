# from celery import shared_task
# from django.utils.timezone import now
# from web.models import Cleaning_room  # Замените на путь к вашей модели
# from time import sleep


# @shared_task
# def update_cleaning_status():
#     pass
#     # current_time = now()  # Текущее время

#     # # Ищем уборки, которые завершены по времени, но имеют статус "в процессе"
#     # cleaning_rooms = Cleaning_room.objects.filter(
#     #     end_datetime__lte=current_time,
#     #     status='in_progress'  # Статус "в процессе"
#     # )

#     # # Обновляем их статус на "завершено"
#     # updated_count = cleaning_rooms.update(status='completed')

#     # return f'{updated_count} уборок было обновлено на "завершено"'

# @shared_task
# def add():
#     # sleep(5)  # Имитируем задержку
#     print("QWEQWEQWEWQEQWEWQE: ")
#     return 1

from celery import shared_task

@shared_task
def periodic_task():
    print("This task runs every 5 secondsssssss.")
