from paho.mqtt import publish
import struct
import sys
from colour import Color
from bsnotify import packet

led = int(sys.argv[1])
c = Color(sys.argv[2])
p = packet.Packet(red=c.red*255,blue=c.blue*255,green=c.green*255,led=led)
publish.single("blinkstick/BS002233-3.0", p.to_bytes(), qos=1, hostname="boris.tlyk.eu")