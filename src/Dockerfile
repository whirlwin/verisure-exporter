FROM python:alpine3.11

ENV VERISURE_EXPORTER_PATH=/opt/verisure-exporter

WORKDIR $VERISURE_EXPORTER_PATH

COPY requirements.txt $VERISURE_EXPORTER_PATH
RUN pip install -r requirements.txt

COPY . $VERISURE_EXPORTER_PATH

CMD ["python", "main.py"]