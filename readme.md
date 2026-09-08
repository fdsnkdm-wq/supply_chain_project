Supply Chain ETL & Analytics Data Warehouse

An end-to-end Data Engineering project focused on supply chain data processing, Star Schema Data Warehouse (DWH) design in PostgreSQL,
and key business metrics visualization in Grafana.

Architecture

CSV Dataset ──► Python (Pandas ETL) ──► PostgreSQL DWH (Star Schema) ──► Grafana

Extract & Transform (Python / Pandas): Raw data extraction from CSV, cleaning, deduplication, surrogate key generation, and dimension modeling.

Load (SQLAlchemy / PostgreSQL): Idempotent table loading into PostgreSQL with conflict handling and old raw verification.

Analytics & Visualization (Grafana): Interactive dashboard generation via SQL queries against fact and dimension tables.

Tech Stack

Language: Python 3.10+

Libraries: Pandas, SQLAlchemy, psycopg2, python-dotenv

Database: PostgreSQL 16

Visualization: Grafana

Containerization: Docker, Docker Compose file

Data Model (Star Schema)

Fact Table
fact_order_items: Contains transactional metrics per line item (sales, discounts, profit, delivery timelines) and foreign keys (FK) referencing dimension tables.

Dimension Tables
dim_customer: Customer profiles (segments, addresses, names).

dim_product: Product catalog (categories, names, prices).

dim_geography: Geographic metadata (countries, states, markets, coordinates).

dim_shipping: Shipping modes, delivery statuses, delay risks.

dim_date: Calendar dimension (year, month, week, day of week).