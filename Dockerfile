FROM python:3.7

WORKDIR /code

COPY requirements.txt /code/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

COPY app ./app
COPY models ./models

# CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]
CMD ["python", "app/app.py"]