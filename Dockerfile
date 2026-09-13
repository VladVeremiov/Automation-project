FROM python:3.13

WORKDIR /app

COPY . .

RUN pip install -r requirements.txt
RUN playwright install --with-deps chromium