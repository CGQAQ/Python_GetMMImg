# coding:utf-8
# author: CG

from urllib import request
import re
import random
import time
import os

class Spider:
    @classmethod
    def gethtml(cls, n):
        url = 'http://jandan.net/ooxx/page-' + str(n)
        res = request.urlopen(url)
        html = res.read().decode('utf-8')
        return html

    @classmethod
    def geturl(cls, o):
        a = re.findall('(?<=<img src=").*?(?=" />)', o, re.MULTILINE)
        return a

    @classmethod
    def download(cls, o):
        for i in o:
            req = request.Request(i, headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.116 Safari/537.36'})
            res = request.urlopen(req)
            with open('./MM/' + i.split('/')[-1], 'wb') as f:
                f.write(res.read())

    @classmethod
    def run(cls):
        index = random.randint(500, 1500)
        i = input('input page you want: ')
        print('Spiding...')
        if not os.path.exists('./MM'):
            os.mkdir('./MM')
        for item in range(index, index+int(i)):
            html = cls.gethtml(item)
            urls = cls.geturl(html)
            cls.download(urls)
            time.sleep(0.5)
        print('download complete!')


a = Spider()
a.run()
