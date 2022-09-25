FROM python:3.9

WORKDIR app

COPY app/requirements.txt /app/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt

COPY app /app/

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "9000", "--reload"]
