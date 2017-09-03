#!/bin/bash

serverAuth="openstack --os-auth-url http://10.23.108.3:5000/v2.0 --os-username rnd_test --os-password clt --os-project-name rnd_test  server "
action="list "
servername=$1
echo $serverAuth $action | sh | grep -w "$servername" | awk '{print $8}' | cut -d "=" -f2

