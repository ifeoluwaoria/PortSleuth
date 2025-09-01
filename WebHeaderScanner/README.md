🌐 Web Header & Security Scanner

A Python project for scanning HTTP headers and checking website security headers. Helps identify missing security configurations and provides CSV reports for analysis.

⚡ Quick Start

Clone the project:

git clone https://github.com/your-username/WebHeaderScanner.git
cd WebHeaderScanner


Activate virtual environment:

source venv/bin/activate


Install dependencies:

pip install requests tabulate colorama


Scan a single URL:

python3 headersleuth.py -u example.com
python3 web_header_scanner.py -u example.com


Scan multiple URLs from a file:

python3 headersleuth.py -f urls.txt
python3 web_header_scanner.py -f urls.txt

📝 Scripts
1️⃣ headersleuth.py – Simple Header Scanner

Scan single or multiple URLs.

Saves results in headers_results.csv.

Reports missing security headers.

Security headers checked:

Content-Security-Policy

Strict-Transport-Security

X-Frame-Options

X-Content-Type-Options

Referrer-Policy

Permissions-Policy

2️⃣ web_header_scanner.py – Enhanced Scanner

Color-coded terminal output using colorama.

Handles invalid or unreachable URLs gracefully.

Displays progress indicators.

Saves results in web_headers_results.csv.

Extra Features:

Skips invalid URLs automatically

Easier readability with colors

CSV export for analysis

📊 Output

Terminal table of headers for each URL.

Security header check with ✅/❌ indicators.

CSV files for further analysis:

headers_results.csv (headersleuth)

web_headers_results.csv (web_header_scanner)

⚙️ Dependencies

requests – for HTTP requests

tabulate – for table formatting

colorama – for colored output (only web_header_scanner.py)

Install dependencies inside your virtual environment:

pip install requests tabulate colorama

⚠️ Notes

Only scan websites you have permission to analyze.

Keep CSV results for further reports or analysis.


