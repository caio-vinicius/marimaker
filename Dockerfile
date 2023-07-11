FROM python:3.8-slim-buster

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

EXPOSE 5000

CMD ["python3", "wsgi.py"]
