import socket
import time

# Target host is IP of player you want to be able to join your game
target_host = "1.1.1.1"
target_port = 6112

# create a socket object
client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
client.bind(('0.0.0.0', 6112))

# send some data
while True:
   client.sendto("AAABBBCCC",(target_host, target_port))
   time.sleep(1)
   print "Sent some data"
