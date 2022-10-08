import json
import random

from django.http import HttpResponse
from django.template import loader

from portfolio.settings import STATIC_URL


def home(request):
    template = loader.get_template('site/public_html/index.html')
    context = {
        'random': "meh",
    }
    return HttpResponse(template.render(context, request))


def live_map(request):
    template = loader.get_template('site/map/live_map.html')
    context = {
        'STATIC_URL': STATIC_URL,
    }
    return HttpResponse(template.render(context, request))


def map_data(request):
    return HttpResponse(status=200, content=json.dumps([{
        "loc": {
            "lat": random.uniform(-80, 80),
            "lng": random.uniform(-170, 170)
        },
        "delay_after": random.randint(500, 1500),
    }]))
