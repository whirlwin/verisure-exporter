# verisure-exporter

----

Prometheus exporter for Verisure.

Based on [persandstrom/python-verisure](https://github.com/persandstrom/python-verisure) to obtain Verisure data.

## Usage

Start the container using Docker:
```bash
docker run \
    -e VERISURE_MYPAGES_USERNAME=<your_username (email)> \
    -e VERISURE_MYPAGES_PASSWORD=<your_password> \
    quay.io/whirlwin/verisure-exporter:latest
```

### Configuration

Configuration is done mainly through environment variables.


| Environment variable       | Required | Default | Description                |
|----------------------------|----------|---------|----------------------------|
| VERISURE_MY_PAGES_USERNAME | Yes      |         | Verisure My Pages username |
| VERISURE_MY_PAGES_PASSWORD | Yes      |         | Verisure My Pages password |
| HTTP_PORT                  | No       | 8000    | Exporter HTTP port         |
