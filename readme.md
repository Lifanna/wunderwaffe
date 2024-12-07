pip install channels channels-redis
pip install daphne

pip install celery[redis]
pip install django-celery-beat

python manage.py migrate django_celery_beat

celery -A your_project beat -l info
