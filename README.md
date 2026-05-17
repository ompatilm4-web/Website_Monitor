# Website Monitor

> A lightweight, modular Python tool for monitoring website availability, measuring response times, logging activity, persisting results in SQLite, and generating uptime reports.

---

## Table of Contents

- [Features](#features)
- [Folder Structure](#folder-structure)
- [System Flow](#system-flow)
- [Module Overview](#module-overview)
- [Requirements](#requirements)
- [Installation & Usage](#installation--usage)
- [Output Files](#output-files)
- [Roadmap](#roadmap)
- [License](#license)

---

## Features

- Monitor multiple websites concurrently
- Measure HTTP response time and status codes
- Persist results in a local SQLite database
- Structured activity logging
- Generate human-readable uptime reports
- Modular architecture — easy to extend

---

## Folder Structure

```
website-monitor/
│
├── main.py               # Entry point
├── monitor.py            # Core monitoring logic
├── database.py           # SQLite database operations
├── logger_config.py      # Logging configuration
├── reports.py            # Uptime report generation
│
├── websites.db           # Generated: monitoring data
├── monitor.log           # Generated: activity log
└── uptime_report.txt     # Generated: uptime summary
```

---

## System Flow

```mermaid
flowchart TD

A[main.py] --> B[monitor.py]

B --> C[Send HTTP Requests]
C --> D[Measure Response Time]

D --> E[Store Results]

E --> F[database.py]
F --> H[websites.db]

E --> G[logger_config.py]
G --> I[monitor.log]

A --> J[reports.py]
J --> K[uptime_report.txt]
```

---

## How It Works

1. **`main.py`** initializes and orchestrates the monitoring cycle.
2. **`monitor.py`** dispatches HTTP requests to all configured target websites.
3. Response time and HTTP status are captured and evaluated.
4. **`database.py`** persists the results into `websites.db` (SQLite).
5. **`logger_config.py`** writes structured activity entries to `monitor.log`.
6. **`reports.py`** reads the database and produces a summary in `uptime_report.txt`.

---

## Module Overview

| Module             | Responsibility                          |
|--------------------|-----------------------------------------|
| `main.py`          | Application entry point and orchestration |
| `monitor.py`       | HTTP request handling and status checks |
| `database.py`      | SQLite schema, reads, and writes        |
| `logger_config.py` | Centralized logging setup               |
| `reports.py`       | Uptime report generation from DB data   |

---

## Requirements

- Python **3.8** or higher
- [`requests`](https://pypi.org/project/requests/) library

---



## Output Files

| File                | Description                              |
|---------------------|------------------------------------------|
| `websites.db`       | SQLite database storing all check results |
| `monitor.log`       | Timestamped log of monitoring activity   |
| `uptime_report.txt` | Human-readable uptime summary report     |

---

## Roadmap

- [ ] Email / SMS alerts on downtime detection
- [ ] External config file for managing target websites
- [ ] Web-based dashboard for real-time visualization
- [ ] CSV and JSON export support
- [ ] Scheduled monitoring via cron or APScheduler

---



