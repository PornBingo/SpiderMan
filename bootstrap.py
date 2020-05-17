# encoding=utf-8

import pymongo
from items import InformationItem, TweetsItem, RelationshipsItem
import MySQLdb

class MysqlDBPipleline(object):
    def __init__(self):
        sef.count=1
        self.conn = MySQLdb.connect(
          host='localhost',
          port=3306,
          user='root',
          passwd='***'
          db='PornHub',
          charset='utf8')
         self.cur = self.conn.cursor()
         
