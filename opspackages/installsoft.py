# coding: utf8
from __future__ import absolute_import 
import salt.client

def mysql(hostname):
    local = salt.client.LocalClient()
 #   local.cmd(hostname,'cp.get_file',['salt://packages/mysql/files/MySQL-client-5.6.24-1.el7.x86_64.rpm','/tmp/MySQL-client-5.6.24-1.el7.x86_64.rpm','makedirs=True'])
 #   local.cmd(hostname,'cp.get_file',['salt://packages/mysql/files/MySQL-devel-5.6.24-1.el7.x86_64.rpm','/tmp/MySQL-devel-5.6.24-1.el7.x86_64.rpm','makedirs=True'])
 #   local.cmd(hostname,'cp.get_file',['salt://packages/mysql/files/MySQL-server-5.6.24-1.el7.x86_64.rpm','/tmp/MySQL-server-5.6.24-1.el7.x86_64.rpm','makedirs=True'])
 #   local.cmd(hostname,'cp.get_file',['salt://packages/mysql/files/my.cnf','/tmp/my.cnf','makedirs=True'])
    local.cmd(hostname,'cp.get_file',['salt://packages/mysql/scripts/mysql_install.sh','/root/scripts/mysql_install.sh','makedirs=True'])
    local.cmd(hostname,'cp.get_file',['salt://packages/mysql/scripts/mysql_back.sh','/root/scripts/mysql_back.sh','makedirs=True'])
    local.cmd(hostname,'cmd.run',['chmod +x /root/scripts/mysql_install.sh'])
    local.cmd(hostname,'cmd.run',['chmod +x /root/scripts/mysql_back.sh'])
    local.cmd(hostname,'cmd.run',['/root/scripts/mysql_install.sh'])
    local.cmd(hostname,'cmd.run',['rm -rf /root/scripts/mysql_install.sh'])

def fastdfs(hostname):
    local = salt.client.LocalClient()
  #  local.cmd(hostname,'cp.get_file',['salt://packages/fastdfs/files/fastdfs-nginx-module_v1.16.tar.gz','/tmp/fastdfs-nginx-module_v1.16.tar.gz','makedirs=True'])
  #  local.cmd(hostname,'cp.get_file',['salt://packages/fastdfs/files/libfastcommon-master.zip','/tmp/libfastcommon-master.zip ','makedirs=True'])
  #  local.cmd(hostname,'cp.get_file',['salt://packages/fastdfs/files/FastDFS_v5.05.tar.gz','/tmp/FastDFS_v5.05.tar.gz','makedirs=True'])
  #  local.cmd(hostname,'cp.get_file',['salt://packages/nginx/files/nginx-1.8.0.tar.gz','/tmp/nginx-1.8.0.tar.gz','makedirs=True'])
  #  local.cmd(hostname,'cp.get_file',['salt://packages/fastdfs/files/nginx.conf','/tmp/nginx.conf','makedirs=True'])
  #  local.cmd(hostname,'cp.get_file',['salt://packages/fastdfs/files/mod_fastdfs.conf','/tmp/mod_fastdfs.conf','makedirs=True'])
  #  local.cmd(hostname,'cp.get_file',['salt://packages/fastdfs/files/http.conf','/tmp/http.conf','makedirs=True'])
  #  local.cmd(hostname,'cp.get_file',['salt://packages/fastdfs/files/client.conf','/tmp/client.conf','makedirs=True'])
  #  local.cmd(hostname,'cp.get_file',['salt://packages/fastdfs/files/config','/tmp/config','makedirs=True'])
  #  local.cmd(hostname,'cp.get_file',['salt://packages/fastdfs/files/storage.conf','/tmp/storage.conf','makedirs=True'])
  #  local.cmd(hostname,'cp.get_file',['salt://packages/fastdfs/files/tracker.conf','/tmp/tracker.conf','makedirs=True'])
  #  local.cmd(hostname,'cp.get_file',['salt://packages/nginx/files/nginx_log_cut.sh','/tmp/nginx_log_cut.sh','makedirs=True'])
    local.cmd(hostname,'cp.get_file',['salt://packages/fastdfs/scripts/fastdfs_install.sh','/root/scripts/fastdfs_install.sh','makedirs=True'])
    local.cmd(hostname,'cmd.run',['chmod +x /root/scripts/fastdfs_install.sh'])
    local.cmd(hostname,'cmd.run',['/root/scripts/fastdfs_install.sh'])
    local.cmd(hostname,'cmd.run',['mv /root/scripts/fastdfs_install.sh /tmp'])

