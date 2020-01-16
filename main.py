import csv
import subprocess
import threading
import concurrent.futures

# read csv
def read_network():
    with open('network.csv', mode="r") as file:
        ip_addresses = []
        reader = csv.reader(file)
        for row in reader:
            for num in range(1, 10):
                ip_addresses.append(', '.join(row) + str(num))
    return ip_addresses


# write csv
def write_result(responses):
    with open('net1.csv', mode="w") as file:
        writer = csv.writer(file)
        for response in responses:
            writer.writerow([response])
                
def ping(ip_address):
    return subprocess.call(['ping', '-c', '1',ip_address])

IP_ADDRESS = read_network()
results = []

# We can use a with statement to ensure threads are cleaned up promptly
with concurrent.futures.ThreadPoolExecutor() as executor:
    # Start the load operations and mark each future with its URL
    future_ping = {executor.submit(ping, ip_address): ip_address for ip_address in IP_ADDRESS}
    for future in concurrent.futures.as_completed(future_ping):
        ip_address = future_ping[future]
        try:
            data = future.result()
        except Exception as exc:
            print('%r generated an exception: %s' % (ip_address, exc))
        else:
            results.append(f"{ip_address}   {data}")


write_result(results)

#response = os.system("ping -c 1 192.168.219.189")
#res = subprocess.call(['ping', '-c', '3','192.168.219.189'])
#print("dddd " + str(res))




