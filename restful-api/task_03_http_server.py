#!/usr/bin/python3
"""
Simple API Handler
"""


import http.server
import json


class SimpleAPIHandler(http.server.BaseHTTPRequestHandler):
    """
    Custom API Handler
    """

    def _send_headers(self, status_code=200, content_type='text/plain'):
        # Sending HTTP response status code
        self.send_response(status_code)

        # Sending Headers
        self.send_header("Content-type", content_type)
        self.end_headers()

    def do_GET(self):
        if self.path == '/':
            self._send_headers()
            self.wfile.write(b"Hello, this is a simple API!")
            return

        elif self.path == '/data':
            data = {"name": "John", "age": 30, "city": "New York"}
            json_data = json.dumps(data).encode()

            self._send_headers(200, 'application/json')
            self.wfile.write(json_data)
            return

        elif self.path == '/status':
            self._send_headers()
            self.wfile.write(b"OK")

        else:
            self._send_headers(404)
            self.wfile.write(b"Endpoint not found")


def run(server_class=http.server.HTTPServer, handler_class=SimpleAPIHandler):
    server_address = ('', 8000)
    httpd = server_class(server_address, handler_class)
    httpd.serve_forever()


if __name__ == '__main__':
    run()
