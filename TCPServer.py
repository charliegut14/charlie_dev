import socket
import threading

bind_ip = "0.0.0.0"
bind_port = 9999

#Create TCP Socket
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#Bind
server.bind((bind_ip,bind_port))

#Listen
server.listen(5) #Max backlog of connections
print("[*] Listening on %s:%d" % (bind_ip,bind_port))

#Client Handling Thread
def handle_client(client_socket):

    #print what client sends
    request = client_socket.recv(1024)
    print("[*] Receieved: %s" % request)

    msg = "ACK!"
    emsg = msg.encode()
    #send back an ack
    client_socket.send(emsg)

    #Close socket
    client_socket.close()

while True:

    client,addr = server.accept()
    print("[*] Accepted connection from: %s:%d" % (addr[0],addr[1]))

    #create client thread to handle incoming data
    client_handler = threading.Thread(target=handle_client,args=(client,))
    client_handler.start()