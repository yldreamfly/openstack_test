#!/usr/bin/env python 
# coding: utf8
import os
import urllib


import logging
import logging.config
import sys,datetime
import xml.etree.ElementTree as etree


#import sys,urllib2
import logging.handlers
from ftplib import FTP 

import time

import salt.client

nowtime=datetime.datetime.now()
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

handler = logging.FileHandler('/root/scripts/config_newsystem_scripts/initsystem.log')
handler.setLevel(logging.INFO)

def listkey():
     unacceptkeydir='/etc/salt/pki/master/minions_pre/'
     unacceptkeys=os.listdir(unacceptkeydir)
     #for unacceptkey in unacceptkeys:
     for i in range(0,len(unacceptkeys)):
           print str([i+1]),unacceptkeys[i]
     select_num=raw_input("请选择需要认证的主机(你配置的IP),如要认证多台请用空格分隔[例：2 3 10] ： ")
     select_num_arry=select_num.split()
     select_result=[]
     for line in select_num_arry:
          select_result.append(unacceptkeys[int(line)-1])
     return select_result

def initsalt(ip):
   import remote.command
   x="rm -rf /etc/salt/pki"
   remote.command.command(ip,x)
   command='/usr/bin/salt-key -d %s -y' % ip
   os.system(command)
   y="systemctl restart salt-minion.service"
   remote.command.command(ip,y)
   time.sleep(10)

def os_command(ip,x):
    import remote.command
    remote.command.command(ip,x)

def reauthkey(ip):
   import remote.command
   command='/usr/bin/salt-key -d %s -y' % ip
   os.system(command)
   c="systemctl restart salt-minion.service"
   remote.command.command(ip,c)


def authkey(ip):
   command='/usr/bin/salt-key -a %s -y' % ip
   os.system(command)
   time.sleep(10)
   try:
     counter=0
     while (counter < 10):
        local = salt.client.LocalClient()
        output = local.cmd(ip,'test.ping')
        print output
        authresult = output[ip]
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

def get_key(ip):
    import MySQLdb
    db = MySQLdb.connect(host='10.23.101.251',user='root',passwd='clt',port=3306,charset='utf8')
    cur = db.cursor()
    query = "SELECT HOST_NAME FROM dafmanager.DETECTOR_HOST where HOSTIP = '%s';" % ip
    cur.execute(query)
    rows=cur.fetchall()
    print "##################以下为目前存在的项目以及英文缩写####################"
    for row in rows:
       key = row[0]
       return key
    cur.close()
    db.close()  

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

def insert_host(hostname,ip):
    import MySQLdb
    db = MySQLdb.connect(host='10.23.101.251',user='root',passwd='clt',port=3306,charset='utf8')
    cur = db.cursor()
    query = "INSERT INTO  dafmanager.INSTALL_HOSTS VALUES (%s,%s) ;" % (hostname,ip)
    cur.execute(query)
    cur.close()
    db.close()
    return  insert_host

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


def get_soft_version(software_id,softname):
    import MySQLdb
    import sys
    db = MySQLdb.connect(host='10.23.101.251',user='root',passwd='clt',port=3306,charset='utf8')
    cur = db.cursor()
    query = "SELECT SOFTWARE_VERSION from dafmanager.INSTALL_SOFT_VERSION  where software_id = '%s'" % (software_id)
    cur.execute(query)
    rows=cur.fetchall()
    num=len(rows)
    print  "##################以下为%s软件存在的版本####################" % softname
    if num > 1 :
      for i in  range(0, len(rows)):
          a = rows[i]
          print str([i+1]),a
    else:  
          i = 1
          a = rows[0]
          print i,a
    select_num=raw_input("以下为选择需要部署软件的版本,请选择序号【单选】： ")
    soft_version=rows[int(select_num)-1]
    cur.close()
    db.close()
    return soft_version

def modify_client(ip,hostname):
    import salt
    from salt import client
    local = salt.client.LocalClient()
    print '开始修改新初始化机器hostname'
    saltcommand='hostnamectl set-hostname %s' % hostname
 #   role=local.cmd(ip, 'cmd.run', [saltcommand])

def upconfigfile(ip,hostname):
    import paramiko
    import datetime
    username='root'
    password='car@clt'
    port = 22
    host=hostname
   # zabbixlocalfile='/root/scripts/config_newsystem_scripts/zabbix_config/zabbix_agentd.conf'
   # saltminionlocalfile='/root/scripts/config_newsystem_scripts/salt_minion_config/minion'
    zabbixcommand="/usr/bin/sed -i 's|Hostname=.*|Hostname=%s|' /root/scripts/config_newsystem_scripts/zabbix_config/zabbix_agentd.conf" % hostname
    saltcommand="/usr/bin/sed -i 's|id:.*|id: %s|' /root/scripts/config_newsystem_scripts/salt_minion_config/minion" % hostname
    os.system(zabbixcommand)
    os.system(saltcommand)
    hostname=ip
    t=paramiko.Transport((hostname,port))
    t.connect(username=username, password=password)
    sftp = paramiko.SFTPClient.from_transport(t)
    print '#########################################'
    print '开始上传机器初始化配置文件到%s, %s ' % (hostname,datetime.datetime.now())
    print '开始上传zabbix配置文件'
    sftp.put(os.path.join('/root/scripts/config_newsystem_scripts/zabbix_config/','zabbix_agentd.conf'),os.path.join('/etc/zabbix/','zabbix_agentd.conf'))
    print '开始上传salt配置文件'
    sftp.put(os.path.join('/root/scripts/config_newsystem_scripts/salt_minion_config/','minion'),os.path.join('/etc/salt/','minion'))
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
 #   stdin,stdout,stderr=ssh.exec_command('reboot')    
    print stdout.read()
    print 'hostname已成功修改'
    ssh.close()
    t.close()
