import paho.mqtt.client as mqtt
from blinkstick import blinkstick
import struct
import os.path
from bsnotify import packet

# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))
    client.subscribe("blinkstick/BS002233-3.0")

PACKET_SIZE=5

# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    for i in range(0,len(msg.payload),PACKET_SIZE):
        pkt = msg.payload[i:i+PACKET_SIZE]
        if len(pkt) == PACKET_SIZE:            
            p = packet.Packet.from_bytes(pkt)
            serial = os.path.split(msg.topic)[-1]
            print "Setting LED "+str(p.led)+" to R"+str(p.red)+" G"+str(p.green)+" B"+str(p.blue)
            stick = blinkstick.find_by_serial(serial)
            if stick != None:
                # print index,r,g,blue
                stick.set_color(0,p.led,p.red,p.green,p.blue)

# sticks = map(lambda s: (s.get_serial(), s), blinkstick.find_all())

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect("boris.tlyk.eu", 1883, 60)

# Blocking call that processes network traffic, dispatches callbacks and
# handles reconnecting.
# Other loop*() functions are available that give a threaded interface and a
# manual interface.
client.loop_forever()