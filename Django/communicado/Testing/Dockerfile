FROM python:3.8-slim
WORKDIR /app
COPY . /app

RUN pip install --no-cache-dir psycopg2-binary pymysql

CMD ["python", "check_db_connection.py"]
