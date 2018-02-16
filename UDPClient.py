import socket

target_host = "127.0.0.1"
target_port = 80

#create a socket object
client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

msg = input("Enter Data: ")

#encode message
emsg = msg.encode()


#send data
client.sendto(emsg, (target_host,target_port))

#recieve data
data, addr = client.recvfrom(4096)

print(data)
