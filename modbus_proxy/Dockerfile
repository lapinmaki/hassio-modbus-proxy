FROM ghcr.io/home-assistant/amd64-base:latest

RUN apk add --no-cache python3 py3-pip
RUN pip install modbus-proxy --break-system-packages

# Find and patch the file regardless of python version path
RUN find / -name "modbus_proxy.py" 2>/dev/null | head -5
RUN PROXY_FILE=$(find / -name "modbus_proxy.py" 2>/dev/null | head -1) && \
    echo "Patching: $PROXY_FILE" && \
    sed -i 's/uid = reply\[6\]/uid = reply[6] if len(reply) > 6 else 0/' "$PROXY_FILE" && \
    echo "Patch applied" && \
    grep "uid = reply" "$PROXY_FILE"

COPY run.sh /run.sh
RUN chmod +x /run.sh

CMD ["/run.sh"]
