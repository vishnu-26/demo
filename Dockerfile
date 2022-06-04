FROM python:3-alpine
ENV PYTHONUNBUFFERED 1
WORKDIR /code

COPY requirements.txt /code/requirements.txt
RUN pip3 install -r requirements.txt
COPY . .

EXPOSE 8000
#RUN python3 manage.py runserver 0.0.0.0:8000

CMD ["gunicorn", "--bind", ":8000","django_redis.wsgi"]
