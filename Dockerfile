FROM python:3.10-slim

# Install essential packages + Chromium + Chromedriver
RUN apt-get update && apt-get install -y \
    wget \
    unzip \
    curl \
    gnupg \
    ca-certificates \
    chromium \
    chromium-driver \
    && apt-get clean

# Set Chrome & Chromedriver paths
ENV CHROME_BIN=/usr/bin/chromium
ENV CHROMEDRIVER_PATH=/usr/bin/chromedriver

# Set working directory
WORKDIR /app

# Copy and install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the project
COPY . .

# Expose app port
EXPOSE 10000

# Run Flask using Gunicorn
CMD ["gunicorn", "app:app", "--bind", "0.0.0.0:10000"]
