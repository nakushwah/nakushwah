FROM python:3.6

ENV PYTHONUNBUFFERED=1

WORKDIR /usr/src/app


COPY requirements.txt ./
COPY . .

RUN pip install -r requirements.txt
RUN python3 manage.py makemigrations
RUN python3 manage.py migrate

#CMD python ./manage.py runserver

