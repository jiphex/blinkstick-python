from paho.mqtt import publish
import struct
import sys
from colour import Color
from bsnotify import packet

if len(sys.argv) > 1:
    c = Color(sys.argv[1])
else:
    c = Color("black")    
pkts = map(lambda x: packet.Packet(led=x,red=c.red*255,green=c.green*255,blue=c.blue*255).to_bytes(), range(0,8))
pktsb = reduce(lambda x,y: x+y, pkts)
publish.single("blinkstick/BS002233-3.0", pktsb, qos=1, hostname="boris.tlyk.eu")