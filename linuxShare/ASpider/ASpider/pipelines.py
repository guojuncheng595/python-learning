# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import codecs
import json
import MySQLdb
import MySQLdb.cursors
from scrapy.pipelines.images import ImagesPipeline
from scrapy.exporters import JsonItemExporter
from twisted.enterprise import adbapi


class AspiderPipeline(object):
    def process_item(self, item, spider):
        return item


#
class JsonWithEncodingPipeline(object):
    # 自定义json文件的导出
    def __init__(self):  # 初始化打开json文件
        #初始化的时候打开json文件，以wb的形式打开，
        self.file = codecs.open('article.json', 'w', encoding="utf-8")

    # 读取文件
    def process_item(self, item, spider):  # 将文件存储在文件中

        lines = json.dumps(dict(item), ensure_ascii=False) + '\n'  # 将item转换成字符串
        self.file.write(lines)  # 写入到文件当中
        return item

    # 关闭文件
    def spider_closed(self, spider):  # 关闭文件
        self.file.close()


class MysqlPipeline(object):
    # 采用同步的机制写入mysql
    def __init__(self):
        self.conn = MySQLdb.connect('47.104.176.41', 'root', '@Gjc040050', 'article_spider', charset="utf8",
                                    use_unicode=True)
        self.cursor = self.conn.cursor()

    def process_item(self, item, spider):
        insert_sql = """
            insert into article(title, url, create_date, fav_nums)
            VALUES (%s, %s, %s, %s)
        """
        self.cursor.execute(insert_sql, (item["title"], item["url"], item["create_date"], item["fav_nums"]))
        self.conn.commit()


class MysqlTwistedPipline(object):
    def __init__(self, dbpool):
        #初始化的时候，保存在当前类中
        self.dbpool = dbpool

    @classmethod
    def from_settings(cls, settings):
        dbparms = dict(
            host=settings["MYSQL_HOST"],
            db=settings["MYSQL_DBNAME"],
            user=settings["MYSQL_USER"],
            passwd=settings["MYSQL_PASSWD"],
            charset='utf8',
            cursorclass=MySQLdb.cursors.DictCursor,
            use_unicode=True,
        )
        dbpool = adbapi.ConnectionPool("MySQLdb", **dbparms)

        return cls(dbpool)

    def process_item(self, item, spider):
        # 使用twisted将mysql插入变成异步执行
        query = self.dbpool.runInteraction(self.do_insert, item)
        query.addErrback(self.handle_error, item, spider)  # 处理异常

    def handle_error(self, failure, item, spider):
        # 处理异步插入的异常
        print(failure)

    def do_insert(self, cursor, item):
        # 执行具体的插入
        insert_sql = """
            insert into article(title, url, create_date, fav_nums)
            VALUES (%s, %s, %s, %s)
        """
        cursor.execute(insert_sql, (item["title"], item["url"], item["create_date"], item["fav_nums"]))


class JsonExporterPipleline(object):
    # 调用scrapy提供的json exporter导出json文件
    def __init__(self):
        #初始化的时候打开json文件，以wb的形式打开，
        self.file = open('articleexport.json', 'wb')
        self.exporter = JsonItemExporter(self.file, encoding="utf-8", ensure_ascii=False)
        self.exporter.start_exporting()

    def close_spider(self, spider):
        self.exporter.finish_exporting()
        self.file.close()

    def process_item(self, item, spider):
        self.exporter.export_item(item)
        return item


class ArticleImagePipeline(ImagesPipeline):
    def item_completed(self, results, item, info):
        if "front_image_url" in item:
            for ok, value in results:
                image_file_path = value["path"]
            item["front_image_path"] = image_file_path
        return item
