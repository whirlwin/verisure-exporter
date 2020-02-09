build:
	docker build -t quay.io/whirlwin/verisure-exporter:latest ./src

example:
	docker run \
	    -e VERISURE_MYPAGES_USERNAME=<your_username (email)> \
	    -e VERISURE_MYPAGES_PASSWORD=<your_password> \
	    quay.io/whirlwin/verisure-exporter:latest

deploy:
	docker push quay.io/whirlwin/verisure-exporter:latest