def nginx(hostname):
    local = salt.client.LocalClient()
  #  local.cmd(hostname,'cp.get_file',['salt://packages/nginx/files/nginx-1.8.0.tar.gz','/tmp/nginx-1.8.0.tar.gz','makedirs=True'])
  #  local.cmd(hostname,'cp.get_file',['salt://packages/nginx/files/nginx.conf','/tmp/nginx.conf','makedirs=True'])
  #  local.cmd(hostname,'cp.get_file',['salt://packages/nginx/files/nginx_log_cut.sh','/tmp/nginx_log_cut.sh','makedirs=True'])
    local.cmd(hostname,'cp.get_file',['salt://packages/nginx/scripts/nginx_install.sh','/root/scripts/nginx_install.sh','makedirs=True'])
    local.cmd(hostname,'cmd.run',['chmod +x /root/scripts/nginx_install.sh'])
    local.cmd(hostname,'cmd.run',['/root/scripts/nginx_install.sh'])
    local.cmd(hostname,'cmd.run',['mv /root/scripts/nginx_install.sh /tmp'])

def mongo(hostname,softversion):
    local = salt.client.LocalClient()
    if  softversion == "244":
  #  local.cmd(hostname,'cp.get_file',['salt://packages/mongo/files/mongodb-linux-x86_64-2.4.4.tgz','/tmp/mongodb-linux-x86_64-2.4.4.tgz','makedirs=True'])
       local.cmd(hostname,'cp.get_file',['salt://packages/mongo/scripts/mongo_install.sh','/root/scripts/mongo_install.sh','makedirs=True'])
       local.cmd(hostname,'cp.get_file',['salt://packages/mongo/scripts/mongo.service','/usr/lib/systemd/system/mongo.service','makedirs=True'])
       local.cmd(hostname,'cp.get_file',['salt://packages/mongo/scripts/mongo','/etc/init.d/mongo','makedirs=True'])
       local.cmd(hostname,'cmd.run',['systemctl enable mongo.service'])
       local.cmd(hostname,'cmd.run',['chmod +x /root/scripts/mongo_install.sh'])
       local.cmd(hostname,'cmd.run',['/root/scripts/mongo_install.sh'])
       local.cmd(hostname,'cmd.run',['mv /root/scripts/mongo_install.sh /tmp'])
    elif softversion == "328":
       local.cmd(hostname,'cp.get_file',['salt://packages/mongo/scripts/mongo_3.2.8_install.sh','/root/scripts/mongo_3.2.8_install.sh','makedirs=True'])
       local.cmd(hostname,'cp.get_file',['salt://packages/mongo/scripts/mongo328.service','/usr/lib/systemd/system/mongo.service','makedirs=True'])
       local.cmd(hostname,'cp.get_file',['salt://packages/mongo/scripts/mongo328','/etc/init.d/mongo','makedirs=True'])
       local.cmd(hostname,'cmd.run',['systemctl enable mongo.service'])
       local.cmd(hostname,'cmd.run',['chmod +x /root/scripts/mongo_3.2.8_install.sh'])
       local.cmd(hostname,'cmd.run',['/root/scripts/mongo_3.2.8_install.sh'])
       local.cmd(hostname,'cmd.run',['mv /root/scripts/mongo_3.2.8_install.sh /tmp'])
    else:
        print "请输入正确的版本信息"
