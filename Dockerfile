FROM python:3.13.0-alpine3.20

WORKDIR /app

RUN apk update && \
    apk add --no-cache gcc musl-dev mariadb-connector-c-dev pkgconfig

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

WORKDIR /app/littlelemon

EXPOSE 8000

CMD [ "python", "manage.py", "runserver", "0.0.0.0:8000" ]
