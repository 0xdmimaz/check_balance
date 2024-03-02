import time
import json
import random
from datetime import datetime
import web3
from web3 import Web3
from requests.exceptions import ReadTimeout, HTTPError

with open('config.json', 'r') as config_file:
    config = json.load(config_file)

web3 = Web3(web3.HTTPProvider(config["endpoint"]))
dt = datetime.now()


def get_balance(_address, _time):
    balance = web3.eth.get_balance(_address)
    random_idle = random.choice(_time)
    time.sleep(random_idle)
    return random_idle, balance


for i in range(config["repeats"]):
    try:
        wait_time, wallet_balance = get_balance(config["address"], config["idle"])
        log_str = f"{i} - {dt} - {config['endpoint']} - {config['address']} - {wait_time} - {wallet_balance}"
        print(f"{log_str}")

    except ReadTimeout as err:
        print(f"{dt} - {err}")

    except HTTPError as err:
        print(f"{dt} - {err}")

    except ValueError as err:
        print(f"{dt} - {err}")
