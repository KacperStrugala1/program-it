FROM python:3.11-slim

#let container to flush logs
ENV PYTHONUNBUFFERED=1

WORKDIR /app

COPY requirements.txt /app/
RUN pip install -r requirements.txt

COPY . /app/

EXPOSE 8080

CMD [ "python", "/app/programit/manage.py", "runserver", "0.0.0.0:8080" ]