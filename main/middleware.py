from django.shortcuts import redirect

class LoginRequiredMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.path == '/login/' and request.session.get('hub_id'):
            return redirect('flights')
        response = self.get_response(request)
        return response
