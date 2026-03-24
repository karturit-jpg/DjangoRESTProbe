from django.http import HttpResponseForbidden

class SubscriptionCheckMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.path.startswith("api/v1/ManipulateOrder/"):
            if not request.user.is_authenticated:
                return HttpResponseForbidden("Login required")
            if not request.user.subscriptions.exists():
                return HttpResponseForbidden("Subscription required")
            response = self.get_response(request)
            return response