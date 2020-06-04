#!/bin/bash

echo "$WOL_ID" | tr '\' '\n' | sed -r 's/[ ]+//g' > /etc/macs.list
chmod +x /usr/local/bin/guac_wol.py
"/usr/local/bin/guac_wol.py &
