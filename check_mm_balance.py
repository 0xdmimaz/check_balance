import time
import random
from datetime import datetime
import web3
from web3 import Web3

endpoint = input('Enter your RPC endpoint: ')   # https://foo.bar
web3 = Web3(web3.HTTPProvider(endpoint))
address = input('Enter your address: ')   # 0x.....
repeat_count = int(input('Enter your repeat count: '))   # 10
idle = [1, 2]
file = open('log.txt', 'a')


def get_balance(_address, _time):
    balance = web3.eth.get_balance(_address)
    random_idle = random.choice(_time)
    time.sleep(random_idle)
    return random_idle, balance


for i in range(repeat_count):
    random_idle, balance = get_balance(address, idle)
    dt = datetime.now()
    log_str = f"{i} - {dt} - {endpoint} - {address} - {random_idle} - {balance}"
    file.write(f"{log_str} \n")
    print(f"{log_str}")

file.close()
