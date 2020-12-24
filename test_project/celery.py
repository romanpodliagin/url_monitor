import os
from celery import Celery
from celery.schedules import crontab

# set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'test_project.settings')

app = Celery('test_project')
app.conf.broker_url = 'redis://romaan:DUQVa8L3JZ7X6nOyuVON8PybHmRfj@localhost:6379/0'

# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
app.config_from_object('django.conf:settings', namespace='CELERY')

# Load task modules from all registered Django app configs.
app.autodiscover_tasks()


@app.task(bind=True)
def debug_task(self):
    print(f'Request: {self.request!r}')


app.conf.beat_schedule = {
    'sync_urls': {
        'task': 'url_monitor.tasks.sync_urls',
        'schedule': crontab(minute='*', hour='*')
    }
}
app.conf.timezone = 'UTC'