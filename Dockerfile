FROM python:3.10-slim

ENV DEBIAN_FRONTEND=noninteractive

# Install essential Chrome dependencies
RUN apt-get update && apt-get install -y \
    wget unzip gnupg curl ca-certificates \
    libnss3 libgconf-2-4 libxss1 libappindicator3-1 \
    libgbm-dev libasound2 libxrandr2 libc6 libgcc1 \
    libatk1.0-0 libatk-bridge2.0-0 libgtk-3-0 \
    libxcomposite1 libxdamage1 libxfixes3 libx11-xcb1 \
    && rm -rf /var/lib/apt/lists/*

# Install Google Chrome stable
RUN wget -q https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb \
    && apt-get install -y ./google-chrome-stable_current_amd64.deb || true \
    && rm google-chrome-stable_current_amd64.deb

# Install ChromeDriver matching Chrome version
RUN CHROME_VERSION=$(google-chrome --version | sed 's/Google Chrome //') \
    && CHROME_VERSION_MAIN=$(echo $CHROME_VERSION | cut -d '.' -f 1) \
    && wget -q -O /tmp/chromedriver.zip "https://chromedriver.storage.googleapis.com/LATEST_RELEASE_$CHROME_VERSION_MAIN" || true \
    && unzip -o /tmp/chromedriver.zip -d /usr/local/bin/ \
    && chmod +x /usr/local/bin/chromedriver \
    && rm /tmp/chromedriver.zip

ENV CHROME_BIN=/usr/bin/google-chrome
ENV CHROMEDRIVER_PATH=/usr/local/bin/chromedriver

WORKDIR /app
COPY . .

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

EXPOSE 10000

CMD ["gunicorn", "app:app", "--bind", "0.0.0.0:10000"]
