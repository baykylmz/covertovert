from scapy.all import IP, ICMP, send

def send_icmp():
    packet = IP(dst="172.18.255.255", ttl=1) / ICMP()
    send(packet)

if __name__ == "__main__":
    send_icmp()
