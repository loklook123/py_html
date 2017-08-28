#!/bin/bash/pyton3
# coding=utf-8
from html_parser import html_parser
import urllib.request
import datetime

def parser(links,myparser):
    count=0
    for x in  links:
        data=""
        print("parsing(%s) url:%s" %(str(count),str(x)))
        try:
            response = urllib.request.urlopen(x,b"",10000)
            data = response.read().decode(encoding="utf-8")
        except urllib.error.HTTPError as e:
            print('The server couldn\'t fulfill the request.')
            print('Error code: ', e.code)
        except urllib.error.URLError as e:
            print('We failed to reach a server.')
            print('Reason: ', e.reason)
        except UnicodeDecodeError:
            print("UnicodeDecodeError")
        except:
            print("Other exception handle")
        else:
            '''print("no exception, get here")'''
        finally:
            '''print("finally")'''

        if data!="":
            myparser.feed(data)
        count =count+1
        if count>1000:
            break

url="http://b2b.youboy.com/";
myparser=html_parser()
start=datetime.datetime.now()

resp=urllib.request.urlopen(url).read()
myparser.feed(resp.decode(encoding="utf-8"))
links=myparser.getLinks();

parser(links,myparser);

myparser.saveLinksToFile("urls.txt",5000)
myparser.close()
d=datetime.datetime.now()-start
print("process use:"+str(d.seconds)+" seconds")