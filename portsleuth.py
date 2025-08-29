#!/usr/bin/env python3
import socket
import argparse

def scan_port(target, port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(2)  # increase timeout to 2 seconds
        result = sock.connect_ex((target, port))
        if result == 0:
            print(f"[+] Port {port} is OPEN")
        else:
            print(f"[-] Port {port} is CLOSED or filtered")
        sock.close()
    except Exception as e:
        print(f"[-] Error scanning port {port}: {e}")

def main():
    parser = argparse.ArgumentParser(description="PortSleuth - Simple Port Scanner")
    parser.add_argument("target", help="Target IP or hostname")
    parser.add_argument("-p", "--ports", help="Ports to scan (e.g. 20-80 or 21,22,80,443)")
    args = parser.parse_args()

    # Parse ports (can be "20-80" or "21,22,80,443")
    ports = []
    if args.ports:
        if "-" in args.ports:  # range like 20-80
            start_port, end_port = map(int, args.ports.split("-"))
            ports = range(start_port, end_port + 1)
        elif "," in args.ports:  # list like 21,22,80,443
            ports = [int(p.strip()) for p in args.ports.split(",")]
    else:
        ports = [80, 443]  # default

    print(f"[*] Scanning target {args.target}")
    for port in ports:
        scan_port(args.target, port)

if __name__ == "__main__":
    main()
