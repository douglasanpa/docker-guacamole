FROM oznu/guacamole:latest
COPY guac_wol.py watch_macs.sh /usr/local/bin/

RUN echo "/usr/local/bin/watch_macs.sh" >> /etc/cont-init.d/30-defaults.sh && \
    chmod +x /usr/local/bin/guac_wol.py && \
    chmod +x /usr/local/bin/watch_macs.sh && \
    rm -rf /var/lib/apt/lists/* && \
    rm /etc/services.d/guacamole/run
COPY run /etc/services.d/guacamole/
RUN  chmod +x /etc/services.d/guacacamole/run
    


