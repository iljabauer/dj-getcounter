from django.conf import settings
from getcounter import models


class GetCounterMiddleware(object):
    def process_request(self, request):
        parameters = settings.GET_COUNTER_PARAMETERS
        if not parameters:
            return

        for parameter in parameters:
            if parameter not in request.GET:
                continue

            models.GetCounter(parameter=parameter).save()
