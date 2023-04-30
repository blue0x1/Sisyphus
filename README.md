<h1 align="center">Sisyphus Reverse Shell<br></h1><br>


<br>
<p align="center">
  <img src="https://user-images.githubusercontent.com/52697989/235373672-730ee3ab-6079-4147-a95f-319db2ed41fc.png" alt="Screenshot">
</p>

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
