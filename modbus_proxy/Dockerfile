FROM ghcr.io/home-assistant/amd64-base:latest

RUN apk add --no-cache python3 py3-pip
RUN pip install modbus-proxy --break-system-packages

# Patch the reply[6] IndexError bug:
# Original: uid = reply[6]
# Fixed: uid = reply[6] if len(reply) > 6 else 0
RUN sed -i \
  's/uid = reply\[6\]/uid = reply[6] if len(reply) > 6 else 0/' \
  /usr/lib/python3.12/site-packages/modbus_proxy.py

COPY run.sh /run.sh
RUN chmod +x /run.sh

CMD ["/run.sh"]
