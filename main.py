import logging
from http.server import HTTPServer, CGIHTTPRequestHandler

HOST, PORT = 'localhost', 5000


def run_server():
    logging.basicConfig(level=logging.INFO)
    httpd = HTTPServer((HOST, PORT), CGIHTTPRequestHandler)
    logging.info('Starting HTTP Server')
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        logging.info('KeyboardInterrupt. Server stopped')


if __name__ == '__main__':
    run_server()
