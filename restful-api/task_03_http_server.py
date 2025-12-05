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

    def do_GET(self):
        # Sending HTTP response status code
        self.send_response(200)

        # Sending Headers
        self.send_header("Content-type", "text/html")
        self.end_headers()

        # Writing response body
        self.wfile.write(b"Hello, this is a simple API!")

        return


def run(server_class=http.server.HTTPServer, handler_class=SimpleAPIHandler):
    server_address = ('', 8000)
    httpd = server_class(server_address, handler_class)
    httpd.serve_forever()


if __name__ == '__main__':
    run()
