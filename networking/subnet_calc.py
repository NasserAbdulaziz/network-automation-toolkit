#!/usr/bin/env python3

import argparse
import ipaddress

def get_arguments():
    parser = argparse.ArgumentParser(description="Subnet Calculator")
    parser.add_argument("-t", "--target", dest="target", help="Target IP / CIDR (e.g. 192.168.1.1/24)")
    options = parser.parse_args()
    if not options.target:
        parser.error("[-] Please specify a target IP / CIDR")
    return options

def calculate_subnet(ip_string):
    """
    Takes an IP string (e.g., 192.168.1.1/24) and prints network details.
    """
    try:
        # 1. Create the network object
        # 'strict=False' allows us to pass a host IP (like .5) and still get the network
        network = ipaddress.ip_network(ip_string, strict=False)

        print(f"\n[+] Subnet Details for {ip_string}")
        print("-" * 40)

        # 2. Extract and print details
        print(f"Network Address: {network.network_address}")
        print(f"Broadcast Address: {network.broadcast_address}")
        print(f"Subnet Mask: {network.netmask}")
        print(f"Total Hosts: {network.num_addresses}")
        print(f"Usable Hosts: {network.num_addresses - 2}")

        print("-" * 40)

    except ValueError:
        print("[-] Error: Invalid IP address format.")

# ___ Main Execution ___
if __name__ == "__main__":
    options = get_arguments()
    calculate_subnet(options.target)