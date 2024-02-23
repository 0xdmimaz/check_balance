import time
import random
import web3
from web3 import Web3

endpoint = input('Enter your RPC endpoint: ')   # https://foo.bar
web3 = Web3(web3.HTTPProvider(endpoint))
address = input('Enter your address: ')   # 0x.....
idle = [1, 2]


def get_balance(_address, _time):
    balance = web3.eth.get_balance(_address)
    random_idle = random.choice(_time)
    time.sleep(random_idle)
    return random_idle, balance


for i in range(2000000):
    random_idle, balance = get_balance(address, idle)
    print(f"ITERATION: {i} - IDLE: {random_idle} - BALANCE: {balance}")
