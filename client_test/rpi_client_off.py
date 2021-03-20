import socket

HEADER = 64
# Choose a port
PORT = 5051
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "!DISCONNECT"
# Check your ip address using ifconfig/ipconfig/ip addr
SERVER = "192.168.1.149"
ADDR = (SERVER, PORT)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)

def send(msg):
    message = msg.encode('utf-8')
    msg_length = len(message)

    send_length = str(msg_length).encode(FORMAT)
    send_length += b' ' * (HEADER - len(send_length))

    client.send(send_length)
    client.send(message)
    print(client.recv(2048).decode(FORMAT))

send("LED OFF")
send(DISCONNECT_MESSAGE)

