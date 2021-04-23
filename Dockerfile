#FROM python:3
RUN mkdir /code
WORKDIR /code
COPY . /code/
CMD python manage.py migrate && python manage.py runserver 0.0.0.0:6007
EXPOSE  6007








