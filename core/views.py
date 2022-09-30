from django.http import HttpResponse
from django.template import loader


def home(request):
    template = loader.get_template('site/public_html/index.html')
    context = {
        'random': "meh",
    }
    return HttpResponse(template.render(context, request))