def kafka(hostname,softversion):
    local = salt.client.LocalClient()
    print softversion
    if  softversion == "082":
           iscluster=raw_input("请选择安装的kafka是否为集群（yes/no?）:\n")
           if iscluster == "yes":
             local.cmd(hostname,'cp.get_file',['salt://packages/kafka/scripts/kafkacluster_install.sh','/root/scripts/kafkacluster_install.sh','makedirs=True'])
             local.cmd(hostname,'cp.get_file',['salt://packages/zookeeper/scripts/zookeepercluster_install.sh','/root/scripts/zookeepercluster_install.sh','makedirs=True'])
             local.cmd(hostname,'cmd.run',['chmod +x /root/scripts/zookeepercluster_install.sh'])
             local.cmd(hostname,'cmd.run',['chmod +x /root/scripts/kafkacluster_install.sh'])
             local.cmd(hostname,'cmd.run',['/root/scripts/zookeepercluster_install.sh'])
             local.cmd(hostname,'cmd.run',['/root/scripts/kafkacluster_install.sh'])
             local.cmd(hostname,'cmd.run',['mv /root/scripts/kafkacluster_install.sh /tmp'])
             print "kafka 0.8.2 安装完成"
           elif iscluster == "no":
             local.cmd(hostname,'cp.get_file',['salt://packages/kafka/scripts/kafka_install.sh','/root/scripts/kafka_install.sh','makedirs=True'])
             local.cmd(hostname,'cp.get_file',['salt://packages/zookeeper/scripts/zookeeper_install.sh','/root/scripts/zookeeper_install.sh','makedirs=True'])
             local.cmd(hostname,'cmd.run',['chmod +x /root/scripts/kafka_install.sh'])
             local.cmd(hostname,'cmd.run',['chmod +x /root/scripts/zookeeper_install.sh'])
             local.cmd(hostname,'cmd.run',['/root/scripts/kafka_install.sh'])
             local.cmd(hostname,'cmd.run',['mv /root/scripts/kafka_install.sh /tmp'])
           else:
             print "未指定单点或者集群，安装失败"
    else:
        print "请输入正确的版本信息"

def zookeeper(hostname,softversion):
    local = salt.client.LocalClient()
    print softversion
    if  softversion == "346":
           iscluster=raw_input("请选择安装的zookeeper是否为集群（yes/no?）:\n")
           if iscluster == "yes":
             local.cmd(hostname,'cp.get_file',['salt://packages/zookeeper/scripts/zookeeper_install.sh','/root/scripts/zookeeper_install.sh','makedirs=True'])
             local.cmd(hostname,'cmd.run',['chmod +x /root/scripts/zookeeper_install.sh'])
             local.cmd(hostname,'cmd.run',['/root/scripts/zookeeper_install.sh'])
             local.cmd(hostname,'cmd.run',['mv /root/scripts/zookeeper_install.sh /tmp'])
             print "zookeeper 3.4.6 安装完成"
           elif iscluster == "no":
             local.cmd(hostname,'cp.get_file',['salt://packages/zookeeper/scripts/zookeeper_install.sh','/root/scripts/zookeeper_install.sh','makedirs=True'])
             local.cmd(hostname,'cmd.run',['chmod +x /root/scripts/zookeeper_install.sh'])
             local.cmd(hostname,'cmd.run',['/root/scripts/zookeeper_install.sh'])
             local.cmd(hostname,'cmd.run',['mv /root/scripts/zookeeper_install.sh /tmp'])
           else:
             print "未指定单点或者集群，安装失败"
    else:
        print "请输入正确的版本信息"

