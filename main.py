import csv

# read csv
def read_network():
    with open('network.csv', mode="r") as file:
        ip_addresses = []
        reader = csv.reader(file)
        for row in reader:
            for num in range(1, 3):
                ip_addresses.append(', '.join(row) + str(num))
    return ip_addresses


# write csv
def write_result():
    ip_addresses = read_network()
    with open('net1.csv', mode="w") as file:
        writer = csv.writer(file)
        for ip_address in ip_addresses:
            writer.writerow(["network", "hostname", "success"])
            writer.writerow([f"{ip_address}"])


write_result()





