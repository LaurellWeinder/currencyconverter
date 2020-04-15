from http.server import HTTPServer, CGIHTTPRequestHandler

HOST, PORT = 'localhost', 5000
BUFFSIZE = 2096


def run_server():
    cgi_handler = CGIHTTPRequestHandler
    httpd = HTTPServer((HOST, PORT), cgi_handler)
    httpd.serve_forever()
    # with HTTPServer((HOST, PORT), cgi_handler) as httpd:
    #     httpd.serve_forever()
    #     print(cgi_handler.log_date_time_string)

if __name__ == '__main__':
    run_server()
