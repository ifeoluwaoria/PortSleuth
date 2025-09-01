#!/usr/bin/env python3
import requests
from tabulate import tabulate
import argparse
import csv
from urllib.parse import urlparse
from datetime import datetime

# Security headers to check
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

        print(f"\n🔎 Scanning headers for: {url}")
        table = [[k, v] for k, v in headers.items()]
        print(tabulate(table, headers=["Header", "Value"], tablefmt="grid"))

        print("\n🛡️ Security Header Check:")
        results = {}
        for header in SECURITY_HEADERS:
            if header in headers:
                print(f"✅ {header} is present: {headers[header]}")
                results[header] = headers[header]
            else:
                print(f"❌ Missing: {header}")
                results[header] = "MISSING"

        return url, results

    except Exception as e:
        print(f"❌ Error scanning {url}: {e}")
        return url, {h: "ERROR" for h in SECURITY_HEADERS}

def save_to_csv(results, filename=None):
    if not filename:
        filename = f"headers_results_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv"

    with open(filename, "w", newline="") as csvfile:
        fieldnames = ["URL"] + SECURITY_HEADERS
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for url, headers in results:
            row = {"URL": url, **headers}
            writer.writerow(row)
    print(f"✅ Results saved to {filename}")

def main():
    parser = argparse.ArgumentParser(description="HeaderSleuth - Web Header Scanner")
    parser.add_argument("-u", "--url", help="Scan a single URL")
    parser.add_argument("-f", "--file", help="Scan multiple URLs from a file")
    args = parser.parse_args()

    targets = []

    if args.url:
        targets.append(args.url.strip())
    elif args.file:
        try:
            with open(args.file, "r") as f:
                targets = [line.strip() for line in f if line.strip()]
        except FileNotFoundError:
            print(f"❌ File '{args.file}' not found.")
            return
    else:
        print("❌ Please provide a URL (-u) or a file (-f) of URLs.")
        return

    all_results = []
    for target in targets:
        all_results.append(scan_headers(target))

    save_to_csv(all_results)

if __name__ == "__main__":
    main()

