#!/usr/bin/python

import sys
from mininet.net import Mininet
from mininet.node import Controller
from mininet.cli import CLI
from mininet.log import setLogLevel, info
from mininet.link import TCLink

def emptyNet():

    "Create an empty network and add nodes to it."

    net = Mininet( controller=Controller )

    info( '*** Adding controller\n' )
    net.addController( 'c0' )
    hosts = []
    
    info( '*** Adding hosts\n' )
    host_base = "h"
    h_count = 1
    while h_count <= x*y:
        if h_count%2 == 0:
            hosts.append(net.addHost('h'+str(h_count), ip = '10.0.0.'+str(h_count)))
        else:
            hosts.append(net.addHost('h' + str(h_count), ip = '11.0.0.' + str(h_count)))
        #info('h_count: ', h_count)
        h_count = h_count + 1
            
    info('created: ', h_count , 'hosts') 
    info( '*** Adding switch\n' )
    switchs = []
    s_count = 0 
    while s_count < y:
        switchs.append(net.addSwitch('s'+str(s_count)))
        #info('s_count: ', s_count)
        s_count = s_count + 1
    
    info( '*** Creating links\n' )
    l_count = 0
    h_c = 0 
    while l_count < x:
        for i in range(0, y):
            info('\n Adding New Link: ')
	    o = net.addLink(hosts[h_c], switchs[l_count], cls = TCLink)
            if i%2 == 0:
                o.intf1.config( bw = 2)
            else:
                o.intf1.config( bw=1 )
            h_c = h_c + 1    
	    info('h_c: ', h_c)	
    	l_count  = l_count + 1 
    
    l_count = 0
    while l_count < y-1:
        net.addLink(switchs[l_count],switchs[l_count+1])
        l_count = l_count + 1

    info( '*** Starting network\n')
    net.start()

    info( '*** Running CLI\n' )
    CLI( net )

    info( '*** Stopping network' )
    #net.pingPairFull()
    net.stop()

if __name__ == '__main__':
    x = int(sys.argv[1]) 
    y = int(sys.argv[2])
    setLogLevel( 'info' )
    emptyNet()
