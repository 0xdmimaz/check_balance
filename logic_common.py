import os
from datetime import datetime
import web3
from web3 import Web3

web3 = Web3(web3.HTTPProvider(endpoint))
current_time = datetime.now()

vcpu_count = os.cpu_count()
