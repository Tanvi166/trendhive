FROM python:3.10

# -------------------------
# Install Google Chrome
# -------------------------
RUN apt-get update && apt-get install -y wget gnupg2 curl unzip

RUN wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add -
RUN echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" \
    > /etc/apt/sources.list.d/google-chrome.list

RUN apt-get update && apt-get install -y google-chrome-stable

# -------------------------
# Install ChromeDriver (matching Chrome version)
# -------------------------
RUN CHROME_VERSION=$(google-chrome-stable --version | awk '{print $3}' | sed 's/\.[0-9]*$//') \
    && echo "Chrome Version: $CHROME_VERSION" \
    && wget -O /tmp/chromedriver.zip \
       https://chromedriver.storage.googleapis.com/$CHROME_VERSION/chromedriver_linux64.zip || true

RUN unzip /tmp/chromedriver.zip -d /usr/local/bin/ || true
RUN chmod +x /usr/local/bin/chromedriver || true

# -------------------------
# Install Python dependencies
# -------------------------
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# -------------------------
# Copy project files
# -------------------------
COPY . .

# -------------------------
# Expose port for Gunicorn
# -------------------------
EXPOSE 10000

# -------------------------
# Start the Flask app using Gunicorn
# -------------------------
CMD ["gunicorn", "-b", "0.0.0.0:10000", "app:app"]
