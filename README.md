# Python_baike_spider
Python练习——简单入门级百度百科定向爬虫

爬取百度百科 python 词条 10个

环境

python2.7

依赖

pip install beautifulsoup4
运行

python spider_main.py
如果爬取不了，则百度修改了页面，根据页面修改爬取规则（ urlParser.py 修改规则）

main 爬虫总调度程序
urlManager url管理器
urlDownloader html下载器
urlParser html 解析器、
urlOutputer 输出
