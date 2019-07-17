import requests
import json
import yaml

def get_mac_addr(userkey, mac):
    """
    Function to get the Mac Address Info requested from macaddress.io.
    Makes a request to macaddress.io via their API using Headers

    Parameters:
    userkey (str): User key to access the macaddress.io API
    mac (str): Mac address to lookup

    Returns:
    dict: Returns dictionary values from lookup
    """
    url = f"https://macaddress.io/v1?output=json&search={mac}"
    headers = {"X-Authentication-Token": userkey}
    r = requests.get(url, headers=headers)
    return r


def main():
    mac_addr = get_mac_addr('at_Zqv1oE2FQAZjtZPHdYqLdanmCoJUb', '44:38:39:ff:ef:57')
    return mac_addr

if __name__ == "__main__":
    main()
