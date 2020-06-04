#!/bin/bash
echo "id,mac" > /etc/macs.list
echo "$WOL_ID" | tr '\' '\n' | sed -r 's/[ ]+//g' >> /etc/macs.list
/usr/local/bin/guac_wol.py &
