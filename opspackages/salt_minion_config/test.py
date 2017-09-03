#!/usr/local/python34/bin/python3.4
# coding: utf8
import os
zabbixlocalfile='/root/scripts/config_newsystem_scripts/zabbix_config/zabbix_agentd.conf'
saltminionlocalfile='/root/scripts/config_newsystem_scripts/salt_minion_config/minion'
hostname="temp"
zabbixcommand="/usr/bin/sed -i 's|Hostname=.*|Hostname=%s|' /root/scripts/config_newsystem_scripts/zabbix_config/zabbix_agentd.conf" % (hostname)
saltcommand="/usr/bin/sed -i 's|id:.*|id: %s|' /root/scripts/config_newsystem_scripts/salt_minion_config/minion" % (hostname)
os.system(zabbixcommand)
os.system(saltcommand)
