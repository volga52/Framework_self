# def application(environ, start_response):
#     """
#     :param environ: словарь данных от сервера
#     :param start_response: функция для ответа серверу
#     """
#     print(environ)
#     # сначала в функцию start_response передаем код ответа и заголовки
#     start_response('200 OK', [('Content-Type', 'text/html')])
#     # возвращаем тело ответа в виде списка из bite
#     return [b'Hello world from a simple WSGI application!']


def application(environ, start_response):
    # print(type(environ))
    # print(environ)
    path = environ['PATH_INFO']
    if path == '/':
        start_response('200 OK', [('Content-Type', 'text/html')])
        return [b'Index']
    elif path == '/abc/':
        start_response('200 OK', [('Content-Type', 'text/html')])
        return [b'ABC']
    else:
        start_response('404 NOT FOUND', [('Content-Type', 'text/html')])
        return [b'404 Error']