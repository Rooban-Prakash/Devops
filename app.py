from http.server import SimpleHTTPRequestHandler, HTTPServer

# Define the server address and port
HOST = '0.0.0.0'  # Listen on all interfaces
PORT = 80  # Port 80 for HTTP

class CustomHTTPRequestHandler(SimpleHTTPRequestHandler):
    # Custom behavior can be added here if needed
    def do_GET(self):
        # Log the request path
        print(f"Received request for: {self.path}")
        super().do_GET()  # Call the parent class's do_GET method

def run(server_class=HTTPServer, handler_class=CustomHTTPRequestHandler):
    server_address = (HOST, PORT)
    httpd = server_class(server_address, handler_class)
    print(f'Serving HTTP on port {PORT}...')
    httpd.serve_forever()

if __name__ == "__main__":
    run()
