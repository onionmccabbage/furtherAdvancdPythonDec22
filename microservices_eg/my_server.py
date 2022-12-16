# microservices is a design pattern where each part of a system is contained within its own module
# each module is callable over http and response with a 'response' data packet
# These microservices can be thought of as APIs
import socket # this is needed for http services

def myServer():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    param_t = ('localhost', 9874) # IP addy and port
    server.bind(param_t) # specify the IP addy and prot for our server
    # begin listening for client connections
    server.listen(6)
    print(f'Server is listening on {param_t[0]}:{param_t[1]}')
    #run the server continuosly
    while True: # careful
        (client, addr) = server.accept() # unpack the request
        buffer = client.recv(1024) # read the first 1024 bytes from the client request
        print(f'Server received {buffer}')
        # respond to the request in some way
        response_text = buffer.upper() # make  the text into upper case
        client.send(response_text)
        if buffer == b'quit': #  we will terminate the server
            server.close()
            break # break out of the while loop


if __name__ == '__main__':
    myServer() # we start the server