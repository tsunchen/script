sed -i -E 's/allowed_hosts=127.0.0.1,::1/allowed_hosts=162.211.229.24/'  /etc/nagios/nrpe.cfg
echo "command[check_wait_connect]=/usr/lib64/nagios/plugins/lcgdm/check_wait_connect" >> /etc/nrpe.d/lcgdm-common.cfg

