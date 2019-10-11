#-*-coding:utf-8-*-

import requests
from threading import Thread
from queue import Queue
import time
import csv
from bs4 import BeautifulSoup
from threading import Lock
from my_fake_useragent import UserAgent


class XiaomiSpider(object):
    def __init__(self):
        self.url = 'http://app.mi.com/categotyAllListApi?page={}&categoryId={}&pageSize=30'
        self.q = Queue()  # 存放所有URL地址的队列
        self.i = 0
        self.id_list = []  # 存放所有类型id的空列表
        # 打开文件
        self.f = open('xiaomi.csv', 'a', newline="")
        self.writer = csv.writer(self.f)
        self.lock = Lock()  # 创建锁
        self.ua = UserAgent()

    def get_cateid(self):
        # 请求
        url = 'http://app.mi.com/'
        headers = {'User-Agent': self.ua.random}
        html = requests.get(url=url, headers=headers).text
        # 解析
        parse_html =BeautifulSoup(html,'lxml')
        li_list = parse_html.xpath('//ul[@class="category-list"]/li')
        for li in li_list:
            typ_name = li.xpath('./a/text()')[0]
            typ_id = li.xpath('./a/@href')[0].split('/')[-1]
            pages = self.get_pages(typ_id)  # 计算每个类型的页数
            self.id_list.append((typ_id, pages))

        self.url_in()  # 入队列

    # 获取counts的值并计算页数
    def get_pages(self, typ_id):
        # 每页返回的json数据中,都有count这个key
        url = self.url.format(0, typ_id)
        html = requests.get(url=url, headers={'User-Agent': self.ua.random}).json()
        count = html['count']       # 类别中的数据总数
        pages = int(count) // 30 + 1        # 每页30个，看有多少页

        return pages

    # url入队列
    def url_in(self):
        for id in self.id_list:
            # id为元组,(typ_id, pages)-->('2',pages)
            for page in range(2):
                url = self.url.format(page, id[0])
                print(url)
                # 把URL地址入队列
                self.q.put(url)

    # 线程事件函数: get() - 请求 - 解析 - 处理数据
    def get_data(self):
        while True:
            # 当队列不为空时,获取url地址
            if not self.q.empty():
                url = self.q.get()
                headers = {'User-Agent': self.ua.random}
                html = requests.get(url=url, headers=headers).json()
                self.parse_html(html)
            else:
                break

    # 解析函数
    def parse_html(self, html):
        # 存放1页的数据 - 写入到csv文件
        app_list = []
        for app in html['data']:
            # 应用名称 + 链接 + 分类
            name = app['displayName']
            link = 'http://app.mi.com/details?id=' + app['packageName']
            typ_name = app['level1CategoryName']
            # 把每一条数据放到app_list中,目的为了 writerows()
            app_list.append([name, typ_name, link])
            print(name, typ_name)
            self.i += 1

        # 开始写入1页数据 - app_list
        self.lock.acquire()
        self.writer.writerows(app_list)
        self.lock.release()

    # 主函数
    def main(self):
        self.get_cateid()       # URL入队列
        t_list = []
        # 创建多个线程
        for i in range(1):
            t = Thread(target=self.get_data)
            t_list.append(t)
            t.start()

        # 统一回收线程
        for t in t_list:
            t.join()

        # 关闭文件
        self.f.close()
        print('数量:', self.i)


if __name__ == '__main__':
    start = time.time()
    spider = XiaomiSpider()
    spider.main()
    end = time.time()
    print('执行时间:%.2f' % (end - start))