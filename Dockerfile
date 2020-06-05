FROM oznu/guacamole:latest
COPY guac_wol.py watch_macs.sh /usr/local/bin/

RUN echo "/usr/local/bin/watch_macs.sh" >> /etc/cont-init.d/30-defaults.sh && \
    chmod +x /usr/local/bin/guac_wol.py && \
    chmod +x /usr/local/bin/watch_macs.sh && \
    rm /etc/services.d/guacamole/run && \
    apt-get update && apt-get -y install nano python3-venv python3-pip && \
    pip3 install wakeonlan requests && \
    rm -rf /var/lib/apt/lists/*
COPY run /etc/services.d/guacamole/
RUN  chmod +x /etc/services.d/guacamole/run
    


