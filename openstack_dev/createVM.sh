#!/bin/bash

serverAuth="openstack --os-auth-url http://10.23.108.3:5000/v2.0 --os-username rnd_test --os-password clt --os-project-name rnd_test  server "
action="create "
serverName=$1
count=$2
vmArgs=" --image 'tomcat' --flavor 'm1.medium' --nic net-id='rnd_test'   --security-group 'rnd_test'"
echo $serverAuth $action $serverName $vmArgs --max $count | sh 
#> vmlog.txt
#cat vmlog.txt  | grep "| id " | awk '{print $4}'
