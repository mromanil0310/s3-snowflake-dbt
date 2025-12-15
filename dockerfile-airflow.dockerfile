FROM apache/airflow:2.9.1-python3.10

# Optional: install system dependencies as root (for things like pyarrow, fastparquet, etc.)
USER root
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    git \
    curl \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Switch to airflow user BEFORE running pip (required by Airflow image)
USER airflow

# Copy requirements and install Python packages as 'airflow' user
COPY requirements.txt /requirements.txt
RUN pip install --no-cache-dir -r /requirements.txt
