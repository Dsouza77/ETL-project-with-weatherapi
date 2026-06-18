# 🌦️ ETL Project with weatherapi.com 🌦️

A robust data engineering pipeline (ETL) designed for real-time climate data extraction, advanced transformation, and hybrid persistence using a PostgreSQL database and local backup files.

---

## 📝 Description

**ETL Project with weatherapi.com** is a Python-based data engineering pipeline that consumes real-time meteorological data from the **WeatherAPI** platform. The core philosophy of this project builds on the principle that *"Transformation is not moving data. Transformation is adding value to data."*

To achieve this, the pipeline cleans, standardizes, and enriches raw API payloads before loading them. The system implements a resilient persistence workflow: first, the enriched data is appended to a local CSV file as an absolute backup priority; if and only if this step succeeds, the data is ingested into a relational **PostgreSQL** database using the **Psycopg2** driver.

---

## 🗃️ Pipeline Architecture (ETL)

### 1. Extract
Captures comprehensive real-time weather metrics via HTTP requests to the WeatherAPI, mapping the following data points:
* **Location:** City name and State/Region.
* **Current Conditions:** Climate description, condition numerical code, temperature (°C), feels-like temperature, and dew point (°C).
* **Wind Dynamics:** Wind speed (km/h) and wind gust speed (km/h).
* **Atmospheric Metrics:** Relative humidity (%), atmospheric pressure (mb), cloud cover (%), and UV index.
* **Precipitation:** Accumulated rain volume (mm) and percent chance of rain.

### 2. Transform
The stage where real value is added to raw data through rigorous engineering rules:
* **Time Correction:** Since the timestamp returned by WeatherAPI often introduces inconsistencies due to provider processing lags, the pipeline natively captures and aggregates the real-time execution clock synced with the `America/Sao_Paulo` timezone (via `datetime`), preserving both sources for auditing.
* **Climate Score Engineering:** Custom attribute engineering to calculate environmental quality metrics.
* **Data Sanitization:** Null value handling and strict type casting (converting string inputs into structured `int` or `float` types).
* **Mathematical Standardization:** Formatting all floating-point metrics strictly to a maximum of 2 decimal places.

### 3. Load
Data persistence follows a high-availability business rule managed by a central orchestrator (`config_load.py`):
1. **Top Priority (Backup):** Enriched records are appended to a local CSV file (`data_backup.csv`).
2. **Transaction Safeguard:** If any failure occurs during the CSV write operation, the pipeline aborts immediately to prevent data desynchronization between targets.
3. **Database Ingestion:** Upon successful CSV backup, the pipeline opens a secure transaction via **Psycopg2** and inserts the structured records into the **PostgreSQL** database.

---

## 💻 Technologies & Libraries

- **Python 3.10+**
- **PostgreSQL** — Main relational database.
- **Library:** `psycopg2` — Native PostgreSQL adapter for safe query execution.
- **Library:** `pandas` — Data manipulation, structuring, and CSV backup generation.
- **Library:** `requests` — Consuming the WeatherAPI RESTful endpoints.
- **Library:** `datetime` — Timezone synchronization and execution clock anchoring (`America/Sao_Paulo`).
- **Library:** `os` & `time` — Filesystem path routing and execution interval pacing.

---

## 🚀 Project Structure

```text
├── .gitignore               # Files and credential modules hidden from Git
├── .venv/                   # Python Virtual Environment
├── api.py                   # Secure storage for API keys and database credentials
├── extract.py               # Module handling WeatherAPI connections and data ingestion
├── transform.py             # Data engineering core (cleaning, score calculation, time sync)
├── load_csv.py              # Script dedicated to writing and validating the backup CSV
├── load_postgresql.py       # Script managing PostgreSQL connections and Psycopg2 inserts
├── config_load.py           # Pipeline Orchestrator (Enforces: CSV Backup First -> PostgreSQL)
├── data_backup.csv          # Physical CSV backup generated automatically by the pipeline
└── planning.txt             # Internal project scope and roadmap documentation
