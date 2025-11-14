FROM python:3.10-slim

RUN apt-get update && apt-get install -y \
    wget unzip curl gnupg \
    ca-certificates chromium chromium-driver \
    && apt-get clean

ENV CHROME_BIN=/usr/bin/chromium
ENV CHROMEDRIVER_PATH=/usr/bin/chromedriver

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 10000

CMD ["gunicorn", "app:app", "--workers=1", "--threads=1", "--timeout=300", "--bind=0.0.0.0:10000"]
