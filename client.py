import zmq
import subprocess

host = '192.168.8.107'
port = 5001

context = zmq.Context()
socket = context.socket(zmq.REQ)
socket.connect(f"tcp://{host}:{port}")

while True:
    command = input("Enter command: ")
    socket.send_string(command)
    output = socket.recv_string()
    print(output)
