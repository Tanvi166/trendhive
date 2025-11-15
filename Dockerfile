FROM python:3.10-slim

<<<<<<< HEAD
=======
ENV DEBIAN_FRONTEND=noninteractive

# Install Chrome dependencies
RUN apt-get update && apt-get install -y \
    wget unzip gnupg curl ca-certificates \
    libnss3 libxss1 libappindicator3-1 libatk1.0-0 \
    libatk-bridge2.0-0 libgtk-3-0 libx11-xcb1 \
    libxcomposite1 libxdamage1 libxrandr2 \
    libgbm1 libasound2 libpangocairo-1.0-0 \
    libcups2 libxfixes3 libpango-1.0-0 libxshmfence1 \
    && rm -rf /var/lib/apt/lists/*

# Install Chrome stable
RUN wget -q https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb \
    && apt-get install -y ./google-chrome-stable_current_amd64.deb || true \
    && rm google-chrome-stable_current_amd64.deb

# Install matching ChromeDriver
RUN CHROME_VERSION=$(google-chrome --version | sed 's/Google Chrome //') \
    && CHROME_VERSION_MAIN=$(echo $CHROME_VERSION | cut -d '.' -f 1) \
    && wget -q -O /tmp/chromedriver.zip "https://chromedriver.storage.googleapis.com/LATEST_RELEASE_$CHROME_VERSION_MAIN" || true \
    && unzip -o /tmp/chromedriver.zip -d /usr/local/bin/ \
    && chmod +x /usr/local/bin/chromedriver \
    && rm /tmp/chromedriver.zip

ENV CHROME_BIN=/usr/bin/google-chrome
ENV CHROMEDRIVER_PATH=/usr/local/bin/chromedriver

>>>>>>> 5b84689855316a5e90d647614d54f3125ae1b38c
WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 10000

CMD ["gunicorn", "app:app", "--bind", "0.0.0.0:10000"]
