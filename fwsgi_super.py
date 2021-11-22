from wsgiref.simple_server import make_server


def application(environ, start_response):
    """
    :param environ: словарь данных от сервера
    :param start_response: функция для ответа серверу
    """
    print(environ)
    start_response('200 OK', [('Content-Type', 'text/html')])
    return [b'Hello world from a simple WSGI application!']


with make_server('', 8001, application) as httpd:
    print("Serving on port 8001...")
    httpd.serve_forever()
