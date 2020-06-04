FROM oznu/guacamole
COPY guac_wol.py /usr/local/bin

RUN echo "/usr/local/bin/watch_macs.sh" >>
