from cgi import parse_qs

def app(environ, start_response):
	body = ''
        if environ['REQUEST_METHOD'] == 'GET':
                a = parse_qs(environ['QUERY_STRING'])
                print(a)
                for key, value in a.items():
                	body = body + key + '+'	+ value + '\n'
                print(body)
                status = '200 OK'
                headers = [('Content-Type', 'text/plain')]
                start_response(status, headers )
                return [ body ]
