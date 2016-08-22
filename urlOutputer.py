#! usr/bin/python
# -*- coding: UTF-8 -*-
import MySQLdb

__author__ = 'Ronny'

class UrlOutputer(object):

    def __init__(self):
        self.datas = []

    def collect_data(self, data):
        if data is None:
            return
        self.datas.append(data)

    def output_html(self):
        fout = open('output.html', 'w')
        fout.write('<html>')
        fout.write('<body>')
        fout.write('<table>')
        for data in self.datas:
            fout.write('<tr>')
            fout.write('<td>%s</td>'%(data['url'].encode('utf-8')))
            fout.write('<td>%s</td>' % (data['title'].encode('utf-8')))
            fout.write('<td>%s</td>' % (data['summary'].encode('utf-8')))
            fout.write('</tr>')

        fout.write('</table>')
        fout.write('</body>')
        fout.write('</html>')

        fout.close()
    def output_sql(self):
        db = MySQLdb.connect('127.0.0.1', 'root', 'root', 'test',charset = 'utf8')
        cursor = db.cursor()
        try:
            for data in self.datas:
                sql = "INSERT INTO spider (url, title, summary) VALUES ('%s', '%s', '%s')" %( data['url'].encode('utf-8'), data['title'].encode('utf-8'), data['summary'].encode('utf-8'))
                cursor.execute(sql)
                db.commit()
        except Exception, e:
            print e
            print 'DBError'
            db.rollback()
        db.close()

