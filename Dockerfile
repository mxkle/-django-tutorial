FROM python:3

WORKDIR /app
ADD /app/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
