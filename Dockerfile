FROM python:3.10

RUN mkdir /code

COPY . /code/

WORKDIR /code/

RUN pip install -r requirements.txt
WORKDIR /code/MattsAwesomeShop/
CMD ls
CMD python manage.py runserver 0.0.0.0:8000
