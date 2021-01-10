from scapy.all import *
from scapy.layers.inet import IP, TCP
from scapy.layers.l2 import *

ip1 = IP()
ip1.src = "223.129.0.189"
ip1.dst = "223.129.0.190"

tcp1 = TCP()
tcp1.sport = 80
tcp1.dport = 81

packet1 = Ether() / ip1 / tcp1
packet1.show()
hexdump(packet1)
name1 = "tcp-opposite-five-tuple-1"
wrpcap("src/scapy/" + name1 + ".pcap", packet1)

ip2 = IP()
ip2.src = "223.129.0.190"
ip2.dst = "223.129.0.189"

tcp2 = TCP()
tcp2.sport = 81
tcp2.dport = 80

packet2 = Ether() / ip2 / tcp2
packet2.show()
hexdump(packet2)
name2 = "tcp-opposite-five-tuple-2"
wrpcap("src/scapy/" + name2 + ".pcap", packet2)
