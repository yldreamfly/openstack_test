# -*- coding: utf8 -*-
#from __future__ import absolute_import
import paramiko

def command(ip,cmd):
    username='root'
    password='car@clt'
    port = 22
    hostname=ip
    try:
      ssh=paramiko.SSHClient()
      ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
      ssh.connect(hostname=hostname,username=username,password=password)
      stdin,stdout,stderr=ssh.exec_command(cmd,timeout=5)
      print hostname,stdout.readlines()
      ssh.close()
    except Exception,e:
      print ip,"not connect"
      error_ip=ip
