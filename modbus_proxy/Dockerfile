FROM ghcr.io/home-assistant/amd64-base:latest

RUN apk add --no-cache python3 py3-pip
RUN pip install "git+https://github.com/tiagocoutinho/modbus-proxy.git" --break-system-packages

COPY run.sh /run.sh
RUN chmod +x /run.sh

CMD ["/run.sh"]
