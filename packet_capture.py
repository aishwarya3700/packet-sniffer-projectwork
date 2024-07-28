import multiprocessing
from scapy.all import sniff
import api.models

def packet_capture(interface):
    def packet_handler(packet):
        # Extract packet data
        packet_data = {
        "timestamp": str(packet.time),  # Consider using DateTime for improved accuracy
        "source_ip": packet[IP].src,
        "destination_ip": packet[IP].dst,
        "protocol": packet[IP].proto,  # Extract protocol from captured packet
        "source_port": packet[packet.proto].sport,  # Extract source port if applicable
        "destination_port": packet[packet.proto].dport,  # Extract destination port if applicable
        # ... (Extract fields)
    }
        # Create PacketData object and save to database
        new_packet = PacketData(**packet_data)
        packet_obj = PacketData(**packet_data)
        session.add(packet_obj)
        session.commit()

    sniff(iface=interface, prn=packet_handler)

if __name__ == '__main__':
    multiprocessing.Process(target=packet_capture, args=('eth0',)).start()



# from api.models import PacketData, session  # Import PacketData and session


# def packet_capture(interface):
#     def packet_handler(packet):
#         # Extract packet data
#         packet_data = {
#             'timestamp': str(packet.time),
#             'source_ip': packet[IP].src,
#             'destination_ip': packet[IP].dst,
#             # ... other fields
#         }
#         # Create PacketData object and save to database
#         packet_obj = PacketData(**packet_data)
#         session.add(packet_obj)
#         session.commit()

#     sniff(iface=interface, prn=packet_handler)

# if __name__ == '__main__':
#     multiprocessing.Process(target=packet_capture, args=('eth0',)).start()


# import multiprocessing
# from scapy.all import sniff
# import sqlite3

# def packet_capture(db_file):
#     conn = sqlite3.connect(db_file)
#     cursor = conn.cursor()

#     def packet_handler(packet):
#         # Extract relevant data from packet
#         packet_data = {
#             'timestamp': str(packet.time),
#             'source_ip': packet[IP].src,
#             'destination_ip': packet[IP].dst,
#             # Add other fields as needed
#         }
#         cursor.execute("INSERT INTO packets VALUES (?, ?, ?)", (packet_data['timestamp'], packet_data['source_ip'], packet_data['destination_ip']))
#         conn.commit()

#     sniff(iface='eth0', prn=packet_handler)

# if __name__ == '__main__':
#     db_file = 'packets.db'
#     multiprocessing.Process(target=packet_capture, args=(db_file,)).start()
