# Import socket module 
import socket             
  
# Create a socket object 
s = socket.socket()         
  
# Define the port on which you want to connect 
port = 12345                
  
# connect to the server on local computer 
s.connect(('127.0.0.1', port)) 

for i in range(100):  
    # receive data from the server 
    s.send(str(i).encode('utf-8'))
    
# close the connection 
s.close()     