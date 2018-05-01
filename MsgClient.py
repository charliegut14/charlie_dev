#!/usr/bin/env python3

from socket import AF_INET, socket, SOCK_STREAM
from threading import Thread
import tkinter

def receive():
    #Handles incoming messages
    while True:
        try:
            msg = client_socket.recv(BUFSIZ).decode("utf8")
            msg_list.insert(tkinter.END, msg)
        except OSError: #Possibly client has left the chat
            break

def send(event=None): #Event is passsed by binders
    #handles outgoing messages
    msg = my_msg.get()
    my_msg.set("") #Clears input field
    client_socket.send(bytes(msg, "utf8"))
    if msg == "{quit}":
        client_socket.close()
        top.quit()

def on_closing(event=None):
    #disconnects when the gui window is closed
    my_msg.set("{quit}")
    send()

top = tkinter.Tk()
top.title("Chatter")

messages_frame = tkinter.Frame(top)
my_msg = tkinter.StringVar() # For messages to be send
my_msg.set("Type your messages here.")
scrollbar = tkinter.Scrollbar(messages_frame) # To navigate through past messages

msg_list = tkinter.Listbox(messages_frame, height=15, width=50, yscrollcommand=scrollbar.set)
scrollbar.pack(side=tkinter.RIGHT, fill=tkinter.Y)
msg_list.pack(side=tkinter.LEFT, fill=tkinter.BOTH)
msg_list.pack()

messages_frame.pack()
entry_field = tkinter.Entry(top, textvariable=my_msg)
entry_field.bind("<Return>", send)
entry_field.pack()
send_button = tkinter.Button(top, text="Send", command=send)
send_button.pack()

top.protocol("WM_DELETE_WINDOW", on_closing)

HOST = input('Enter host: ')
PORT = input('Enter port: ')

if not PORT:
    PORT = 33000 #Default Value
else:
    PORT = int(PORT)

BUFSIZ = 1024
ADDR = (HOST, PORT)
client_socket = socket(AF_INET, SOCK_STREAM)
client_socket.connect(ADDR)

receive_thread = Thread(target=receive)
receive_thread.start()
tkinter.mainloop() #Starts GUI execution

