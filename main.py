__author__ = 'adm'

import socket

socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket.bind(('', 80))
socket.listen(1)
connection, _ = socket.accept()
while True:
    connection.sendall(connection.recv(1024))
    connection.sendall("""HTTP/1.1 200 OK
    Content-type: text/html
    <html>
        <body>
            <h1>Hello!</h1>
        </body>
    </html>""")
