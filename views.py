from framework.templator import render


class Index:
    def __call__(self, request):
        return '200 OK', render('index.html', request=request)


class Basket:
    def __call__(self, request):
        return '200 OK', render('basket.html', request=request)


class History:
    def __call__(self, request):
        return '200 OK', render('history.html', request=request)


class NotFound404:
    def __call__(self, request):
        return '404 WHAT', '404 PAGE Not Found'
