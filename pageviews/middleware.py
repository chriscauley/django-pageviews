from .models import HitCount
from django.db.models import F

import urllib2

class PageViewsMiddleware:
    def process_request(self, request, *args, **kwargs):
        try:
            url = urllib2.quote(request.path)
        except KeyError:
            url = "BAD UNICODE DATA"
        hit, hit_created = HitCount.objects.get_or_create(url=url)
        hit.hits = F('hits') + 1
        hit.save()

        return None
