import time
from celery import task
from items.models import Item

@task
def add_item(uuid, created_at):
    time.sleep(3)
    item = Item(uuid=uuid, created_at=created_at)
    item.save()
