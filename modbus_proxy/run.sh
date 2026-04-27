#!/usr/bin/with-contenv bashio

LISTEN_PORT=$(bashio::config 'listen_port')
MODBUS_HOST=$(bashio::config 'modbus_host')
MODBUS_PORT=$(bashio::config 'modbus_port')

bashio::log.info "Starting Modbus Proxy..."
bashio::log.info "Listening on 0.0.0.0:${LISTEN_PORT}"
bashio::log.info "Forwarding to ${MODBUS_HOST}:${MODBUS_PORT}"

cat > /tmp/modbus-proxy.yml << YMLEOF
devices:
  - modbus:
      url: "${MODBUS_HOST}:${MODBUS_PORT}"
      timeout: 10
      connection_time: 1.0
    listen:
      bind: "0.0.0.0:${LISTEN_PORT}"
YMLEOF

exec modbus-proxy -c /tmp/modbus-proxy.yml
