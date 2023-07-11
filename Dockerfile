FROM python:3.8-slim-buster

WORKDIR /root/.u2net/

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

RUN pip install gdown
RUN pip install --upgrade --no-cache-dir gdown
RUN gdown --fuzzy 'https://drive.google.com/file/d/1-02zGziSL3FnBwn-1OiTFhAMB_78K0gB/view?usp=sharing'

EXPOSE 5000

CMD ["python3", "wsgi.py"]
