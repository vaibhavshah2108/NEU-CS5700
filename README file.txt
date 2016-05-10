
INTRODUCTION
-------------
The project is a client module which consist of simple networking codes which are
used to solve hundreds of simple mathematical expressions, until it receives a 
BYE message with a secret flag from the server.

REQUIREMENTS
-------------
The basic requirements for the program to run are the following modules - 
- Import socket (this module imports the definition of the socket features)
- Import sys (this module defines the system's features)
- Import ssl (this module defines the SSl feature and import features required to
		make secure connection) 

INSTALLATION / EXECUTING
-------------------------
To execute the program type the following command in terminal -
encrypted, 
 $ ./client <-p port> [hostname] [NEU ID]
where
- 'client' is the name of the client file
- '-p port' is the TCP port on which server is listening
- 'hostname' is the name of the server or could be the IP address of the server
- 'NEU ID' is the ID of the client/student.

DETAILS and OUTPUT
-------------------
* The program consist a function 'roles' which basically solves all the mathematical
  operations provided by the server, and further the main program return's it back to 
  the server. 
  - The program runs on the port number - 27993, and
  - The server's hostname is - cs5700sp16.ccs.neu.edu
  - The server could also take the server's IP_address in place of the hostname, 
    which is- '129.10.113.143'

* The client terminates the program as it receives the BYE message from the server
and will print the 64-bits secret flag given by the server.

SUPPORTS / ADDITIONAL FEATURES
-------------------------------
* The client program also supports SSL, which is used to establish a secure connection
  with the server and the transfers the data in encrypted manner.

* To execute the client program with the SSL, run the following command in terminal
  $ ./client <-p port> <-s> [hostname] [NEU ID]
  where,
  - 'client' is the name of the client file
  - '-p port' is 27994 for the secure connection
  - '-s' tells the server that client wants to establish a secure connection. Also 
    it helps the client file to follow the SSl part of the program.
  - 'hostname is cs5700sp16.ccs.neu.edu or '129.10.113.143'
  - 'NEU ID' is the ID of the client/student.

TROBLESHOOTING
---------------
* If the program file doesn't execute in the way as mentioned above, or gives the error
message as: "Permission denied", check the following :
  - Is the client file is executable mode or not. If not, make it executable by:
	- chmod +x client

* If the program file return you with the "Unknown_Husky_ID" in the BYE message,
  re-check the entered NEU_ID or contact the programmer.

* If program returns "Invalid hostname or "Invalid Port Number" re-check the enterd
  values.

* If program returns "cannot resolve the hostname" with error "[Errno -2]", then re-check
the entered hostname.

CONTACT INFORMATION
--------------------
* Programmer 1:
Name:		Sapan Jain
E-mail:		jain.sap@husky.neu.edu
NEU-ID:		001611702
Mob_num:	857-294-7603

* Programmer 2:
Name:		Vaibhav Shah
E-mail:		shah.vaib@husky.neu.edu
NEU-ID:		001714286
Mob_num:	617-382-3897