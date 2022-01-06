import os

from celery import Celery

# Set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')

app = Celery('project')

# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
app.config_from_object('django.conf:settings', namespace='CELERY')

# Load task modules from all registered Django apps.
app.autodiscover_tasks()


@app.task(bind=True)
def debug_task(self):
    print(f'Request: {self.request!r}')

# celery beat settings


from celery.schedules import crontab

'''
app.conf.beat_schedule = {
    'task-name(give any name)': {
        'task': 'app_name.tasks(tasks.py).function_name',# need to specify the path of the file and function
        'schedule': crontab(hour=8,minute=0),
        #'args': (data)# we cn pass some data to the function

}
'''

app.conf.beat_schedule = {
    'testing': {
        'task': 'home_application.task.cal',
        'schedule': crontab(hour=14,minute=29),
    }
}