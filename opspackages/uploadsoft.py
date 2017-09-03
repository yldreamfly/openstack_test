# coding: utf8
from __future__ import absolute_import
import salt.client


def soft(softname):
    from os import walk
    mypath="/srv/salt/packages/%s/files" % (softname)
    f = []
    for (dirpath,dirnames,filenames) in walk(mypath):
      f.extend(filenames)
      for fastdfsfiles in f:
          print fastdfsfiles
    return f

def upinstallfile(ip,softname):
    import paramiko
    import datetime,os
    username='root'
    password='car@clt'
    port = 22
    hostname=ip
    t=paramiko.Transport((hostname,port))
    t.connect(username=username, password=password)
    sftp = paramiko.SFTPClient.from_transport(t)
    if softname == "activemq":
       files=soft(softname)
       for f in files:
         sftp.put(os.path.join('/srv/salt/packages/activemq/files/',f),os.path.join('/tmp/',f))
    elif softname == "mysql":    
       files=soft(softname)
       for f in files:
         sftp.put(os.path.join('/srv/salt/packages/mysql/files/',f),os.path.join('/tmp/',f))
       #sftp.put(os.path.join('/srv/salt/packages/mysql/files/','MySQL-client-5.6.24-1.el7.x86_64.rpm'),os.path.join('/tmp/','MySQL-client-5.6.24-1.el7.x86_64.rpm'))
       #sftp.put(os.path.join('/srv/salt/packages/mysql/files/','MySQL-devel-5.6.24-1.el7.x86_64.rpm'),os.path.join('/tmp/','MySQL-devel-5.6.24-1.el7.x86_64.rpm'))
       #sftp.put(os.path.join('/srv/salt/packages/mysql/files/','MySQL-server-5.6.24-1.el7.x86_64.rpm'),os.path.join('/tmp/','MySQL-server-5.6.24-1.el7.x86_64.rpm'))
       #sftp.put(os.path.join('/srv/salt/packages/mysql/files/','my.cnf'),os.path.join('/tmp/','my.cnf'))
       sftp.put(os.path.join('/srv/salt/packages/mysql/scripts','mysql_install.sh'),os.path.join('/root/scripts/','mysql_install.sh'))
    elif softname == "fastdfs":    
       files=soft(softname)
       for f in files:
         sftp.put(os.path.join('/srv/salt/packages/fastdfs/files/',f),os.path.join('/tmp/',f))
       #sftp.put(os.path.join('/srv/salt/packages/fastdfs/files/','fastdfs/files/fastdfs-nginx-module_v1.16.tar.gz'),os.path.join('/tmp/','fastdfs/files/fastdfs-nginx-module_v1.16.tar.gz'))
       #sftp.put(os.path.join('/srv/salt/packages/fastdfs/files/','libfastcommon-master.zip'),os.path.join('/tmp/','libfastcommon-master.zip'))
       #sftp.put(os.path.join('/srv/salt/packages/fastdfs/files/','FastDFS_v5.05.tar.gz'),os.path.join('/tmp/','FastDFS_v5.05.tar.gz'))
       #  sftp.put(os.path.join('/srv/salt/packages/nginx/files/',f),os.path.join('/tmp/',f))
       sftp.put(os.path.join('/srv/salt/packages/nginx/files/','nginx.conf'),os.path.join('/tmp/','nginx.conf'))
       sftp.put(os.path.join('/srv/salt/packages/nginx/files/','nginx_log_cut.sh'),os.path.join('/tmp/','nginx_log_cut.sh'))
       sftp.put(os.path.join('/srv/salt/packages/nginx/files/','nginx-1.8.0.tar.gz'),os.path.join('/tmp/','nginx-1.8.0.tar.gz'))
 
    elif softname == "nginx":    
       sftp.put(os.path.join('/srv/salt/packages/nginx/files/','nginx-1.8.0.tar.gz'),os.path.join('/tmp/','nginx-1.8.0.tar.gz'))
    elif softname == "mongo":    
       sftp.put(os.path.join('/srv/salt/packages/mongo/files/','mongodb-linux-x86_64-2.4.4.tgz'),os.path.join('/tmp/','mongodb-linux-x86_64-2.4.4.tgz'))
    elif softname == "redis":    
       sftp.put(os.path.join('/srv/salt/packages/redis/files/','redis-3.0.5.tar.gz'),os.path.join('/tmp/','redis-3.0.5.tar.gz'))
       sftp.put(os.path.join('/srv/salt/packages/redis/files/','redis-2.6.14.tar.gz'),os.path.join('/tmp/','redis-2.6.14.tar.gz'))
    elif softname == "terracotta":
       sftp.put(os.path.join('/srv/salt/packages/terracotta/files/','terracotta-3.5.1.zip'),os.path.join('/tmp/','terracotta-3.5.1.zip'))
       sftp.put(os.path.join('/srv/salt/packages/terracotta/files/','terracotta-3.5.1-installer.jar'),os.path.join('/tmp/','terracotta-3.5.1-installer.jar'))
    elif softname == "tomcat":
       sftp.put(os.path.join('/srv/salt/packages/tomcat/files/','apache-tomcat-7.0.14.tar.gz'),os.path.join('/tmp/','apache-tomcat-7.0.14.tar.gz'))
    elif softname == "kafka":
       sftp.put(os.path.join('/srv/salt/packages/kafka/files/','kafka_2.9.1-0.8.2.1.tar.gz'),os.path.join('/tmp/','kafka_2.9.1-0.8.2.1.tar.gz'))
       sftp.put(os.path.join('/srv/salt/packages/zookeeper/files/','zookeeper-3.4.6.tar.gz'),os.path.join('/tmp/','zookeeper-3.4.6.tar.gz'))
    else:
       print "请输入上传软件的正确格式"
    #ssh=paramiko.SSHClient()
    #ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    #ssh.load_system_host_keys()
    #ssh.connect(hostname=hostname,username=username,password=password)
    #command='hostnamectl set-hostname %s' % host
    #stdin,stdout,stderr=ssh.exec_command(command)
    #print stdout.read()
    #ssh.close()
    t.close()
