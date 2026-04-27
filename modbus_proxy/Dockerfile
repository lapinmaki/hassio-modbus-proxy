FROM ghcr.io/home-assistant/amd64-base:latest

RUN apk add --no-cache python3 py3-pip
RUN pip install modbus-proxy pyyaml --break-system-packages

COPY patch.py /patch.py
RUN python3 /patch.py

COPY run.sh /run.sh
RUN chmod +x /run.sh

CMD ["/run.sh"]
