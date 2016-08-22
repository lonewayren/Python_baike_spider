#! usr/bin/python
# -*- coding: UTF-8 -*-
from baike import urlDownloader
from baike import urlManager
from baike import urlOutputer
from baike import urlParser

__author__ = 'Ronny'

class SpiderMain(object):
    def __init__(self):
        self.urls = urlManager.Urlmanager()
        self.downloader = urlDownloader.UrlDownloader()
        self.parser = urlParser.UrlParser()
        self.outputer = urlOutputer.UrlOutputer()

    def crew(self,root_url):
        count = 1
        self.urls.add_new_url(root_url)
        while self.urls.has_new_url():
            try:
                new_url = self.urls.get_new_url()
                # print 'crew %d ：%s' %(count, new_url)
                print 'crew',count,new_url
                html_cont = self.downloader.download(new_url)
                new_urls, new_data = self.parser.parse(new_url, html_cont)
                self.urls.add_new_urls(new_urls)
                self.outputer.collect_data(new_data)

                count += 1
                if count == 10:
                    break
            except Exception,e:
                print e
                print 'crew faild'

        self.outputer.output_html()
        #self.outputer.output_sql()  //连接数据库输出，不需要的话不用管这里

if __name__ == '__main__':
    root_url = 'http://baike.baidu.com/view/21087.htm'
    spider = SpiderMain()
    spider.crew(root_url)
