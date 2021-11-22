from framework.templator import render


class Index:
    def __call__(self, request):
        return '200 OK', render('index.html', data=request.get('data', None))


class Basket:
    def __call__(self, request):
        return '200 OK', render('basket.html', data=request.get('data', None))


class NotFound404:
    def __call__(self, request):
        return '404 WHAT', '404 PAGE Not Found'
