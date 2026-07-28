import os

# Locally these default to ./data and ./logs (relative to wherever the app
# is started from). On platforms with a read-only filesystem (e.g. Vercel's
# serverless functions), set DATA_DIR / LOG_DIR to a writable path such as
# /tmp/data and /tmp/logs via environment variables.
DATA_DIR = os.environ.get("DATA_DIR", "data")
LOG_DIR = os.environ.get("LOG_DIR", "logs")
REPORTS_DIR = os.environ.get("REPORTS_DIR", "reports")

DB_PATH = os.path.join(DATA_DIR, "websites.db")
LOG_PATH = os.path.join(LOG_DIR, "monitor.log")
REPORT_CSV_PATH = os.path.join(REPORTS_DIR, "uptime_report.csv")
