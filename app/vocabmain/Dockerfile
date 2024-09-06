FROM python:3.10

WORKDIR /app

COPY ./requirements.txt /app/requirements.txt

RUN pip install --upgrade --no-cache-dir -r /app/requirements.txt

COPY /vocabdev /app/vocabdev

COPY ./manage.py /app/manage.py

VOLUME /app/db

COPY /db /app/db

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]


