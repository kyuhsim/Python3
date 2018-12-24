'''
    UDP Echo server / client
    Client Program
	(using Python 2.7)
	
    History:
    20180720 kyuhsim - created.
'''

import sys
import socket

gPort = 9006


if __name__ == '__main__':
  if ( len(sys.argv) != 3 ):
    print ("- Usage : python {} <target_host_ip> <port>".format( sys.argv[0] ))
    print ("* Exiting...")
  else:
    gHost = sys.argv[1]
    gPort = int( sys.argv[2] )					# to integer
    print ("- UDP Protocol Client : \n")

    #create a UDP socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    socket.setdefaulttimeout(10)       # 10 sec

    server_address = (gHost, gPort )
    message = 'This is the message. It will be repeated.'

    try:
      #send data
      print >> sys.stderr, '- sending: %s' % message
      sent = sock.sendto( message, server_address )

      #receive response
      print >> sys.stderr, '- waiting to receive'
      data, server = sock.recvfrom( 4096 )
      print >> sys.stderr, '- received: %s' % data

    finally:
      print >> sys.stderr, '- closing socket'
      sock.close()


# End of File
