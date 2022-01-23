FROM python:3.8-slim-buster

COPY requirements.txt .

RUN pip install -r requirements.txt

RUN pip install Pillow

COPY . .

ENTRYPOINT ["python", "app.py"]
