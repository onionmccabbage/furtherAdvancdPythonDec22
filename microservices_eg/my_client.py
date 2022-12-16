# a client can make requests to an http server (a microservice)
# a web server is a scaled-up http microservice

import sys
import socket
def myClient():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    param_t = ('localhost', 9874) # IP addy and port
    sock.connect(param_t)
    # we can send data to the server
    message = 'default message'
    # if system argument variables were provided, use them to pass the message
    if len(sys.argv) > 1:
        message = ' '.join(sys.argv[1:]) # join the arguments from 1 onwards, using a space
    sock.send(message.encode()) # we need to encode the message over http
    # is there a response from the server?
    res = sock.recv(1024) # receive the first 1024 bytes
    print(f'Client received {res}')
    sock.close()

if __name__ == '__main__':
    myClient() # here we start our client