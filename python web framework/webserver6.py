import socket
import mimetypes

class WebServer :

 def run(self, SERVER_PORT) :

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('0.0.0.0', SERVER_PORT))
    server_socket.listen(1)
    print('Listening on port %s ...' % SERVER_PORT)


    while True:    
        client_connection, client_address = server_socket.accept()

        request = client_connection.recv(1024).decode()

        headers = request.split("\n")
        if len(headers[0]) == 0 or 'favicon.ico' in headers[0] :
            content= ("no~~~ ").encode()
        else :
            filename = headers[0].split()[1]    
            try :
                #계산값을 return하는 함수
                content= eval(filename[1:]+"()").encode() 
            except :
                content= ("no~~~ " + filename).encode()

        response = 'HTTP/1.0 200 OK\n\n'.encode()
        client_connection.send(response)
        client_connection.send(content)    
        client_connection.close()    

    server_socket.close()   


def hello() :
    return "<h1>Hello~~~~"

def test() :
    return "<h1>test~~~~</h1>"

app = WebServer()
app.run(8000)