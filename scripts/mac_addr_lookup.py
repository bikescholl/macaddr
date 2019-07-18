"""
Command line Tool for looking up MAC Address information from macaddress.io
Parameters:
mac_address (str): Mac Address to be looked up against macaddress.io
"""

import json
import argparse
import os
import yaml
import requests

def get_mac_addr(userkey, mac):
    """
    Function to get the Mac Address Info requested from macaddress.io
    Makes a request to macaddress.io via their API using Headers
    Parameters:
    userkey (str): User key to access the macaddress.io API
    mac (str): Mac address to lookup
    Returns:
    Response: Returns Response object from lookup
    """
    session = requests.Session()
    session.headers.update({'X-Authentication-Token': userkey, 'Content-Type':'application/json'})
    url = "https://api.macaddress.io/v1"
    params = {"search": mac, "output": "json"}
    response_data = requests.get(url, headers=session.headers, params=params)
    return response_data


def main(mac_lookup):
    """
    Main function to execute the mac address lookup.
    Parameters:
    mac_lookup (str): MAC Address used for lookup
    Returns:
    dict: Dictionary representation of the macaddress.io API response.
    """
    api_key = os.environ.get('API_KEY')
    mac_return = get_mac_addr(api_key, mac_lookup).content
    return json.loads(mac_return.decode("utf-8"))

if __name__ == "__main__":
    PARSER = argparse.ArgumentParser(description= \
			"Command line tool for accessing Mac Address info from macaddress.io")
    PARSER.add_argument("--json", action='store_true',  \
			default=False, help="Pretty Print JSON output (default: False)")
    PARSER.add_argument("--yaml", action='store_true', \
			default=False, help="Pretty Print YAML output (default: False)")
    PARSER.add_argument("mac_address", metavar="MAC", \
			help="MAC Address to perform a lookup")
    ARGS = PARSER.parse_args()
    MAC_OUTPUT = main(ARGS.mac_address)
    if 'vendorDetails' in MAC_OUTPUT:
        print(json.dumps(MAC_OUTPUT['vendorDetails'], sort_keys=True, indent=4))
    elif ARGS.yaml:
        print(yaml.safe_dump(MAC_OUTPUT, sort_keys=True, indent=2))
    elif ARGS.json:
        print(json.dumps(MAC_OUTPUT, sort_keys=True, indent=4))
    else:
        print(json.dumps(MAC_OUTPUT))
