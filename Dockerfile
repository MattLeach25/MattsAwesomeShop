FROM python:3.10
WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install --no-cache-dir --system -r requirements.txt

COPY /MattsAwesomeShop .