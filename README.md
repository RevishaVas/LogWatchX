# LogWatchX

**LogWatchX** is a containerized log monitoring and data processing pipeline designed to support structured log ingestion, transformation, and analysis. It integrates **Logstash** for log parsing and **Python** for building a data-focused ETL pipeline, enabling log intelligence for developers, DevOps engineers, and data engineers.

---

## 🔧 Features

- 📥 Ingests logs from files like `app.log` and `applogs.log`
- 🔍 Parses and structures raw log data using **Logstash**
- 🐍 Processes data with a custom **Python ETL pipeline**
- 📊 Outputs cleaned logs and summary statistics to **CSV and SQLite**
- 🚨 Detects error bursts and log anomalies
- 📦 Deployable with **Docker Compose**




---

## 🚀 Getting Started

### ✅ Prerequisites

- [Docker](https://www.docker.com/get-started)
- [Docker Compose](https://docs.docker.com/compose/install/)
- Python 3.7+ with `pandas`, `sqlite3`

---

### 🛠️ Installation & Usage

1. **Clone the repository**:

   ```bash
   git clone https://github.com/RevishaVas/LogWatchX.git
   cd LogWatchX

2. **Start Logstash via Docker Compose**:
   ```
   docker-compose up -d
3. **Run the Python ETL pipeline**:
   
   ```
   python etl.py
**This will:**

Load structured_logs.csv

Clean and structure the logs

Generate a log summary

Store output in CSV and SQLite (logs.db)

---
## ⚙️ Configuration
**🔹 logstash.conf**

  Parses logs using grok patterns:
  ```
  %{TIMESTAMP_ISO8601:timestamp} %{LOGLEVEL:level} %{GREEDYDATA:message}
  ```
  Filters low-severity logs (INFO, DEBUG)
  
  Can output to Elasticsearch or files


  **🔹 etl.py**
  
  Reads structured log file (CSV)
  
  Filters and classifies by severity
  
  Counts log levels and detects spikes

**Saves:**
Cleaned logs to cleaned_logs.csv

Summary to log_summary.csv

Full data to logs.db (SQLite)

---
  ## 🧪 ETL Use Cases
  
This project demonstrates core data engineering skills:

Data extraction from semi-structured logs

Transformation using Python with pandas

Load into CSV and SQL databases

Anomaly detection (e.g., error bursts)

Scalable with Docker

