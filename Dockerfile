FROM oznu/guacamole
COPY guac_wol.py /usr/local/bin

RUN echo ${WOL_ID// \/$eol} > /etc/macs.list
