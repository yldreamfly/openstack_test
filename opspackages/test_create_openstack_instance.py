#!/usr/bin/env python
# coding: utf8
import os,subprocess
import urllib

from multiprocessing import Pool

import time
import multiprocessing

import logging
import logging.config
import sys,datetime
import xml.etree.ElementTree as etree

import nmap

#import sys,urllib2
import logging.handlers
from ftplib import FTP

import time
import commands

import salt.client

nowtime=datetime.datetime.now()
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

handler = logging.FileHandler('/root/scripts/config_newsystem_scripts/initsystem.log')
handler.setLevel(logging.INFO)



def initsalt(ip):
   import remote.command
   x="rm -rf /etc/salt/pki"
   remote.command.command(ip,x)
   command='/usr/bin/salt-key -d %s -y' % ip
   os.system(command)
   y="systemctl restart salt-minion.service"
   remote.command.command(ip,y)
   time.sleep(10)

def authkey(hostname):
   command='/usr/bin/salt-key -a %s -y' % hostname
   os.system(command)
   time.sleep(10)
   try:
     counter=0
     while (counter < 10):
        local = salt.client.LocalClient()
        output = local.cmd(hostname,'test.ping')
        print output
        authresult = output[hostname]
        if authresult == True:
           print "认证完成！"
           break
        else:
           print "认证客户端无法连接！"
           counter==counter+1
           print "尝试再次连接客户端！"
           if counter == 2:
              print "尝试三次连接失败，请排查salt客户端是否配置正确！"
   except Exception,e:
          print Exception,":",e,"网络异常，获取不到客户端信息!! \n 请重新删除saltmaster服务器客户端认证,重启salt-minion客户端，并重新执行此脚本！！"
          os._exit(0)


def get_project(): 
    import MySQLdb 
    db = MySQLdb.connect(host='10.23.101.251',user='root',passwd='clt',port=3306,charset='utf8') 
    cur = db.cursor() 
    query = "SELECT id,projectid_name,projectid_shortname FROM dafmanager.OPS_PROJECT;" 
    cur.execute(query)   
    rows=cur.fetchall() 
    print "##################以下为目前存在的项目以及英文缩写####################" 
    for row in rows: 
       project_id = row[0] 
       project = row[1] 
       projectid_shortname = row[2] 
       fmt = '%-3s%-20s%-20s' 
       print fmt % (project_id,projectid_shortname,project) 
    cur.close() 
    db.close() 
 
def select_project(id): 
    import MySQLdb 
    db = MySQLdb.connect(host='10.23.101.251',user='root',passwd='clt',port=3306,charset='utf8') 
    cur = db.cursor() 
    query = "SELECT projectid_shortname FROM dafmanager.OPS_PROJECT where id = %s; " % id 
    cur.execute(query) 
    rows=cur.fetchall() 
    for row in rows: 
       project_name=row[0] 
    cur.close() 
    db.close() 
    return  project_name 

def get_env():
    import MySQLdb
    db = MySQLdb.connect(host='10.23.101.251',user='root',passwd='clt',port=3306,charset='utf8')
    cur = db.cursor()
    query = "SELECT ID,EVNTYPE,EVNDESCRIBE FROM dafmanager.HOST_EVN_TYPE;"
    cur.execute(query)
    rows=cur.fetchall()
    print  "##################以下为目前所存在环境####################"
    for row in rows:
       env_id = row[0]
       env = row[1]
       envdescribe = row[2]
       fmt = '%-3s%-10s%-10s'
       print fmt % (env_id,env,envdescribe)
    cur.close()
    db.close()

def select_env(env_id):
    import MySQLdb
    db = MySQLdb.connect(host='10.23.101.251',user='root',passwd='clt',port=3306,charset='utf8')
    cur = db.cursor()
    query = "SELECT EVNTYPE FROM dafmanager.HOST_EVN_TYPE where ID = %s;" % env_id
    cur.execute(query)
    rows=cur.fetchall()
    for row in rows:
       env = row[0]
    cur.close()
    db.close()
    return env

def get_soft():
    import MySQLdb
    db = MySQLdb.connect(host='10.23.101.251',user='root',passwd='clt',port=3306,charset='utf8')
    cur = db.cursor()
    query = "SELECT SOFTWARE_ID,SOFTWARE_NAME from dafmanager.INSTALL_SOFT"
    cur.execute(query)
    rows=cur.fetchall()
    print  "##################以下为目前所存在软件####################"
    for row in rows:
       soft_id = row[0]
       soft_name = row[1]
       fmt = '%-3s%-5s'
       print fmt % (soft_id,soft_name)
    cur.close()
    db.close()

