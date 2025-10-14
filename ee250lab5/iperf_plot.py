import matplotlib.pyplot as plt 
import pandas as pd 


tcp_data_2m = pd.read_csv('iperf_tcp_2m.csv')
udp_data_2m = pd.read_csv('iperf_udp_2m.csv')
tcp_data_5m = pd.read_csv('iperf_tcp_5m.csv')
udp_data_5m = pd.read_csv('iperf_udp_5m.csv')
tcp_data_8m = pd.read_csv('iperf_tcp_8m.csv')
udp_data_8m = pd.read_csv('iperf_udp_8m.csv')
tcp_data_10m = pd.read_csv('iperf_tcp_10m.csv')
udp_data_10m = pd.read_csv('iperf_udp_10m.csv')
tcp_data_15m = pd.read_csv('iperf_tcp_15m.csv')
udp_data_15m = pd.read_csv('iperf_udp_15m.csv')

#2m
plt.figure(figsize = (10, 6))

for index, row in tcp_data_2m.iterrows():
    distance = row['Distance']
    run_no = row[['Run1', 'Run2', 'Run3', 'Run4', 'Run5']]
    plt.plot([1, 2, 3, 4, 5], run_no, marker = '-', label = f'Distance {distance}m')

for index, row in udp_data_2m.iterrows():
    distance = row['Distance']
    run_no = row[['Run1', 'Run2', 'Run3', 'Run4', 'Run5']]
    plt.plot([1, 2, 3, 4, 5], run_no, marker = '-', label = f'Distance {distance}m')

plt.title('Test Runs vs Throughput (2m)')
plt.xlabel('Test Run #')
plt.ylabel('Throughput (Mbps)')
plt.xticks([1, 2, 3, 4, 5], ['Run 1', 'Run 2', 'Run 3', 'Run 4', 'Run 5'])
plt.grid(True)
plt.legend()

plt.show()

#5m
plt.figure(figsize = (10,6))

for index, row in tcp_data_5m.iterrows():
    distance = row['Distance']
    run_no = row[['Run1', 'Run2', 'Run3', 'Run4', 'Run5']]
    plt.plot([1, 2, 3, 4, 5], run_no, marker = '-', label = f'Distance {distance}m')

for index, row in udp_data_5m.iterrows():
    distance = row['Distance']
    run_no = row[['Run1', 'Run2', 'Run3', 'Run4', 'Run5']]
    plt.plot([1, 2, 3, 4, 5], run_no, marker = '-', label = f'Distance {distance}m')

plt.title('Test Runs vs Throughput (5m)')
plt.xlabel('Test Run #')
plt.ylabel('Throughput (Mbps)')
plt.xticks([1, 2, 3, 4, 5], ['Run 1', 'Run 2', 'Run 3', 'Run 4', 'Run 5'])
plt.grid(True)
plt.legend()

plt.show()

#8m
plt.figure(figsize = (10,6))

for index, row in tcp_data_8m.iterrows():
    distance = row['Distance']
    run_no = row[['Run1', 'Run2', 'Run3', 'Run4', 'Run5']]
    plt.plot([1, 2, 3, 4, 5], run_no, marker = '-', label = f'Distance {distance}m')

for index, row in udp_data_8m.iterrows():
    distance = row['Distance']
    run_no = row[['Run1', 'Run2', 'Run3', 'Run4', 'Run5']]
    plt.plot([1, 2, 3, 4, 5], run_no, marker = '-', label = f'Distance {distance}m')

plt.title('Test Runs vs Throughput (8m)')
plt.xlabel('Test Run #')
plt.ylabel('Throughput (Mbps)')
plt.xticks([1, 2, 3, 4, 5], ['Run 1', 'Run 2', 'Run 3', 'Run 4', 'Run 5'])
plt.grid(True)
plt.legend()

plt.show()

#10m
plt.figure(figsize = (10,6))

for index, row in tcp_data_10m.iterrows():
    distance = row['Distance']
    run_no = row[['Run1', 'Run2', 'Run3', 'Run4', 'Run5']]
    plt.plot([1, 2, 3, 4, 5], run_no, marker = '-', label = f'Distance {distance}m')

for index, row in udp_data_10m.iterrows():
    distance = row['Distance']
    run_no = row[['Run1', 'Run2', 'Run3', 'Run4', 'Run5']]
    plt.plot([1, 2, 3, 4, 5], run_no, marker = '-', label = f'Distance {distance}m')

plt.title('Test Runs vs Throughput (10m)')
plt.xlabel('Test Run #')
plt.ylabel('Throughput (Mbps)')
plt.xticks([1, 2, 3, 4, 5], ['Run 1', 'Run 2', 'Run 3', 'Run 4', 'Run 5'])
plt.grid(True)
plt.legend()

plt.show()

#15 m
plt.figure(figsize = (10,6))

for index, row in tcp_data_15m.iterrows():
    distance = row['Distance']
    run_no = row[['Run1', 'Run2', 'Run3', 'Run4', 'Run5']]
    plt.plot([1, 2, 3, 4, 5], run_no, marker = '-', label = f'Distance {distance}m')

for index, row in udp_data_15m.iterrows():
    distance = row['Distance']
    run_no = row[['Run1', 'Run2', 'Run3', 'Run4', 'Run5']]
    plt.plot([1, 2, 3, 4, 5], run_no, marker = '-', label = f'Distance {distance}m')

plt.title('Test Runs vs Throughput (15m)')
plt.xlabel('Test Run #')
plt.ylabel('Throughput (Mbps)')
plt.xticks([1, 2, 3, 4, 5], ['Run 1', 'Run 2', 'Run 3', 'Run 4', 'Run 5'])
plt.grid(True)
plt.legend()

plt.show()