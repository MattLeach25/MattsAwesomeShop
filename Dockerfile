FROM python:3.11-slim
ENV PORT 8000
EXPOSE 8000
WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY /MattsAwesomeShop .

ENTRYPOINT ["python"]
CMD ["manage.py runserver"]