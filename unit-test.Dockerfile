FROM python:3.9-buster

WORKDIR /usr/local/src

# todo optimize layers count
COPY bin bin
COPY lib lib
COPY tests tests
#COPY requirements.txt .
COPY unit-test.requirements.txt .
#RUN pip install -r requirements.txt
RUN pip install -r unit-test.requirements.txt

ENV PYTHONPATH=/usr/local/src/bin:/usr/local/src/lib:/usr/local/src/tests
CMD python3 -m pytest --capture=no
