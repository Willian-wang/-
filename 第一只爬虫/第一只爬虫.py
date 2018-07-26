#-*- coding:utf-8 -*-
import urllib.request 
import http.cookiejar
from bs4 import BeautifulSoup
import txt_to_excel
import json
import time
import multiprocessing
import threading
import queue



class CatchDataThread(threading.Thread):
    #顾名思义，这玩意是用来抓取
    def __init__(self,threadID,Urlqueue,Dataqueue):
        self.Urlqueue=Urlqueue
        self.Dataqueue=Dataqueue
        self.threadID=threadID
        self.headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
    def run(self):
        while 1:
            if self.Urlqueue.empty():
                break
            num=self.Urlqueue.get()
            url="http://ce.sysu.edu.cn/hope/Diaries/Index_"+str(num)+".aspx"
            self.Dataqueue.put(RequireData(url))

class DealDataThread(threading.Thread):
    def __init__(self,threadID,Dataqueue,lock):
        self.Dataqueue=

def RequireData(url):
    data=bytes(urllib.parse.urlencode({'用户名':'谢志强'},{'密码':''}),encoding='utf8')
    req=urllib.request.Request(url,data=data,headers=headers,method='GET')
    Response=urllib.request.urlopen(req)    
    TEXT=Response.read().decode('utf-8')
    return TEXT


CATCH_EXIT=False
PARSE_EXIT = False


Urlqueue=queue.Queue(13176)
Dataqueue=queue.Queue()
threads=[]
for i in range(13176):
    Urlqueue.put(i)

for threadID in range(10):
    Cthread=CatchDataThread(threadID,Urlqueue,Dataqueue)
    threads.append(thread)
    thread.start()

for threadID in range(11:13):
    thread=DealDataThread(threadID,Dataqueue,lock)






def getdata(aue,fileObject,n):
    #cookie=http.cookiejar.CookieJar()
    headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
    #headers=urllib.request.HTTPCookieProcessor(cookiejar=cookie)
    #dict = {'name':'Germey'}
    data=bytes(urllib.parse.urlencode({'用户名':'谢志强'},{'密码':''}),encoding='utf8')
    req=urllib.request.Request(aue,data=data,headers=headers,method='GET')
    Response=urllib.request.urlopen(req)    
    TEXT=Response.read().decode('utf-8')
    soup=BeautifulSoup(TEXT,"lxml")
    #print(soup)
    content=soup.find_all("li",class_="internal_box_left_dairylist_li")
    #print(content)
    n=str(n)
    for item in content:
        for string_item in item.stripped_strings:
            #print(string_item)
            fileObject.write(string_item)
            fileObject.write('\n')
    print("Complete %s/13176"% n)


n=0
aue="http://ce.sysu.edu.cn/hope/Diaries/Index_0.aspx"
fileObject = open('日志.txt', 'a',encoding="utf-8") 
while n<13176:
    str1=str(n)
    str2=str(n+1)
    aue=aue.replace(str1,str2)
    getdata(aue,fileObject,n)
    n=n+1
fileObject.close()   
txt_to_excel.txt_to_excel()