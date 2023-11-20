from celery import shared_task

@shared_task
def some_task(param):
    print('I am in the task') 