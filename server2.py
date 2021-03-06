import socket
import threading
import RPi.GPIO as gpio

gpio.setwarnings(False)
gpio.setmode(gpio.BCM)
gpio.setup(1,gpio.OUT)



HEADER = 64
# Choose a port
PORT = 5051
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
            
            if (msg == 'on'):
                gpio.output(1, gpio.HIGH)

            if (msg == 'off'):
                gpio.output(1, gpio.LOW)

            if (msg == "!DISCONNECT"):
                connected = False

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

start()
