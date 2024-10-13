import pyshark
import pandas as pd

pcap_file = 'pcap_file.pcap'
capture = pyshark.FileCapture(pcap_file)

# Extract packet information
packet_data = []
for packet in capture:
    # if(int(packet.number) > 1000):
    #     break
    print(packet.number)
    try:
        packet_info = {
            'No': packet.number,
            'Time': packet.sniff_time,
            'Source': packet.ip.src if hasattr(packet, 'ip') and packet.ip else '',
            'Destination': packet.ip.dst if hasattr(packet, 'ip') and packet.ip else '',
            'Protocol': packet.transport_layer if hasattr(packet, 'transport_layer') else '',
            'Length': packet.length if hasattr(packet, 'length') else '',
            'Info': packet.info if hasattr(packet, 'info') else ''
        }
        packet_data.append(packet_info)
    except Exception as e:
        print(f"Error processing packet: {e}")

capture.close()

df = pd.DataFrame(packet_data)
df.to_csv('output.csv', index=False)