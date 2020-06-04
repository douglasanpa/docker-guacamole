FROM oznu/guacamole:latest
COPY guac_wol.py /usr/local/bin

RUN echo "/usr/local/bin/watch_macs.sh" >> /etc/cont-init.d/30-defaults.sh && \
    chmod +x /usr/local/bin/guac_wol.py && \
    chmod +x /usr/local/bin/watch_macs.sh && \