def select_soft(soft_id):
    import MySQLdb
    db = MySQLdb.connect(host='10.23.101.251',user='root',passwd='clt',port=3306,charset='utf8')
    cur = db.cursor()
    query = "SELECT SOFTWARE_NAME from dafmanager.INSTALL_SOFT where SOFTWARE_ID = '%s'" % (soft_id)
    cur.execute(query)
    rows=cur.fetchall()
    for row in rows:
       soft_name = row[0]
    cur.close()
    db.close()
    return soft_name

def get_soft_id(softname):
    import MySQLdb
    db = MySQLdb.connect(host='10.23.101.251',user='root',passwd='clt',port=3306,charset='utf8')
    cur = db.cursor()
    query = "SELECT SOFTWARE_ID from dafmanager.INSTALL_SOFT where SOFTWARE_NAME = '%s'" % (softname)
    cur.execute(query)
    rows=cur.fetchall()
    for row in rows:
       software_id = row[0]
    cur.close()
    db.close()
    return software_id

def os_command(ip,x):
    import remote.command
    remote.command.command(ip,x)

def post_cmdb(ip,hostname):
    import httplib
    import urllib
    import urllib2
    import json

    conn = httplib.HTTPConnection("10.23.105.180",8080)
    headers = {"Content-type":"application/json"}
    param = ({"ip":ip,"hostName":hostname})
    conn.request("POST" ,"/dafmanager-web/ws/0.1/host/add/info",json.JSONEncoder().encode(param), headers)
    response = conn.getresponse()
    data = response.read(200000)
    print (data)
    conn.close()

def  create_kvm(count,instancename):
     (status,output) = commands.getstatusoutput('/root/scripts/config_newsystem_scripts/openstack_dev/createVM.sh %s %s' % (instancename,str(count)))
   #  id=output
    # print id
    # time.sleep(20)
     #return id

def  modify_kvmname(instancename,hostname):
     (status,output) = commands.getstatusoutput('/root/scripts/config_newsystem_scripts/openstack_dev/modifyVM.sh  %s %s' % (hostname,instancename))
   #  os.system(command)

def  get_kvm_ip(instancename):
     print "获取",instancename,"ip 地址"
     (status,output) = commands.getstatusoutput('/root/scripts/config_newsystem_scripts/openstack_dev/getVmIp.sh %s' % instancename)
     ip=output
     print ip
     return ip

def upconfigfile(ip,hostname,process_id):
    import paramiko
    import datetime
    username='root'
    password='car@clt'
    port = 22
    host=hostname
    zabbixcopy="cp /root/scripts/config_newsystem_scripts/zabbix_config/zabbix_agentd.conf /root/scripts/config_newsystem_scripts/zabbix_config/zabbix_agentd_%s.conf" % str(process_id)
    saltcopy="cp /root/scripts/config_newsystem_scripts/salt_minion_config/minion /root/scripts/config_newsystem_scripts/salt_minion_config/minion_%s" % str(process_id)
    os.system(zabbixcopy)
    os.system(saltcopy)
    zabbixcommand="/usr/bin/sed -i 's|Hostname=.*|Hostname=%s|' /root/scripts/config_newsystem_scripts/zabbix_config/zabbix_agentd_%s.conf" % (hostname,str(process_id))
    saltcommand="/usr/bin/sed -i 's|id:.*|id: %s|' /root/scripts/config_newsystem_scripts/salt_minion_config/minion_%s" % (hostname,str(process_id))
    os.system(zabbixcommand)
    os.system(saltcommand)
    hostname=ip
    t=paramiko.Transport((hostname,port))
    t.connect(username=username, password=password)
    sftp = paramiko.SFTPClient.from_transport(t)
    print '#########################################'
    print '开始上传机器初始化配置文件到%s, %s ' % (hostname,datetime.datetime.now())
    sftp.put(os.path.join('/root/scripts/config_newsystem_scripts/files/','resolv.conf'),os.path.join('/etc/','resolv.conf'))
    print '开始上传zabbix配置文件'
    zfilename="zabbix_agentd_" + str(process_id) + ".conf"
    sftp.put(os.path.join('/root/scripts/config_newsystem_scripts/zabbix_config/',zfilename),os.path.join('/etc/zabbix/','zabbix_agentd.conf'))
    print '开始上传salt配置文件'
    sfilename="minion_" + str(process_id)
    sftp.put(os.path.join('/root/scripts/config_newsystem_scripts/salt_minion_config/',sfilename),os.path.join('/etc/salt/','minion'))
    print 'Uploading file success %s ' % datetime.datetime.now()
    print ''
    print '#########################################'
    paramiko.util.log_to_file('./paramiko.log')
    ssh=paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    #ssh.load_system_host_keys()
    ssh.connect(hostname=hostname,username=username,password=password)
    command='hostnamectl set-hostname %s' % host
    stdin,stdout,stderr=ssh.exec_command(command)
    resaltcom="systemctl restart salt-minion"
    stdin,stdout,stderr=ssh.exec_command(resaltcom)
    rezabbixcom="systemctl restart zabbix-agent"
    stdin,stdout,stderr=ssh.exec_command(rezabbixcom)
   # stdin,stdout,stderr=ssh.exec_command('reboot')
    print stdout.read()
    print 'hostname已成功修改'
    ssh.close()
    t.close()

