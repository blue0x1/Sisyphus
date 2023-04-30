<h1 align="center">Sisyphus Reverse Shell<br></h1><br>

<br>
Sisyphus is a simple reverse shell implementation using ZeroMQ for communication between client and server.


### Prerequisites

- Python 3.x
- ZeroMQ library: Install using `pip install pyzmq`


## Example

Client:

```bash 

└─$ python client.py
Enter command: whoami
kali

```
Server:

```bash 
└─$ python server.py
Listening on 0.0.0.0:5001...

```


## Disclaimer:

Sisyphus Reverse shell is intended for educational and testing purposes only. The author is not responsible for any illegal or unauthorized use of this exploit. Use at your own risk.
