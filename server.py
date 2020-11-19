from http.server import HTTPServer, BaseHTTPRequestHandler
from CRUD import work_with_db

class REST(BaseHTTPRequestHandler):

    def _set_headers(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        self.address_string()

    def do_GET(self):
        self._set_headers()
        self.wfile.write(bytes('GET-запрос', 'utf8'))
        print(f'GET запрос от {self.address_string()}')
        work_with_db.select()

    def do_POST(self):
        self._set_headers()
        self.wfile.write(bytes('POST-запрос', 'utf8'))
        print(f'POST-запрос от {self.address_string}')
        work_with_db.insert()

    def do_PUT(self):
        self._set_headers()
        self.wfile.write(bytes('PUT-запрос', 'utf8'))
        print(f'PUT-запрос от {self.address_string}')
        work_with_db.update_name()
        work_with_db.update_text()

    def do_DELETE(self):
        self._set_headers()
        self.wfile.write(bytes('DELETE-запрос', 'utf8'))
        print(f'DELETE-запрос от {self.address_string}')
        work_with_db.delete()


server_address = ('', 9000)
http_connect = HTTPServer(server_address, REST)
http_connect.serve_forever()
