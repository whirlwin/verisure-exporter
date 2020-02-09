import logging
import os
import time
import verisure

from prometheus_client import start_http_server

from devices import temperature_gauge

HTTP_PORT = os.getenv('HTTP_PORT', 8000)
VERISURE_MYPAGES_USERNAME = os.environ['VERISURE_MYPAGES_USERNAME']
VERISURE_MYPAGES_PASSWORD = os.environ['VERISURE_MYPAGES_PASSWORD']

logging.basicConfig(level=logging.INFO, format='%(levelname)s: %(asctime)s - %(message)s')

session = verisure.Session(VERISURE_MYPAGES_USERNAME, VERISURE_MYPAGES_PASSWORD)
session.login()
logging.info('Successful Verisure My Pages authentication')

temperature_gauge.measure_temperature(session)

session.logout()

start_http_server(HTTP_PORT)
logging.info(f'Serving metrics at port {HTTP_PORT}')

while True:
    time.sleep(1)
