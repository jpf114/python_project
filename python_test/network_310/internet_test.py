from time import time
from threading import Thread

import requests


# 继承Thread类创建自定义的线程类
class DownloadHanlder(Thread):

    def __init__(self, iid, url):
        super().__init__()
        self.id = iid
        self.url = url

    def run(self):
        resp = requests.get(self.url)
        with open('out/' + self.id + '.jpg', 'wb') as f:
            f.write(resp.content)


def main():
    # 通过requests模块的get函数获取网络资源
    # 下面的代码中使用了天行数据接口提供的网络API
    # 要使用该数据接口需要在天行数据的网站上注册
    # 然后用自己的Key替换掉下面代码的中APIKey即可
    resp = requests.get(
        'https://apis.tianapi.com/wxnew/index?key=06f18ee10bb8c2425fb82cd252fe5430&num=20')
    # 将服务器返回的JSON格式的数据解析为字典
    data_model = resp.json()
    result = data_model['result']
    for mm_dict in result['list']:
        iid = mm_dict['id']
        url = mm_dict['picurl']
        # 通过多线程的方式实现图片下载
        DownloadHanlder(iid, url).start()


if __name__ == '__main__':
    main()