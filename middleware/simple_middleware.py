import logging
from django.utils.timezone import now

logger = logging.getLogger(__name__)


class SimpleMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        logger.info(f"Incoming request: {request.path} at {now()}")

        response = self.get_response(request)

        logger.info(f"Outgoing response: {request.path} at {now()}")

        return response