def  test_port(ip):
     try:
       tgtHost=ip
       tgtPort=22
       print tgtHost
       nmScan = nmap.PortScanner()
       nmScan.scan(tgtHost, arguments="-n -p 22")
       state = nmScan[tgtHost]['tcp'][int(tgtPort)]['state']
     #  print  state
       if state == 'open':
            return 0
     except Exception,e:
            print tgtHost,"not connected"

def profile(func):
    def wrapper(*args, **kwargs):
        import time
        start = time.time()
        func(*args, **kwargs)
        end   = time.time()
        print 'COST: {}'.format(end - start)
    return wrapper

@profile
def multiprocess(work):
    jobs = []
    get_project()
    id=raw_input("请选择要创建机器所属项目【请选择项目数字标号】:\n")
    projectname=select_project(id)
    print projectname
    get_env()
    env_id=raw_input("请选择创建机器所属环境【请选择项目数字标号】:\n")
    envname=select_env(env_id)
    print envname
    softname='tomcat'
    softname=softname.encode('utf-8')
    software_id=get_soft_id(softname)
    count=raw_input("请选择你要创建kvm机器的数量:\n")
    instancename=projectname + "-" + envname + "-" + softname
    if  int(count) == 0:
        print "输入有误！"
        exit()
    elif int(count) == 1:
        process_id=1
        instancename=projectname + "-" + envname + "-" + softname + "-" + str(process_id)
        create_kvm(count,instancename)
        time.sleep(20)
        int_instance(process_id,projectname,envname,softname)
    elif int(count) > 1:
        create_kvm(count,instancename)
        time.sleep(30)
        for i in range(int(count)):
            i = i + 1
            p = multiprocessing.Process(target=work, args=(i,projectname,envname,softname))
            time.sleep(1)
            p.start()
        for p in jobs:
            p.join()
   # elif int(count) > 10:
   #     create_kvm(count,instancename)
   #     time.sleep(60)
   #     for i in range(int(count)):
   #         i = i + 1
   #         p = multiprocessing.Process(target=work, args=(i,projectname,envname,softname))
   #         time.sleep(1)
   #         p.start()
   #     for p in jobs:
   #         p.join()

    elif int(count) > 10:
        print "暂时不支持超过同时创建10台机器！请重新执行！"
        exit()

def zabbix_add(ipaddress,groupname):
    import monitor.zabbix_api
    zabbix=monitor.zabbix_api.zabbix_api()
   # zabbix.template_get("Base CentOS")
    templatename="Base CentOS"
    if zabbix.hostgroup_get(groupname) is  None:
         print "group not exist"
         zabbix.hostgroup_create(groupname)
         zabbix.host_create(ipaddress,groupname,templatename)
    else:
         print zabbix.hostgroup_get(groupname)
         zabbix.host_create(ipaddress,groupname,templatename)
#        zabbix.host_delete('10.23.215.204')
#        zabbix.hostgroup_create("test_01")

@profile
def  int_instance(process_id,projectname,envname,softname):
     instancename=projectname + "-" + envname + "-" + softname + "-" + str(process_id)
     ip=get_kvm_ip(instancename)
     ip_label=ip.split('.')[2] + "-" + ip.split('.')[3]
     hostname=projectname + "-" + envname + "-" + softname + "-" + ip_label
     print hostname
     modify_kvmname(instancename,hostname)
     while True:
       if test_port(ip) == 0:
          print "$",process_id,"$:机器sshd服务已启用"
          break
     upconfigfile(ip,hostname,process_id)
     KeyFile='/etc/salt/pki/master/minions_pre/' + hostname
     print KeyFile
     while True:
        KeyResult=os.path.isfile(KeyFile)
        print "$",process_id,"$:",KeyResult
        time.sleep(3)
        if KeyResult == False:
            continue
        elif KeyResult == True:
            print "$",process_id,"$:salt认证请求已到达"
            break
     time.sleep(1)
     authkey(hostname)
     groupname=projectname + "_" + envname
     zabbix_add(ip,groupname)
    # post_cmdb(ip,hostname)
     os_command(ip,"mv /root/scripts/* /tmp")
     print "$",process_id,"$:",ip,"openstack kvm机器创建完成"

if __name__ == '__main__':
     #create_instance()
     multiprocess(int_instance)
