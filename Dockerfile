FROM python:3.8.0

RUN pip install --upgrade pip

RUN mkdir -p /app
WORKDIR /app

COPY ./requirements.txt /app/requirements.txt
RUN pip install -r /app/requirements.txt

COPY . /app

EXPOSE 8027

CMD ["python3", "manage.py", "runserver", "0.0.0.0:8027"]
