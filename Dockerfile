# Use Debian Bullseye base for better NumPy & Pandas compatibility
FROM python:3.11-bullseye

# Set working directory
WORKDIR /app

# Install system dependencies (for numpy, pandas, etc.)
RUN apt-get update && apt-get install -y \
    build-essential \
    gfortran \
    libatlas-base-dev \
    libopenblas-dev \
    liblapack-dev \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements file
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY app.py .

# Expose Flask app port
EXPOSE 4000

# Run the Flask app
CMD ["python3", "app.py"]
