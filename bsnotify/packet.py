import struct

class Packet:
    red=0
    green=0
    blue=0
    led=0
    flags=0
    
    def to_bytes(self):
        return bytearray(struct.pack('5B',self.led,self.red,self.green,self.blue,self.flags))
    
    def __init__(self,**kwargs):
        self.led=int(kwargs.get("led") or 0)
        self.red=int(kwargs.get("red") or 0)
        self.green=int(kwargs.get("green") or 0)
        self.blue=int(kwargs.get("blue") or 0)
        self.flags=int(kwargs.get("flags") or 0)
    
    @classmethod
    def from_bytes(self,bytes):
        p = Packet()
        (p.led,p.red,p.green,p.blue,p.flags) = struct.unpack('5B', bytes)
        return p