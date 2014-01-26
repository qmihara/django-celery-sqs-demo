import uuid
from django.http import HttpResponse
from django.utils import timezone
from items.tasks import add_item

def index(request):
    add_item.delay(uuid.uuid4(), timezone.now())
    return HttpResponse('success')
