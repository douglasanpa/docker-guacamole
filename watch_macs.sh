#!/bin/bash
echo "id,mac" > /etc/macs.list
echo "$WOL_ID" | tr '\' '\n' | sed -r 's/[ ]+//g' >> /etc/macs.list
envsubst < /usr/local/bin/guac_wol_base.py > /usr/local/bin/guac_wol.py
chmod +x /usr/local/bin/guac_wol.py
/usr/local/bin/guac_wol.py &
