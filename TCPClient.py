import socket # for sockets
import sys # for exit

#Create a socket AF_INET = IPV4 STEAM SOCKET = TCP

try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
except socket.error as msg:
    print("Failed to create socket. Error code: " + str(msg[0]) + " , Error message : " + msg[1])
    sys.exit();


print("Socket Created")


#Test
host = input("Input FQDN of host: ")
port = int(input("Enter destination port: "))

try:
    remote_ip = socket.gethostbyname(host)

except socket.gaierror:
    # could not resolve
    print("Hostname could not be resolved. Exiting")
    sys.exit()

print("Ip address of " + host + " is " + remote_ip)

# Connect to remote server
s.connect((remote_ip, port))
print("Socket Connected to " + host + " on ip " + remote_ip)

#Send data to server

message = input("Enter data to send: ")
#message = "GET / HTTP/1.1\r\n\r\n"
#convert string to bytes
emsg = message.encode()

try:
    #set the whole string
    s.sendall(emsg)
except socket.error:
    #send failed
    print("Send Failed")
    sys.exit()

print("Message sent successfully")

#recieve data
reply = s.recv(4096)
print(reply)

#close socket
s.close()
print("Socket closed")