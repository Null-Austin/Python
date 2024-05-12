import socket

# Get the hostname of the socket
hostname = socket.gethostname()

# Get the IP address of the hostname
IPAddr = socket.gethostbyname(hostname)

print(IPAddr)