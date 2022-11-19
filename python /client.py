# Computer client side
import socket
import time

PORT = 55555
HOST = "0.0.0.0"
IP = ""


def get_axis():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((IP, PORT))
        s.sendall(b"Hello, world")
        data = s.recv(2048)
        time.sleep(0.5)
        s.close()
    return data