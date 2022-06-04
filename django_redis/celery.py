from __future__ import absolute_import, unicode_literals
from celery import Celery
from django.conf import settings
from celery.schedules import crontab
import os


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_redis.settings')

app = Celery('django_redis')

app.config_from_object('django.conf:settings', namespace='CELERY')

app.conf.beat_schedule = {
    'dummy': {
        'task': 'url_shortener.tasks.dummy',
        'schedule': crontab(minute="*")
    }
}

app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)

@app.task(bind=True)
def debug_task(self):
    print('Request: {0!r}'.format(self.request))
