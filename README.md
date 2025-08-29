
# PortSleuth - Simple Python Port Scanner

PortSleuth is a lightweight Python 3 script for scanning TCP ports on a target host. It’s designed for learning and cybersecurity practice, allowing you to check which ports are open or closed on a given IP or hostname.

## Features

- Scan single ports, multiple ports, or a range of ports.
- Default scan includes ports 80 and 443.
- Simple output indicating **OPEN** or **CLOSED/filtered** ports.
- Easy to run with Python 3.

## Installation

1. Clone this repository:

```bash
git clone https://github.com/ifeoluwaoria/PortSleuth.git
cd PortSleuth

2) Ensure you have Python 3 installed:
python3 --version

3) Usage
python3 portsleuth.py <target> [-p PORTS]

<target>: IP address or hostname you want to scan.

-p PORTS (optional): Ports to scan. Can be a single port, comma-separated list, or range.

4)Examples

Scan default ports (80 and 443):

python3 portsleuth.py scanme.nmap.org

Scan specific ports:

python3 portsleuth.py scanme.nmap.org -p 21,22,80,443

Scan a range of ports:

python3 portsleuth.py scanme.nmap.org -p 20-25

5) Disclaimer

PortSleuth is intended for educational purposes only. Do not use this tool to scan systems you do not own or have explicit permission to test.

6) License

This project is open-source and available under the MIT License.

License

This project is open-source and available under the MIT License.

 
