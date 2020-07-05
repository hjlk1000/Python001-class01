# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
import pymysql
dbInfo = {
    'host' : 'localhost',
    'port' : 3306,
    'user' : 'root',
    'password' : '123456',
    'db' : 'maoyan'
}

class SpidersPipeline:

    def process_item(self, item, spider):
        return item

 def process_item(self, item, spider):
         movie_name = item['movie_name']
         movie_type = item['movie_type']
         movie_time = item['movie_time']
         conn = pymysql.connect(
            host = dbInfo['host'],
            port = dbInfo['port'],
            user = dbInfo['user'],
            password = dbInfo['password'],
            db = dbInfo['db']
         )

         cur = conn.cursor()
         try:
             values = [movie_name,movie_type, movie_time]
             print(values)
             cur.execute('INSERT INTO  tb2 values(%s,%s,%s)' ,values)

             cur.close()
             conn.commit()
         except:
             conn.rollback()

         conn.close()

         return item