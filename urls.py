from datetime import date
from views import Index, Basket, History


# front controller
def secret_front(request):
    request['data'] = date.today()


def other_front(request):
    request['key'] = 'key'


fronts = [secret_front, other_front]

routes = {
    '/': Index(),
    '/basket/': Basket(),
    '/basket/index.html/': Index(),
    '/history/': History(),
}
