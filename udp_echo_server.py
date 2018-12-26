'''
    UDP Echo server / client
    Server Program : running on controller_board
	(using Python 2.7 -> 3.5)

    History:
    20180720 kyuhsim - created.
    20181226 kyuhsim - change printf to fit with python 3.
'''

import sys
import socket

gPort = 9006


if __name__ == '__main__':
  if ( len(sys.argv) != 2 ):
    print ("- Usage : python {} <port>".format( sys.argv[0] ))
    print ("* Exiting...")
  else:
    gPort = int( sys.argv[1] )			# to integer
    print ("- UDP Protocol Server : \n")

    #create a UDP socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    #bind the socket to the port
    server_address = ('localhost', gPort )
#    print >> sys.stderr, '- Starting server on %s port %s' % (server_address, gPort)
    print("- Starting server on ", server_address, " port ", gPort, end='\n', file=sys.stderr, flush=False)
    sock.bind( server_address )

    while True:
#      print >> sys.stderr, '\n- Waiting to receive message'
      print("\n- Waiting to receive message", end='\n', file=sys.stderr, flush=False)
      data, address = sock.recvfrom( 4096 )

#      print >> sys.stderr, '- received %d bytes from %s : ' % (len(data), address)
      print("- received ", len(data), " bytes from ", address, end='\n', file=sys.stderr, flush=False)
#      print >> sys.stderr, data
      print(data, end='\n', file=sys.stderr, flush=False)

      if data:
        sent = sock.sendto( data, address )
#        print >> sys.stderr, '- sent %d bytes back to %s' % (sent, address)
        print("- sent ", sent, " bytes back to ", address, end='\n', file=sys.stderr, flush=False)


#  print >> sys.stderr, '- Program %s exited normally' % sys.argv[0]
  print("- Program ", sys.argv[0], " exited normally", end='\n', file=sys.stderr, flush=True)

# End of File
