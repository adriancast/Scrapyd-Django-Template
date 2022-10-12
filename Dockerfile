FROM python:3.11.0-stretch
WORKDIR /app
COPY . .
RUN pip install -r requirements.txt