#i/usr/bin/env python3

import subprocess
import argparse

def get_arguments():
    """
    Parses command line arguments for the interface and new MAC address.
    """
    parser = argparse.ArgumentParser(description="A tool to change the MAC address of a network interface.")

    # We define the flags user can use (e.g., -i or --interface)
    parser.add_argument("-i", "--interface", dest="interface", help="Interface to change its MAC address")
    parser.add_argument("-m", "--mac", dest="new_mac", help="New MAC Address")

    args = parser.parse_args()

    # Validation: Ensure the user actually provided inputs
    if not args.interface:
        parser.error("[-] Please specify an interface, use --help for info.")
    elif not args.new_mac:
        parser.error("[-] Please specify a new MAC, use --help for info. ")

    return args
def change_mac(interface, new_mac):
    """
    Uses subprocess to execute Linux shell commands to change the MAC.
    """
    print(f"[+] Changing MAC address for {interface} to {new_mac}")
    try:
        # We use list format for security (prevents shell injection attacks)
        subprocess.call(["ifconfig", interface, "down"])
        subprocess.call(["ifconfig", interface, "hw", "ether", new_mac])
        subprocess.call(["ifconfig", interface, "up"])
    except FileNotFoundError:
        print("[-] Error: 'ifconfig' command not found.")
        print("    This script relies on Linux tools. Please run a compatible OS (e.g., Ubuntu, Kali).")
    except PermissionError:
        print("[-] Error: Permission denied. Run this script with 'sudo'.")
        
# --- Main Execution ---
if __name__ == "__main__":
    # 1. Get inputs
    options = get_arguments()

    # Print them to verify (Debug step)
    # print(f"[+] Interface: {options.interface}")
    # print(f"[+] New MAC:")
    
    # 2. execute the change
    change_mac(options.interface, options.new_mac)
