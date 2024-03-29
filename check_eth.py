import time
import random
import web3
from datetime import datetime
from web3 import Web3
from requests.exceptions import ReadTimeout, HTTPError, ChunkedEncodingError, ConnectionError
from urllib3.exceptions import ProtocolError
from processing_json import config

endpoint = config["network"]["eth"]["endpoint"]
address = config["network"]["eth"]["address"]
repeats = config["network"]["eth"]["repeats"]
idle = config["network"]["eth"]["idle"]

web3 = Web3(web3.HTTPProvider(endpoint))
current_time = datetime.now()


def get_balance(_address, _time):
    balance = web3.eth.get_balance(_address)
    random_idle = random.choice(_time)
    time.sleep(random_idle)
    return random_idle, balance


def print_error(iteration, timestamp, error):
    log_file = open("logs/errors_eth.log", "a")
    log_file.write(f"{iteration} - {timestamp} - {error} \n")
    log_file.close()
    if error == ValueError or error == ProtocolError:
        print(f"{iteration} - {timestamp} - ERROR - {error}")
    else:
        print(f"{iteration} - {timestamp} - ERROR - {error}")


for i in range(1, repeats):
    try:
        wait_time, wallet_balance = get_balance(address, idle)
        log_str = f"{i} - {current_time} - {wait_time} - {wallet_balance}"
        print(f"{log_str}")

    except ReadTimeout as err:
        print_error(i, current_time, err)

    except HTTPError as err:
        print_error(i, current_time, err)

    except ValueError as err:
        print_error(i, current_time, err)

    except ChunkedEncodingError as err:
        print_error(i, current_time, err)

    except ProtocolError as err:
        print_error(i, current_time, err)

    except ConnectionError as err:
        print_error(i, current_time, err)
