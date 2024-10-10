from web3.utils.address import to_checksum_address

reward = 10 # USDC
csv_path = './csv/winners.csv'

# print output (header)
print("Address,USDC")

# print output (body)
with open(csv_path, 'r') as file:
    for index, line in enumerate(file):
        if index == 0: continue # skip header
        [addr, _, _] = line.strip().split(',')
        addr = addr.lower()
        print("{},{}".format(to_checksum_address(addr), reward))