def redis(hostname,softversion):
    local = salt.client.LocalClient()
    print softversion
    if  softversion == "305":
           iscluster=raw_input("请选择安装的redis是否为集群（yes/no?）:\n")
   #     local.cmd(hostname,'cp.get_file',['salt://packages/redis/files/redis-3.0.5.tar.gz','/tmp/redis-3.0.5.tar.gz','makedirs=True'])
           if iscluster == "yes":
             x=raw_input("请选择安装的redis是否为多台机器集群（yes/no?）:\n")
            # local.cmd(hostname,'cp.get_file',['salt://packages/redis/files/rediscluster-3.0.5.conf','/tmp/redis.conf','makedirs=True'])
             if x == "yes":
                local.cmd(hostname,'cp.get_file',['salt://packages/redis/scripts/rediscluster_3.0.5_install.sh','/root/scripts/redis_3.0.5_install.sh','makedirs=True'])
                local.cmd(hostname,'cp.get_file',['salt://packages/redis/scripts/redis.service','/usr/lib/systemd/system/redis.service','makedirs=True'])
                local.cmd(hostname,'cp.get_file',['salt://packages/redis/scripts/redis','/etc/init.d/redis','makedirs=True'])
                local.cmd(hostname,'cmd.run',['systemctl enable redis.service'])
                local.cmd(hostname,'cmd.run',['chmod +x /root/scripts/redis_3.0.5_install.sh'])
                local.cmd(hostname,'cmd.run',['/root/scripts/redis_3.0.5_install.sh'])
                local.cmd(hostname,'cmd.run',['mv /root/scripts/redis_3.0.5_install.sh /tmp'])
                print "redis 3.0.5 安装完成"
             elif x == "no":
                local.cmd(hostname,'cp.get_file',['salt://packages/redis/files/redis-3.0.5.tar.gz','/root/redis-3.0.5.tar.gz','makedirs=True'])
                local.cmd(hostname,'cp.get_file',['salt://packages/redis/files/redis-6379.conf','/root/redis-6379.conf','makedirs=True'])
                local.cmd(hostname,'cp.get_file',['salt://packages/redis/files/redis-6380.conf','/root/redis-6380.conf','makedirs=True'])
                local.cmd(hostname,'cp.get_file',['salt://packages/redis/files/redis-6381.conf','/root/redis-6381.conf','makedirs=True'])
                local.cmd(hostname,'cp.get_file',['salt://packages/redis/scripts/norediscluster_3.0.5_install.sh','/root/scripts/redis_3.0.5_install.sh','makedirs=True'])
                local.cmd(hostname,'cp.get_file',['salt://packages/redis/scripts/redis.service','/usr/lib/systemd/system/redis.service','makedirs=True'])
                local.cmd(hostname,'cp.get_file',['salt://packages/redis/scripts/redis','/etc/init.d/redis','makedirs=True'])
                local.cmd(hostname,'cmd.run',['systemctl enable redis.service'])
                local.cmd(hostname,'cmd.run',['chmod +x /root/scripts/redis_3.0.5_install.sh'])
                local.cmd(hostname,'cmd.run',['/root/scripts/redis_3.0.5_install.sh'])
                local.cmd(hostname,'cmd.run',['mv /root/scripts/redis_3.0.5_install.sh /tmp'])
                print "redis 3.0.5 安装完成"
             else:
                print "未指定单点或者集群，安装失败"
           elif iscluster == "no":
             local.cmd(hostname,'cp.get_file',['salt://packages/redis/scripts/redis_3.0.5_install.sh','/root/scripts/redis_3.0.5_install.sh','makedirs=True'])
             local.cmd(hostname,'cp.get_file',['salt://packages/redis/scripts/redis.service','/usr/lib/systemd/system/redis.service','makedirs=True'])
             local.cmd(hostname,'cp.get_file',['salt://packages/redis/scripts/redis','/etc/init.d/redis','makedirs=True'])
             local.cmd(hostname,'cmd.run',['systemctl enable redis.service'])
             local.cmd(hostname,'cmd.run',['chmod +x /root/scripts/redis_3.0.5_install.sh'])
             local.cmd(hostname,'cmd.run',['/root/scripts/redis_3.0.5_install.sh'])
             local.cmd(hostname,'cmd.run',['mv /root/scripts/redis_3.0.5_install.sh /tmp'])
           else:
             print "未指定单点或者集群，安装失败"
    elif softversion == '2614':
    #    local.cmd(hostname,'cp.get_file',['salt://packages/redis/files/redis-2.6.14.tar.gz','/tmp/redis-2.6.14.tar.gz','makedirs=True'])
        local.cmd(hostname,'cp.get_file',['salt://packages/redis/files/redis-2.6.14.conf','/tmp/redis-2.6.14.conf','makedirs=True'])
        local.cmd(hostname,'cp.get_file',['salt://packages/redis/scripts/redis_2.6.14_install.sh','/root/scripts/redis_2.6.14_install.sh','makedirs=True'])
        local.cmd(hostname,'cmd.run',['chmod +x /root/scripts/redis_2.6.14_install.sh'])
        local.cmd(hostname,'cmd.run',['/root/scripts/redis_2.6.14_install.sh'])
        local.cmd(hostname,'cmd.run',['mv /root/scripts/redis_2.6.14_install.sh /tmp'])
        print "redis 2.6.14 安装完成"
    else:
        print "请输入正确的版本信息"

