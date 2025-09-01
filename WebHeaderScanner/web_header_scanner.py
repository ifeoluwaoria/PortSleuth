#!/usr/bin/env python3
import requests
import argparse
from tabulate import tabulate
from colorama import init, Fore, Style
from time import sleep

# Initialize colorama
init(autoreset=True)

SECURITY_HEADERS = [
    "Content-Security-Policy",
    "Strict-Transport-Security",
    "X-Frame-Options",
    "X-Content-Type-Options",
    "Referrer-Policy",
    "Permissions-Policy"
]

def scan_headers(url):
    try:
        if not url.startswith("http"):
            url = "http://" + url
        response = requests.get(url, timeout=5)
        headers = response.headers
        print(Fore.CYAN + f"\n🔎 Scanning headers for: {url}\n")
        print(tabulate(headers.items(), headers=["Header", "Value"], tablefmt="grid"))

        print("\n🛡️ Security Header Check:\n")
        for header in SECURITY_HEADERS:
            if header in headers:
                print(Fore.GREEN + f"✅ {header} is present: {headers[header]}")
            else:
                print(Fore.RED + f"❌ {header} is MISSING!")

        return headers

    except requests.exceptions.RequestException as e:
        print(Fore.YELLOW + f"⚠️ Could not reach {url}: {e}")
        return None

def save_to_csv(results, filename="headers_results.csv"):
    import csv
    with open(filename, "w", newline="") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["URL", "Header", "Value"])
        for url, headers in results.items():
            if headers:
                for key, value in headers.items():
                    writer.writerow([url, key, value])
    print(Fore.CYAN + f"\n✅ Results saved to {filename}\n")

def main():
    parser = argparse.ArgumentParser(description="HeaderSleuth - Web Header Scanner")
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("-u", "--url", help="Single URL to scan")
    group.add_argument("-f", "--file", help="File containing URLs to scan, one per line")
    args = parser.parse_args()

    results = {}

    if args.url:
        headers = scan_headers(args.url)
        results[args.url] = headers
    elif args.file:
        try:
            with open(args.file, "r") as f:
                urls = [line.strip() for line in f if line.strip()]
            total = len(urls)
            for idx, url in enumerate(urls, 1):
                print(Fore.MAGENTA + f"\nProcessing {idx}/{total}: {url}")
                headers = scan_headers(url)
                results[url] = headers
                sleep(0.5)  # slight delay for readability
        except FileNotFoundError:
            print(Fore.RED + f"❌ File '{args.file}' not found.")
            return

    save_to_csv(results)

if __name__ == "__main__":
    main()

