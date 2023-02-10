FROM python:3.9-buster

WORKDIR /usr/local/src

# todo optimize layers count
COPY bin bin
COPY lib lib
COPY requirements.txt .
RUN pip install -r requirements.txt

ENV PYTHONPATH=/usr/local/src/bin:/usr/local/src/lib

CMD ["uvicorn", "wsgi:app", "--host=0.0.0.0", "--port=8000"]
