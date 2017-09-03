# -*- coding: utf8 -*-
#from __future__ import absolute_import

import json
import sys
import urllib2

class zabbix_api:
    def __init__(self):
         self.url = 'http://10.23.215.9/zabbix/api_jsonrpc.php'
         self.header = {"Content-Type": "application/json"}
    def user_login(self):
         data = json.dumps({
                           "jsonrpc": "2.0",
                           "method": "user.login",
                           "params": {
                                   "user": "Admin",
                                   "password": "zabbix"
                                      },
                           "id": 1
                           })
         request = urllib2.Request(self.url,data)
         for key in self.header:
              request.add_header(key,self.header[key])
         try:
              result = urllib2.urlopen(request)
         except Exception as e:
              print "Auth Failed, Please Check Your Name And Password:"
         else:
              response = json.loads(result.read())
              result.close()
              #print "Auth Successful. The Auth ID Is:",response['result']
              return response['result']
    def hostgroup_get(self, hostgroupName=''):
            data = json.dumps({
                               "jsonrpc":"2.0",
                               "method":"hostgroup.get",
                               "params":{
                                         "output": "extend",
                                         "filter": {
                                                    "name": hostgroupName
                                                    }
                                         },
                               "auth":self.user_login(),
                               "id":1,
                               })
            request = urllib2.Request(self.url,data)
            for key in self.header:
                request.add_header(key, self.header[key])
            try:
                result = urllib2.urlopen(request)
            except URLError as e:
                print "Error as ", e
            else:
                #print result.read()
                response = json.loads(result.read())
                result.close()
                #print response()
                for group in response['result']:
                        if  len(hostgroupName)==0:
                                print "hostgroup:  \033[31m %s \033[0m groupid : %s" %(group['name'],group['groupid'])
                        else:
                #               print "hostgroup:  \033[31m %s \033[0m groupid : %s" %(group['name'],group['groupid'])
                                self.hostgroupID = group['groupid']
                                return group['groupid']

    def hostgroup_create(self, hostgroupName=''):
            data = json.dumps({
                               "jsonrpc":"2.0",
                               "method":"hostgroup.create",
                               "params":{
                                        "name": hostgroupName
                                         },
                               "auth":self.user_login(),
                               "id":1,
                               })
            request = urllib2.Request(self.url,data)
            for key in self.header:
                request.add_header(key, self.header[key])
            try:
                result = urllib2.urlopen(request)
            except URLError as e:
                print "Error as ", e
            else:
                #print result.read()
                response = json.loads(result.read())
                print response
                result.close()
                print "hostgroup:  \033[31m newgroup: %s \033[0m groupid : %s" %(hostgroupName,response['result']['groupids'])
 
    def template_get(self, templateName=''):
            data = json.dumps({
                               "jsonrpc":"2.0",
                               "method":"template.get",
                               "params":{
                                         "output": "extend",
                                         "filter": {
                                                    "host": templateName
                                                    }
                                         },
                               "auth":self.user_login(),
                               "id":1,
                               })
            request = urllib2.Request(self.url,data)
            for key in self.header:
                request.add_header(key, self.header[key])
            try:
                result = urllib2.urlopen(request)
            except URLError as e:
                print "Error as ", e
            else:
                #print result.read()
                response = json.loads(result.read())
                result.close()
                #print response()
                for template in response['result']:
                        if  len(templateName)==0:
                                print "template:  \033[31m %s \033[0m templateid : %s" %(template['host'],template['templateid'])
                        else:
                #               print "template:  \033[31m %s \033[0m templateid : %s" %(template['host'],template['templateid'])
                                self.templateID = template['templateid']
                                return template['templateid']

    def host_create(self, hostName,hostgroupName,templateName):
            zabbix=zabbix_api()
            groupid=zabbix.hostgroup_get(hostgroupName)
            templateid=zabbix.template_get(templateName)
            data = json.dumps({
                               "jsonrpc":"2.0",
                               "method":"host.create",
                               "params": {
                                    "host": hostName,
                                    "interfaces": [
                                        {
                                          "type": 1,
                                          "main": 1,
                                          "useip": 1,
                                          "ip": hostName,
                                          "dns": "",
                                          "port": "10050"
                                         }
                                    ],
                                    "groups": [
                                           {
                                               "groupid": groupid
                                            }
                                    ],
                                    "templates": [
                                           {
                                               "templateid": templateid
                                            }
                                    ],       
                                         },
                               "auth":self.user_login(),
                               "id":1
                               })
            request = urllib2.Request(self.url,data)
            for key in self.header:
                request.add_header(key, self.header[key])
            try:
                result = urllib2.urlopen(request)
            except URLError as e:
                print "Error as ", e
            else:
                #print result.read()
                response = json.loads(result.read())
                print response
                result.close()
                print "newhost:  \033[31m %s \033[0m hostid : %s" %(hostName,response['result']['hostids'])

    def host_get(self, hostName=''):
            data = json.dumps({
                               "jsonrpc":"2.0",
                               "method":"host.get",
                               "params":{
                                         "output": "extend",
                                         "filter": {
                                                    "host": [
                                                         hostName
                                                       ]
                                                    }
                                         },
                               "auth":self.user_login(),
                               "id":1,
                               })
            request = urllib2.Request(self.url,data)
            for key in self.header:
                request.add_header(key, self.header[key])
            try:
                result = urllib2.urlopen(request)
            except URLError as e:
                print "Error as ", e
            else:
                #print result.read()
                response = json.loads(result.read())
                result.close()
                #print response()
                for host in response['result']:
                        if  len(hostName)==0:
                                print "host:  \033[31m %s \033[0m hostid : %s" %(host['host'],host['hostid'])
                        else:
                #               print "host:  \033[31m %s \033[0m hostid : %s" %(host['host'],host['hostid'])
                                return host['hostid']


    def host_delete(self,hostName=''):
            zabbix=zabbix_api()
            hostid=zabbix.host_get(hostName)
            data=json.dumps({
                              "jsonrpc": "2.0",
                              "method": "host.delete",
                              "params": [
                                     hostid
                              ],
                              "auth": self.user_login(),
                              "id": 1
                           })
            request = urllib2.Request(self.url,data)
            for key in self.header:
                request.add_header(key, self.header[key])
            try:
                result = urllib2.urlopen(request)
            except Exception,e:
                print  e
            else:
                response = json.loads(result.read())
                result.close()
                for host in response['result']:
                     if len(hostName)==0:
                          print "hostid : %s" %(host['hostid'])
                     else:
                          print "hostid:  %s  is deleted !" % hostid  


#if __name__ == "__main__":
#        zabbix=zabbix_api()
#       # zabbix.template_get("Base CentOS")
#        if zabbix.hostgroup_get("openstack") is  None:
#               print "group not exist"
#               zabbix.hostgroup_create("openstack")
#        else:
#               print zabbix.hostgroup_get("openstack")
#               zabbix.host_create('10.23.215.204',"test","Base CentOS")
#               zabbix.host_delete('10.23.215.204')
#        #zabbix.hostgroup_create("test_01")
