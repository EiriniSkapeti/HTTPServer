#HTTP server
#print("This is the HTTP server")

import http.server
import socketserver

PORT = 8000


class MyBaseHttpHandler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/index.html":
            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.end_headers()
        else:
            self.send_response(404)
            self.end_headers()
          
with socketserver.TCPServer(("", PORT), MyBaseHttpHandler) as httpd:
    print(f"Serving at port {PORT}")
    httpd.serve_forever()