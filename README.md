## System Flow 
flowchart TD

A[main.py]

A --> B[monitor.py]

B --> C[Send HTTP Requests]

C --> D[Measure Response Time]

D --> E[Store Results]

E --> F[database.py]

E --> G[logger_config.py]

F --> H[websites.db]

G --> I[monitor.log]

A --> J[reports.py]

J --> K[uptime_report.txt]