#    zabbixconfig=local.cmd(ip, 'cp.get_file', [['/root/scripts/config_newsystem_scripts/zabbix_config/zabbix_agentd.conf'],['/etc/zabbix/zabbix_agentd.conf']])
#    saltminion_config=local.cmd(ip, 'cp.get_file', [['/root/scripts/config_newsystem_scripts/salt_minion_config/minion'],['/etc/salt/minion']]) 

def installsoftclient(ip,softname,softversion):
    import opspackages.installsoft
    import opspackages.uploadsoft
    if softname == "redis" or softname == "mongo" or softname == "kafka" or softname == "zookeeper":
       print softversion
       installfun="opspackages.installsoft." + softname
       print "开始上传 %s安装包" % (softname)
       install=eval(installfun)
       #opspackages.uploadsoft.upinstallfile(ip,softname)
       #print "上传完成"
       print  "开始安装%s" % (softname)
     #  upinstall(ip,softname)
       hostname=ip
       install(hostname,softversion)
       print  "安装完成"
    else:
       installfun="opspackages.installsoft." + softname
       print "开始上传 %s安装包" % (softname)
       install=eval(installfun)      
       #opspackages.uploadsoft.upinstallfile(ip,softname)
       #print "上传完成"
       print "开始安装 %s" % (softname)
       hostname=ip
       install(hostname)
       print "安装完成"

def init_system():
    get_project()
    id=raw_input("以下为选择要安装机器的项目，请选择项目数字标号:\n")
    projectname=select_project(id)
    print projectname
    get_env()
    env_id=raw_input("以下为选择要安装机器的所属环境，请选择项目数字标号:\n")
    envname=select_env(env_id)
    print envname
    get_soft()
    soft_id=raw_input("以下为选择要安装机器的软件，请选择软件数字标号（单选）:\n")
    softname=select_soft(soft_id)
    softname=softname.encode('utf-8')
    print softname
    software_id=get_soft_id(softname)
    print software_id
    soft_version=get_soft_version(software_id,softname)
    softversion=soft_version[0].replace('.','')
    print softversion
    print '#########以下为未认证主机列表#########'
    select_result=listkey()
    for ip in select_result:
       initsalt(ip)
       authkey(ip)
       ip_label=ip.split('.')[2] + "-" + ip.split('.')[3]
       hostname=projectname + "-" + envname + "-" + softname + "-" + softversion + "-" + ip_label
       #print hostname
       upconfigfile(ip,hostname)
       modify_client(ip,hostname)
       installsoftclient(ip,softname,softversion)
       post_cmdb(ip,hostname)
       reauthkey(ip)
       time.sleep(5)
       command='/usr/bin/salt-key -a %s -y' % hostname
       os.system(command)
       os_command(ip,"mv /root/scripts/* /tmp")

def again_install():
    import opspackages.installsoft
    import opspackages.uploadsoft
    ip=raw_input("请输入要安装软件的ip地址：")
    key=get_key(ip)
    print key
    command='/usr/bin/salt-key -a %s -y' % key
    os.system(command)
    time.sleep(10)
    try:
      counter=0
      while (counter < 10):
         local = salt.client.LocalClient()
         output = local.cmd(key,'test.ping')
         print output
         authresult = output[key]
         if authresult == True:
            print "认证完成！"
            get_soft()
            soft_id=raw_input("以下为选择要安装机器的软件，请选择软件数字标号（单选）:\n")
            softname=select_soft(soft_id)
            softname=softname.encode('utf-8')
            print softname
            software_id=get_soft_id(softname)
            print software_id
            soft_version=get_soft_version(software_id,softname)
            softversion=soft_version[0].replace('.','')
            print softversion
            hostname=key
            if softname == "redis" or softname == "mongo" or softname == "kafka" or softname == "zookeeper":
                print softversion
                installfun="opspackages.installsoft." + softname
                print "开始上传 %s安装包" % (softname)
                install=eval(installfun)
                print  "开始安装%s" % (softname)
                hostname=key
                install(hostname,softversion)
                print  "安装完成"
                exit()
            else:
                installfun="opspackages.installsoft." + softname
                print "开始上传 %s安装包" % (softname)
                install=eval(installfun)
                print "开始安装 %s" % (softname)
                hostname=key
                install(hostname)
                print "安装完成"
                exit()
         else:
            print "认证客户端无法连接！"
            counter==counter+1
            print "尝试再次连接客户端！"
            if counter == 2:
               print "尝试三次连接失败，请排查salt客户端是否配置正确！"
    except Exception,e:
            print Exception,":",e,"网络异常，获取不到客户端信息!! \n 请重新删除saltmaster服务器客户端认证,重启salt-minion客户端，并重新执行此脚本！！"
            os._exit(0)

def choose(list_init,input_content):
    showway=list_init
    for i in range(0,len(showway)):
          print str([i+1]),showway[i]
    select_num=raw_input(input_content)
    select_num_arry=select_num.split()
    print select_num
    return select_num

if __name__ == '__main__':  
    choose_action = ['新增机器初始化并安装软件','已有机器新增软件安装']
    list_init = choose_action   
    input_content="请选择要进行的操作【*选择序号*】： "      
    choose_result=choose(list_init,input_content)
    if choose_result == '1':
       init_system()
    elif choose_result == '2':
       print again_install()
    else:
       print "#####################"
       print "选择出错，请重新选择!"
       print "#####################"
       exit
