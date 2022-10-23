FROM python:3.8-alpine AS venv

RUN apk --no-cache add gcc musl-dev libffi-dev g++

WORKDIR /app
RUN python -m venv --copies /app/venv
COPY requirements.txt /app/
RUN . /app/venv/bin/activate && pip install -r requirements.txt 

FROM python:3.8-alpine AS app

COPY --from=venv /app/venv /app/venv/
ENV PATH /app/venv/bin:$PATH
WORKDIR /app
COPY app.py /app

CMD ["gunicorn", "-w", "2", "-b", "0.0.0.0:5000", "app:app"]
