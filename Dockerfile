FROM python:3.10-slim

ENV DEBIAN_FRONTEND=noninteractive

# Install dependencies
RUN apt-get update && apt-get install -y \
    wget unzip curl gnupg ca-certificates \
    libnss3 libxss1 libatk1.0-0 \
    libatk-bridge2.0-0 libgtk-3-0 \
    libx11-xcb1 libxcomposite1 libxdamage1 \
    libxrandr2 libgbm1 libasound2 \ 
    libpangocairo-1.0-0 libcups2 \
    && rm -rf /var/lib/apt/lists/*

# ---- INSTALL CHROME (Fixed version 120) ----
RUN wget -q https://storage.googleapis.com/chrome-for-testing-public/120.0.6099.71/linux64/chrome-linux64.zip \
    && unzip chrome-linux64.zip \
    && mv chrome-linux64 /opt/chrome \
    && rm chrome-linux64.zip

# ---- INSTALL MATCHING CHROMEDRIVER ----
RUN wget -q https://storage.googleapis.com/chrome-for-testing-public/120.0.6099.71/linux64/chromedriver-linux64.zip \
    && unzip chromedriver-linux64.zip \
    && mv chromedriver-linux64/chromedriver /usr/local/bin/chromedriver \
    && chmod +x /usr/local/bin/chromedriver \
    && rm -rf chromedriver-linux64 chromedriver-linux64.zip

ENV CHROME_BIN=/opt/chrome/chrome
ENV CHROMEDRIVER_PATH=/usr/local/bin/chromedriver

WORKDIR /app
COPY . .

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

EXPOSE 10000

CMD ["gunicorn", "app:app", "--bind", "0.0.0.0:10000"]
