import socket
import threading

import subprocess
import sys

from functions import handler


# --- OpenCV Detection process ---
subprocess.Popen([sys.executable,"./Object_detection_picamera.py"], cwd="./tensorflow1/models/research/object_detection")



HEADER = 64
# Choose a port
PORT = 5050
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "!DISCONNECT"

SERVER = ''

ADDR = (SERVER, PORT)
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server.bind((SERVER, PORT))

def handle_client(conn, addr):
    #print(f"[NEW CONNECTION] {addr} connected.")

    connected = True
    while connected:
        msg_length = conn.recv(HEADER).decode("utf-8")

        if msg_length:
            msg_length = int(msg_length)

            msg = conn.recv(msg_length).decode(FORMAT)

            if (msg == "!DISCONNECT"):
                connected = False
           
            # Run the functions.handler function
            handler.handle(msg)
            #print(f"[{addr}] {msg}")
            conn.send("Msg Recv!".encode(FORMAT))
    
    return msg
    conn.close()

def start():

    #print("[Starting] server is starting")
    server.listen()

    #print(f"[SERVER HAS STARTED] Listening on {SERVER}")

    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target=handle_client,args=(conn, addr))

        thread.start()
        #print(f"[ACTIVE CONNECTIONS] {threading.activeCount() - 1}")

if __name__ == "__main__":
    start()
