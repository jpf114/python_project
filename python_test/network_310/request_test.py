import re
import time
import random

import requests
from lxml import etree


def retest_1():
    pattern = re.compile(r'<a.*?href="(.*?)".*?title="(.*?)".*?>')
    resp = requests.get('https://www.sohu.com/')
    if resp.status_code == 200:
        all_matches = pattern.findall(resp.text)
        for href, title in all_matches:
            print(href)
            print(title)


def retest_2():
    for page in range(1, 11):
        resp = requests.get(
            url=f'https://movie.douban.com/top250?start={(page - 1) * 25}',
            # 如果不设置HTTP请求头中的User-Agent，豆瓣会检测出不是浏览器而阻止我们的请求。
            # 通过get函数的headers参数设置User-Agent的值，具体的值可以在浏览器的开发者工具查看到。
            # 用爬虫访问大部分网站时，将爬虫伪装成来自浏览器的请求都是非常重要的一步。
            headers={
                'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36'}
        )
        # 通过正则表达式获取class属性为title且标签体不以&开头的span标签并用捕获组提取标签内容
        pattern1 = re.compile(r'<span class="title">([^&]*?)</span>')
        titles = pattern1.findall(resp.text)
        # 通过正则表达式获取class属性为rating_num的span标签并用捕获组提取标签内容
        pattern2 = re.compile(r'<span class="rating_num".*?>(.*?)</span>')
        ranks = pattern2.findall(resp.text)
        # 使用zip压缩两个列表，循环遍历所有的电影标题和评分
        for title, rank in zip(titles, ranks):
            print(title, rank)
        # 随机休眠1-5秒，避免爬取页面过于频繁
        time.sleep(random.random() * 4 + 1)


def request_xpath():
    for page in range(1, 11):
        resp = requests.get(
            url=f'https://movie.douban.com/top250?start={(page - 1) * 25}',
            headers={'User-Agent': 'BaiduSpider'}
        )
        tree = etree.HTML(resp.text)
        # 通过XPath语法从页面中提取电影标题
        title_spans = tree.xpath('//*[@id="content"]/div/div[1]/ol/li/div/div[2]/div[1]/a/span[1]')
        # 通过XPath语法从页面中提取电影评分
        rank_spans = tree.xpath('//*[@id="content"]/div/div[1]/ol/li[1]/div/div[2]/div[2]/div/span[2]')
        for title_span, rank_span in zip(title_spans, rank_spans):
            print(title_span.text, rank_span.text)


def main():
    # retest_1()
    # retest_2()
    request_xpath()


if __name__ == '__main__':
    main()
