FROM python:3.10

ENV PYTHONUNBUFFERED=1

WORKDIR /usr/src/

COPY requirements.txt ./

COPY ./src/ ./

RUN /usr/local/bin/python -m pip install --upgrade pip && pip install -r requirements.txt --no-cache-dir

CMD [ "python", "manage.py", "runserver", "0.0.0.0:8000" ]

EXPOSE 8000
