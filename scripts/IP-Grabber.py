import socket

# Get the hostname of the socket
hostname = socket.gethostname()

# Get the IP address of the hostname
IPAddr = socket.gethostbyname(hostname)

print(IPAddr)

#i believe this is just local ip... or 127.0.0.1