from django.http import HttpResponseRedirect
from django.urls import reverse
import re


class AuthRequiredMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        # One-time configuration and initialization.

    def __call__(self, request):
        # Code to be executed for each request before
        # the view (and later middleware) are called.

        response = self.get_response(request)
        if request.user.is_authenticated:
            return response

        if re.match(r"(\/a\/){1}", request.path):
            return response

        return HttpResponseRedirect(reverse('login'))
