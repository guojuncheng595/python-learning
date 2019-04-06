# -*- coding: utf-8 -*-

# Scrapy settings for GjcArticleSpider project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://doc.scrapy.org/en/latest/topics/settings.html
#     https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://doc.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'GjcArticleSpider'

SPIDER_MODULES = ['GjcArticleSpider.spiders']
NEWSPIDER_MODULE = 'GjcArticleSpider.spiders'


# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'GjcArticleSpider (+http://www.yourdomain.com)'

# Obey robots.txt rules 如果不设置ROBOT回去读取每一个网站上的robot协议
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://doc.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
#DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
#COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
#DEFAULT_REQUEST_HEADERS = {
#   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#   'Accept-Language': 'en',
#}

# Enable or disable spider middlewares
# See https://doc.scrapy.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'GjcArticleSpider.middlewares.GjcarticlespiderSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
#DOWNLOADER_MIDDLEWARES = {
#    'GjcArticleSpider.middlewares.GjcarticlespiderDownloaderMiddleware': 543,
#}

# Enable or disable extensions
# See https://doc.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See https://doc.scrapy.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
   # 'GjcArticleSpider.pipelines.GjcarticlespiderPipeline': 300,
    # 'scrapy.pipelines.images.ImagesPipeline': 1 # 图片下载pipelines
   # 'GjcArticleSpider.pipelines.ArticleImagePipeline': 1,

   # 'GjcArticleSpider.pipelines.JsonWithEncodingPipeline': 2,
   # 'GjcArticleSpider.pipelines.JsonExporterPipleline': 2,
   # 'GjcArticleSpider.pipelines.MysqlPipeline': 1,

   'GjcArticleSpider.pipelines.MysqlTwistedPipline': 1,

}
# Imagespipeline 找IMAGES_URLS_FIELD对应字段，并下载图片
IMAGES_URLS_FIELD = "front_image_url"
# 获取图片存放路径
import os
os.path.dirname(__file__)  # 获取到GjcArticleSpider目录的名称
project_dir = os.path.abspath(os.path.dirname(__file__))
# 设置图片的保存路径
IMAGES_STORE = os.path.join(project_dir, 'images')
IMAGES_MIN_HEIGHT = 100  # 最小高度
IMAGES_MIN_WIDTH = 100  # 最小宽带


# Enable and configure the AutoThrottle extension (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'

MYSQL_HOST = "127.0.0.1"
MYSQL_DBNAME = "scrapyspider"
MYSQL_USER = "root"
MYSQL_PASSWORD = "root"