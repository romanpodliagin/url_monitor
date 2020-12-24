from test_project.celery import app
from url_monitor.models import Url


@app.task(bind=True)
def sync_urls(self):
    for url_obj in Url.objects.all():
        print(f'celery sync {url_obj.id}')
        url_obj.sync()
