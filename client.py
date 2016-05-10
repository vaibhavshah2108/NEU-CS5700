#!/usr/bin/env python
import sys
import socket
import ssl

def validation(host, port, ssl_pro):                                            #Return False if any argument is incorrect
    try:
        ip_addr = socket.gethostbyname(host)                                    #Get the IP address of the server from hostname or IP itself
    except socket.gaierror, e:
        print "cannot resolve the hostname :", host, e
        sys.exit()
    if ssl_pro == 1:                                                            #Check for the SSL_connection
        if ip_addr != '129.10.113.143' and port != 27994:
            print 'Invalid hostname and port number \n'
            return (False)                                                      
        elif ip_addr != '129.10.113.143':
            print 'Invalid hostname \n'
            return (False)
        elif port != 27994:
            print 'Invalid port number \n'
            return (False)
        else:
            return (True)                                                       #Return True if all the arguments are correct
    else:                                                                       #Else, Check for the normal_connection
        if ip_addr != '129.10.113.143' and port != 27993:
            print 'Invalid hostname and port number \n'
            return (False)
        elif ip_addr != '129.10.113.143':
            print 'Invalid hostname \n'
            return (False)
        elif port != 27993:
            print 'Invalid port number \n'
            return (False)
        else:
            return (True)                                                       #Return True if all the arguments are correct

def roles(data):
    msg = data.split()
    if len(msg) == 5:
	operator = msg[3]
	a = int(msg[2])
	b = int(msg[4])
    else:
	print 'Invalid number of operational arguments'

    if operator == '+':                                                         #If the operator is '+', then perform addition
        modimsg = str(a + b)
    elif operator == '-':                                                       #If the operator is '-', then perform substraction
        modimsg = str(a - b)
    elif operator == '/':                                                       #If the operator is '/', then perform division
        modimsg = str(a / b)
    elif operator == '*':                                                       #If the operator is '*', then perform multiplication
        modimsg = str(a * b)
    else:                                                                       #else give the invalid operaor
        modimsg = 'invalid operator'
    return (modimsg)

ssl_pro = 0                                                                     #Initialize the value with zero and assume that user don't want to use ssl_protocol
total=len(sys.argv)
# To take the arguments from the user - 
if total == 3:
	host=str(sys.argv[1])
	neuid=str(sys.argv[2])
	port=27993
elif total == 4:
    if sys.argv[1] == '-s':
        port = 27994
        host = str(sys.argv[2])
        neuid= str(sys.argv[3])
        ssl_pro = 1
    else:
	port=int(sys.argv[1])
	host=str(sys.argv[2])
	neuid=str(sys.argv[3])
elif total == 5:
	port=int(sys.argv[1])
	host=str(sys.argv[3])
	neuid=str(sys.argv[4])
	ssl_pro = 1
else:
	print "Invalid number of arguments"

# If the user intend to have SSL connection, run the following 'if' loop -
if ssl_pro == 1:
    valid = validation(host, port, ssl_pro)                                     #calls the validation function to check the entered arguments from the user
    if valid is False:
        sys.exit()                                                              #If validation fails, exit the system
    else:
        s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)                     #else make the socket connection
        ssl_sock = ssl.wrap_socket(s, ssl_version = ssl.PROTOCOL_TLSv1)         #for SSL connection wrap the socket with ssl_socket
        ssl_sock.connect((host, port))                                          #connect server with the secured socket, ssl_sock

        hello= 'cs5700spring2016 HELLO '+str(neuid)+'\n' 
        ssl_sock.send(hello)                                                    #send the Hello message to server
        while True:
                data=ssl_sock.recv(1024)                                        #receive msg from server
                end=data.split( )
                if end[2] == 'BYE':                                             #if it's a BYE message then print message and close the socket
                    print 'Message from server: '+ end[1] +'\n'
                    ssl_sock.close()
                    sys.exit()
                elif not data:                                                  #if no data is coming from the server break the while loop
                    break
                else:                                                           #else pass the data to 'roles' function to solve the mathematical operation
                    call = roles(data)
                    solution = 'cs5700spring2016 ' + call + '\n'
                    ssl_sock.send(solution)
                    continue

        ssl_sock.close()                                                        #close the SSL socket
        sys.exit()                                                              #exit the system
        
# If the user intend to have have normal connection, run the following 'else' loop, with ssl_pro = 0 -
else:
    valid = validation(host, port, ssl_pro)                                     #calls the validation function to check the entered arguments from the user
    if valid is False:
        sys.exit()                                                              #If validation fails, exit the system
    else:
        s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)                     #else make the socket connection
        s.connect((host, port))                                                 #connect server with the normal socket, s
    #print'Connected to the server \n'

        hello= 'cs5700spring2016 HELLO '+str(neuid)+'\n'
        s.send(hello)                                                           #send the Hello message to server
        while True:
            data=s.recv(1024)                                                   #receive msg from server
            # print data
            end=data.split( )
            if end[2] == 'BYE':                                                 #if it's a BYE message then print message and close the socket
                    print 'Message from server: '+ end[1] +'\n'
                    s.close()
                    sys.exit()
            elif not data:
                    break                                                       #if no data is coming from the server break the while loop
            else:                                                               #else pass the data to 'roles' function to solve the mathematical operation
                    call = roles(data)
                    solution = 'cs5700spring2016 ' + call + '\n'
                    s.send(solution)
                    continue
        
        s.close()                                                               #close the socket
        sys.exit()                                                              #exit the system
