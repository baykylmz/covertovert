from scapy.all import sniff, IP, ICMP

def handle_packet(packet):
    if packet.haslayer(ICMP) and packet[IP].ttl == 1:
        packet[ICMP].show()

def receive_icmp():
    sniff(filter="icmp", prn=handle_packet)

if __name__ == "__main__":
    receive_icmp()