#!/usr/bin/env python3
import socket
import argparse
import sys
from time import sleep

# ANSI color codes
GREEN = "\033[92m"
RED = "\033[91m"
YELLOW = "\033[93m"
RESET = "\033[0m"

def scan_port(target, port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(2)
        result = sock.connect_ex((target, port))
        if result == 0:
            print(f"{GREEN}[+] Port {port} is OPEN{RESET}")
        else:
            print(f"{RED}[-] Port {port} is CLOSED or filtered{RESET}")
        sock.close()
    except Exception as e:
        print(f"{RED}[-] Error scanning port {port}: {e}{RESET}")

def main():
    parser = argparse.ArgumentParser(
        description="PortSleuth - Simple Port Scanner with colored output and progress"
    )
    parser.add_argument("target", help="Target IP or hostname")
    parser.add_argument("-p", "--ports", help="Ports to scan (e.g. 20-80 or 21,22,80,443)")
    args = parser.parse_args()

    # Parse ports
    ports = []
    if args.ports:
        if "-" in args.ports:  # range like 20-80
            start_port, end_port = map(int, args.ports.split("-"))
            ports = range(start_port, end_port + 1)
        elif "," in args.ports:  # list like 21,22,80,443
            ports = [int(p.strip()) for p in args.ports.split(",")]
    else:
        ports = [80, 443]  # default

    total = len(ports)
    print(f"{YELLOW}[*] Scanning target {args.target} ({total} ports){RESET}")
    for i, port in enumerate(ports, start=1):
        print(f"{YELLOW}Scanning port {port} ({i}/{total})...{RESET}", end="\r")
        scan_port(args.target, port)
        sleep(0.1)  # small delay for readability
    print(f"{YELLOW}[*] Scan completed.{RESET}")

if __name__ == "__main__":
    main()

