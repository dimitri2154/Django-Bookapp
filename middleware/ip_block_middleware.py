from django.core.exceptions import PermissionDenied
from django.conf import settings

class IpBlockMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        ip_address = request.META.get('REMOTE_ADDR')
        if ip_address in settings.BLOCKED_IPS:
            raise PermissionDenied

        response = self.get_response(request)
        return response