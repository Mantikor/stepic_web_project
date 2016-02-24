def hello(environ, start_response):
	body = ''
        if environ['REQUEST_METHOD'] == 'GET':
                while part in environ['QUERY_STRING']:
                        body = body+part+'\n'
                status = '200 OK'
                headers = [('Content-Type', 'text/plain')]
                start_response(status, headers )
                return [ body ]
