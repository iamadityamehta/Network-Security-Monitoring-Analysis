from scapy.all import sniff, TCP, UDP, ICMP
import matplotlib.pyplot as plt

print("Capturing 100 packets... please browse some websites to generate traffic.")
# Capture 100 packets from the network
pkts = sniff(count=100)

# Identify at least three different protocols
stats = {"TCP": 0, "UDP": 0, "ICMP": 0, "Other": 0}

for p in pkts:
    if p.haslayer(TCP): stats["TCP"] += 1
    elif p.haslayer(UDP): stats["UDP"] += 1
    elif p.haslayer(ICMP): stats["ICMP"] += 1
    else: stats["Other"] += 1

# Generate a bar chart showing protocol distribution
plt.bar(stats.keys(), stats.values(), color=['blue', 'green', 'red', 'gray'])
plt.title("Network Protocol Distribution")
plt.xlabel("Protocol Type")
plt.ylabel("Number of Packets")
plt.savefig("protocol_chart.png") # This saves the image to your desktop
print("Done!")
