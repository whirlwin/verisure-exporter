import logging

from prometheus_client import Gauge


def measure_temperature(session):
    try:
        overview = session.get_overview()
        climate_values = overview['climateValues']
        climate_values_with_temperatures = list(filter(lambda cv: 'temperature' in cv, climate_values))
        temperature_gauge = Gauge('verisure_temperature',
                                  'The current temprature registered by devices',
                                  ['device_label', 'device_type', 'device_area'])
        for cvwt in climate_values_with_temperatures:
            try:
                temperature_gauge.labels(device_label=cvwt['deviceLabel'],
                                         device_type=cvwt['deviceType'],
                                         device_area=cvwt['deviceArea']).set(cvwt['temperature'])
            except KeyError:
                logging.info("Unable to get device properties", exc_info=True)
                pass
    except KeyError:
        logging.info("Unable to get climate data", exc_info=True)
        pass
