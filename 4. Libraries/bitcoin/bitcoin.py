# Bitcoin

"""
Bitcoin is a form of digitial currency, otherwise known as cryptocurrency. Rather than rely on a central authority like a bank, Bitcoin instead relies on a distributed network, otherwise known as a blockchain, to record transactions.

Because there’s demand for Bitcoin (i.e., users want it), users are willing to buy it, as by exchanging one currency (e.g., USD) for Bitcoin.

In a file called bitcoin.py, implement a program that:

    Expects the user to specify as a command-line argument the number of Bitcoins, 

, that they would like to buy. If that argument cannot be converted to a float, the program should exit via sys.exit with an error message.
Queries the API for the CoinDesk Bitcoin Price Index at https://api.coindesk.com/v1/bpi/currentprice.json, which returns a JSON object, among whose nested keys is the current price of Bitcoin as a float. Be sure to catch any exceptions, as with code like:

import requests

try:
    ...
except requests.RequestException:
    ...

Outputs the current cost of

    Bitcoins in USD to four decimal places, using , as a thousands separator.

Hints

    Recall that the sys module comes with argv, per docs.python.org/3/library/sys.html#sys.argv.
    Note that the requests module comes with quite a few methods, per requests.readthedocs.io/en/latest, among which are get, per requests.readthedocs.io/en/latest/user/quickstart.html#make-a-request, and json, per requests.readthedocs.io/en/latest/user/quickstart.html#json-response-content. You can install it with:

    pip install requests
"""

import sys
import requests

# Handling comand-line arguments
if len(sys.argv) == 1:
    sys.exit('Missing comand-line argument')
elif len(sys.argv) > 2:
    sys.exit('Too many command-line arguments')
else:
    try:
        sys.argv[1] = float(sys.argv[1])
    except ValueError:
        sys.exit('Command-line argument is not a number')

# Requesting the JSON object
try:
    response = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json')
except requests.RequestException:
    print("Request not successful")

# Getting the conversion rate inside the JSON dictionary
o = response.json()
usd_rate = o['bpi']['USD']['rate_float']
amount = float(usd_rate) * sys.argv[1]
print(f"${amount:,.4f}")
