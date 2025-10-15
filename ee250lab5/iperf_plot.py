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

def split_runs(row):
    runs = row['Run1'].split()  # Split the 'Run1' column by space
    return pd.Series([float(run) for run in runs], index=['Run1', 'Run2', 'Run3', 'Run4', 'Run5'])

tcp_data_2m.columns = tcp_data_2m.columns.str.strip()
udp_data_2m.columns = udp_data_2m.columns.str.strip()
tcp_data_5m.columns = tcp_data_5m.columns.str.strip()
udp_data_5m.columns = udp_data_5m.columns.str.strip()
tcp_data_8m.columns = tcp_data_8m.columns.str.strip()
udp_data_8m.columns = udp_data_8m.columns.str.strip()
tcp_data_10m.columns = tcp_data_10m.columns.str.strip()
udp_data_10m.columns = udp_data_10m.columns.str.strip()
tcp_data_15m.columns = tcp_data_15m.columns.str.strip()
udp_data_15m.columns = udp_data_15m.columns.str.strip()

# Apply the split function to all datasets
tcp_data_2m[['Run1', 'Run2', 'Run3', 'Run4', 'Run5']] = tcp_data_2m.apply(split_runs, axis=1)
udp_data_2m[['Run1', 'Run2', 'Run3', 'Run4', 'Run5']] = udp_data_2m.apply(split_runs, axis=1)
tcp_data_5m[['Run1', 'Run2', 'Run3', 'Run4', 'Run5']] = tcp_data_5m.apply(split_runs, axis=1)
udp_data_5m[['Run1', 'Run2', 'Run3', 'Run4', 'Run5']] = udp_data_5m.apply(split_runs, axis=1)
tcp_data_8m[['Run1', 'Run2', 'Run3', 'Run4', 'Run5']] = tcp_data_8m.apply(split_runs, axis=1)
udp_data_8m[['Run1', 'Run2', 'Run3', 'Run4', 'Run5']] = udp_data_8m.apply(split_runs, axis=1)
tcp_data_10m[['Run1', 'Run2', 'Run3', 'Run4', 'Run5']] = tcp_data_10m.apply(split_runs, axis=1)
udp_data_10m[['Run1', 'Run2', 'Run3', 'Run4', 'Run5']] = udp_data_10m.apply(split_runs, axis=1)
tcp_data_15m[['Run1', 'Run2', 'Run3', 'Run4', 'Run5']] = tcp_data_15m.apply(split_runs, axis=1)
udp_data_15m[['Run1', 'Run2', 'Run3', 'Run4', 'Run5']] = udp_data_15m.apply(split_runs, axis=1)

#2m
plt.figure(figsize = (10, 6))

for index, row in tcp_data_2m.iterrows():
    distance = row['Distance']
    run_no = row[['Run1', 'Run2', 'Run3', 'Run4', 'Run5']]
    plt.plot([1, 2, 3, 4, 5], run_no, marker = 'o', label = f'Distance {distance}m')

for index, row in udp_data_2m.iterrows():
    distance = row['Distance']
    run_no = row[['Run1', 'Run2', 'Run3', 'Run4', 'Run5']]
    plt.plot([1, 2, 3, 4, 5], run_no, marker = 'o', label = f'Distance {distance}m')

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
    plt.plot([1, 2, 3, 4, 5], run_no, marker = 'o', label = f'Distance {distance}m')

for index, row in udp_data_5m.iterrows():
    distance = row['Distance']
    run_no = row[['Run1', 'Run2', 'Run3', 'Run4', 'Run5']]
    plt.plot([1, 2, 3, 4, 5], run_no, marker = 'o', label = f'Distance {distance}m')

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
    plt.plot([1, 2, 3, 4, 5], run_no, marker = 'o', label = f'Distance {distance}m')

for index, row in udp_data_8m.iterrows():
    distance = row['Distance']
    run_no = row[['Run1', 'Run2', 'Run3', 'Run4', 'Run5']]
    plt.plot([1, 2, 3, 4, 5], run_no, marker = 'o', label = f'Distance {distance}m')

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
    plt.plot([1, 2, 3, 4, 5], run_no, marker = 'o', label = f'Distance {distance}m')

for index, row in udp_data_10m.iterrows():
    distance = row['Distance']
    run_no = row[['Run1', 'Run2', 'Run3', 'Run4', 'Run5']]
    plt.plot([1, 2, 3, 4, 5], run_no, marker = 'o', label = f'Distance {distance}m')

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
    plt.plot([1, 2, 3, 4, 5], run_no, marker = 'o', label = f'Distance {distance}m')

for index, row in udp_data_15m.iterrows():
    distance = row['Distance']
    run_no = row[['Run1', 'Run2', 'Run3', 'Run4', 'Run5']]
    plt.plot([1, 2, 3, 4, 5], run_no, marker = 'o', label = f'Distance {distance}m')

plt.title('Test Runs vs Throughput (15m)')
plt.xlabel('Test Run #')
plt.ylabel('Throughput (Mbps)')
plt.xticks([1, 2, 3, 4, 5], ['Run 1', 'Run 2', 'Run 3', 'Run 4', 'Run 5'])
plt.grid(True)
plt.legend()

plt.show()