def terracotta(hostname):
    local = salt.client.LocalClient()
   # local.cmd(hostname,'cp.get_file',['salt://packages/terracotta/files/terracotta-3.5.1.zip','/tmp/terracotta-3.5.1.zip','makedirs=True'])
   # local.cmd(hostname,'cp.get_file',['salt://packages/terracotta/files/terracotta-3.5.1-installer.jar','/tmp/terracotta-3.5.1-installer.jar','makedirs=True'])
   # local.cmd(hostname,'cp.get_file',['salt://packages/terracotta/files/tc-config.xml','/tmp/tc-config.xml','makedirs=True'])
    local.cmd(hostname,'cp.get_file',['salt://packages/terracotta/scripts/terracotta_install.sh','/root/scripts/terracotta_install.sh','makedirs=True'])
    local.cmd(hostname,'cmd.run',['chmod +x /root/scripts/terracotta_install.sh'])
    local.cmd(hostname,'cmd.run',['/root/scripts/terracotta_install.sh'])
    local.cmd(hostname,'cmd.run',['mv /root/scripts/terracotta_install.sh /tmp'])

def tomcat(hostname):
    local = salt.client.LocalClient()
   # local.cmd(hostname,'cp.get_file',['salt://packages/tomcat/files/apache-tomcat-7.0.14.tar.gz','/tmp/apache-tomcat-7.0.14.tar.gz','makedirs=True'])
   # local.cmd(hostname,'cp.get_file',['salt://packages/tomcat/files/catalina.sh','/tmp/catalina.sh','makedirs=True'])
   # local.cmd(hostname,'cp.get_file',['salt://packages/tomcat/files/cronolog-1.6.2.tar.gz','/tmp/cronolog-1.6.2.tar.gz','makedirs=True'])
    local.cmd(hostname,'cp.get_file',['salt://packages/tomcat/scripts/tomcat_restart.sh','/root/scripts/tomcat_restart.sh','makedirs=True'])
    local.cmd(hostname,'cp.get_file',['salt://packages/tomcat/scripts/tomcat_install.sh','/root/scripts/tomcat_install.sh','makedirs=True'])
    local.cmd(hostname,'cp.get_file',['salt://packages/tomcat/scripts/tomcat','/etc/init.d/tomcat','makedirs=True'])
    local.cmd(hostname,'cmd.run',['chmod +x /root/scripts/tomcat_install.sh'])
    local.cmd(hostname,'cp.get_file',['salt://packages/tomcat/scripts/tomcat.service','/usr/lib/systemd/system/tomcat.service','makedirs=True'])
    local.cmd(hostname,'cmd.run',['systemctl enable tomcat.service'])
    local.cmd(hostname,'cmd.run',['/root/scripts/tomcat_install.sh'])
    local.cmd(hostname,'cmd.run',['mv /root/scripts/tomcat_install.sh /tmp'])

def activemq(hostname):
    local = salt.client.LocalClient()
   # print "开始上传activemq安装文件"
   # local.cmd(hostname,'cp.get_file',['salt://packages/activemq/files/apache-activemq-5.10.0-bin.tar.gz','/tmp/apache-activemq-5.10.0-bin.tar.gz','makedirs=True'])
    print "开始上传activemq配置文件"
   # local.cmd(hostname,'cp.get_file',['salt://packages/activemq/files/activemq.xml','/tmp/activemq.xml','makedirs=True'])
    local.cmd(hostname,'cp.get_file',['salt://packages/activemq/scripts/activemq_install.sh','/root/scripts/activemq_install.sh','makedirs=True'])
    local.cmd(hostname,'cmd.run',['chmod +x /root/scripts/activemq_install.sh'])
    print "开始安装activemq"
    local.cmd(hostname,'cmd.run',['/root/scripts/activemq_install.sh'])
    local.cmd(hostname,'cmd.run',['mv /root/scripts/activemq_install.sh /tmp'])
