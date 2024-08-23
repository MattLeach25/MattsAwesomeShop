FROM python:3.10

RUN mkdir /code

COPY . /code/

WORKDIR /code/

RUN pip install -r requirements.txt
CMD ls
CMD python /MattsAwesomeShop/manage.py runserver 0.0.0.0:8000
