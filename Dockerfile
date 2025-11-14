FROM python:3.10-slim

# Install dependencies + chromium + chromedriver
RUN apt-get update && apt-get install -y \
    wget \
    unzip \
    curl \
    chromium \
    chromium-driver \
    && apt-get clean

ENV CHROME_BIN=/usr/bin/chromium
ENV CHROMEDRIVER_PATH=/usr/bin/chromedriver

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 10000

# optimized for free plan (1 worker, gevent, 200s timeout)
CMD ["gunicorn", "app:app", "--bind", "0.0.0.0:10000", "--workers=1", "--worker-class=gevent", "--timeout=200"]
