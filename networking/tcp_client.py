import socket

host = 'www.google.com'
port = 80

# creating a socket object
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# connect the client
client.connect((host,port))
# sent some data
client.send(bytes('GET / HTTP/1.1\r\nHost: google.com\r\n\r\n', 'utf-8'))
# receive some data back
response = client.recv(4096)
print(response)
