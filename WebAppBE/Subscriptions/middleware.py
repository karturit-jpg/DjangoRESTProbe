from django.http import HttpResponseForbidden


class SubscriptionCheckMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.path.startswith("api/v1/ManipulateOrder/"):
            if not request.user.is_authenticated:
                return HttpResponseForbidden("Login required") # почти убежден, что, учитывая что view определен кастомным классом фреймворка, этот фрагмент избыточен; однако, это наводит на интересную мысль о том, как рождаются нестыковки и непоследовательность на пересечении различных бизнес осей реализуемых в коде
            if not request.user.subscriptions.exists() or not request.user.subscriptions.first().is_active: # а теперь решил паписать единую строку валидации с двумя субусловиями; интересно здесь то, что в первом применение метода возвращает bool, а во втором--конвенция: сам пишу в занчения только bool'ы, но superficially работаю с обьектами одного типа, отсюда субусловия так легко комбинируются
                return HttpResponseForbidden("Active subscription required")
            response = self.get_response(request)
            return response