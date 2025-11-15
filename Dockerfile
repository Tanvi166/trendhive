# FROM python:3.10-slim

# ENV DEBIAN_FRONTEND=noninteractive

# # Install dependencies
# RUN apt-get update && apt-get install -y \
#     wget unzip curl gnupg ca-certificates \
#     libnss3 libxss1 libatk1.0-0 \
#     libatk-bridge2.0-0 libgtk-3-0 \
#     libx11-xcb1 libxcomposite1 libxdamage1 \
#     libxrandr2 libgbm1 libasound2 \ 
#     libpangocairo-1.0-0 libcups2 \
#     && rm -rf /var/lib/apt/lists/*

# # ---- INSTALL CHROME (Fixed version 120) ----
# RUN wget -q https://storage.googleapis.com/chrome-for-testing-public/120.0.6099.71/linux64/chrome-linux64.zip \
#     && unzip chrome-linux64.zip \
#     && mv chrome-linux64 /opt/chrome \
#     && rm chrome-linux64.zip

# # ---- INSTALL MATCHING CHROMEDRIVER ----
# RUN wget -q https://storage.googleapis.com/chrome-for-testing-public/120.0.6099.71/linux64/chromedriver-linux64.zip \
#     && unzip chromedriver-linux64.zip \
#     && mv chromedriver-linux64/chromedriver /usr/local/bin/chromedriver \
#     && chmod +x /usr/local/bin/chromedriver \
#     && rm -rf chromedriver-linux64 chromedriver-linux64.zip

# ENV CHROME_BIN=/opt/chrome/chrome
# ENV CHROMEDRIVER_PATH=/usr/local/bin/chromedriver

# WORKDIR /app
# COPY . .

# RUN pip install --upgrade pip
# RUN pip install -r requirements.txt

# EXPOSE 10000

# CMD ["gunicorn", "app:app", "--bind", "0.0.0.0:10000"]










# FROM python:3.10-slim

# ENV DEBIAN_FRONTEND=noninteractive

# # Install Firefox + dependencies
# RUN apt-get update && apt-get install -y \
#     firefox-esr \
#     wget \
#     unzip \
#     gnupg \
#     curl \
#     ca-certificates \
#     libglib2.0-0 \
#     libnss3 \
#     libatk1.0-0 \
#     libatk-bridge2.0-0 \
#     libdrm2 \
#     libxkbcommon0 \
#     libx11-xcb1 \
#     libdbus-glib-1-2 \
#     libgtk-3-0 \
#     && rm -rf /var/lib/apt/lists/*

# # Install Geckodriver
# RUN GECKO_VERSION=$(curl -s https://api.github.com/repos/mozilla/geckodriver/releases/latest | grep "tag_name" | cut -d '"' -f 4) && \
#     wget -q "https://github.com/mozilla/geckodriver/releases/download/${GECKO_VERSION}/geckodriver-${GECKO_VERSION}-linux64.tar.gz" && \
#     tar -xf geckodriver-* && \
#     mv geckodriver /usr/local/bin && \
#     chmod +x /usr/local/bin/geckodriver && \
#     rm geckodriver-*

# WORKDIR /app
# COPY . .

# RUN pip install --upgrade pip
# RUN pip install -r requirements.txt

# EXPOSE 10000

# CMD ["gunicorn", "app:app", "--bind", "0.0.0.0:10000"]









# # -----------------------------
# # 1) Use lightweight Python base
# # -----------------------------
# FROM python:3.10-slim

# # -----------------------------
# # 2) Install system dependencies
# # -----------------------------
# RUN apt-get update && apt-get install -y \
#     wget \
#     curl \
#     gnupg \
#     firefox-esr \
#     libgtk-3-0 \
#     libdbus-glib-1-2 \
#     libxt6 \
#     libxcomposite1 \
#     libxdamage1 \
#     libxfixes3 \
#     libasound2 \
#     libxrandr2 \
#     libxss1 \
#     libnss3 \
#     libglib2.0-0 \
#     libx11-xcb1 \
#     && rm -rf /var/lib/apt/lists/*

# # -----------------------------
# # 3) Install Geckodriver
# # -----------------------------
# RUN GECKO_VERSION=$(curl -s https://api.github.com/repos/mozilla/geckodriver/releases/latest \
#     | grep "tag_name" | cut -d '"' -f 4) \
#     && wget https://github.com/mozilla/geckodriver/releases/download/$GECKO_VERSION/geckodriver-$GECKO_VERSION-linux64.tar.gz \
#     && tar -xvzf geckodriver-$GECKO_VERSION-linux64.tar.gz \
#     && mv geckodriver /usr/local/bin/ \
#     && rm geckodriver-$GECKO_VERSION-linux64.tar.gz \
#     && chmod +x /usr/local/bin/geckodriver

# # -----------------------------
# # 4) Set working directory
# # -----------------------------
# WORKDIR /app

# # -----------------------------
# # 5) Copy project files
# # -----------------------------
# COPY . .

# # -----------------------------
# # 6) Install Python dependencies
# # -----------------------------
# RUN pip install --no-cache-dir -r requirements.txt

# # -----------------------------
# # 7) Expose port
# # -----------------------------
# EXPOSE 10000

# # -----------------------------
# # 8) Run the app
# # -----------------------------
# CMD ["gunicorn", "--bind", "0.0.0.0:10000", "app:app"]










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
