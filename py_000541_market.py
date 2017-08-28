#!/bin/bash/python3
from html.parser import HTMLParser

class market_parser(HTMLParser):
    __links=[]
    def handle_starttag(self, tag, attrs):
        if tag=="a":
            for name,value in attrs:
                if name=="href" :
                    if  value.startswith("http") and value not in self.__links:
                        self.__links.append(value)
                    elif  value.startswith("//") and value not in self.__links:
                        self.__links.append("http:"+value)
                    elif  value.startswith("www") and value not in self.__links:
                        self.__links.append("http://"+value)
    def getLinks(self):
        return self.__links
    '''
        保存到文件，自动分拆
        file_path 保存文件路径
        per_count 每个文件的行数
    '''
    def saveLinksToFile(self,file_path,per_count):
        try:
            temp=file_path.split(".")
            file_name=temp[0]
            file_ext=temp[1]
            per_count=int(per_count)
            file_index=0
            count=0
            fp = open(file_path, "w+")
            for item in self.__links:
                if count==per_count:
                    count=0
                    file_index=file_index+1
                    fp.close()
                    fp = open(file_name+str(file_index)+"."+file_ext, "w+")
                fp.write(str(item) + "\n")
                count=count+1
        except IOError:
            print("fail to open file")