# -*- coding: utf8 -*-
#from __future__ import absolute_import
import os

def ftp_files(ip,local_dir,remote_dir,ftp_sfile,ftp_dfile):
    import paramiko
    import datetime
    username='car@root'
    password='clt'
    port = 22
    hostname=ip
    t=paramiko.Transport((hostname,port))
    t.connect(username=username, password=password)
    sftp = paramiko.SFTPClient.from_transport(t)
    sftp.put(os.path.join(local_dir,ftp_sfile),os.path.join(remote_dir,ftp_dfile))
    t.close
