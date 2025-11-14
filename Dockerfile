FROM python:3.10-slim

# ===== install lightweight chromium & dependencies =====
RUN apt-get update && apt-get install -y \
    chromium \
    chromium-driver \
    libglib2.0-0 \
    libnss3 \
    libgconf-2-4 \
    libfontconfig1 \
    libx11-6 \
    libx11-xcb1 \
    libxcb1 \
    libxcomposite1 \
    libxcursor1 \
    libxdamage1 \
    libxrandr2 \
    libxss1 \
    libxtst6 \
    libatk1.0-0 \
    libatk-bridge2.0-0 \
    libcups2 \
    libdrm2 \
    libxkbcommon0 \
    libpango-1.0-0 \
    libgbm1 \
    libasound2 \
    fonts-liberation \
    curl \
    unzip \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# ===== Environment variables =====
ENV CHROME_BIN=/usr/bin/chromium
ENV CHROMEDRIVER_PATH=/usr/bin/chromedriver

# ===== App setup =====
WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 10000

# ===== Optimized Gunicorn for 512MB RAM =====
CMD ["gunicorn", "app:app",
     "--workers=1",
     "--worker-class=gevent",
     "--timeout=200",
     "--bind=0.0.0.0:10000"]
