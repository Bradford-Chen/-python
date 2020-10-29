import time
import random
import os
import datetime

import requests
from bs4 import BeautifulSoup
import pandas as pd


class Stock:
    header = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36'
    }
    order = ['stockid', 'date', 'title', 'href']

    def __init__(self, stockid):
        self.stockid = stockid
        self.file = 'data/{}.xlsx'.format(self.stockid)

    def get_html(self, page):
        try:
            url = 'https://vip.stock.finance.sina.com.cn/corp/view/vCB_AllBulletin.php?stockid={}&Page={}'.format(
                self.stockid, page)
            # print(url)
            req = requests.get(url, headers=self.header)
            html = req.text
            # with open('000002.html', 'w') as fb:
            #     fb.write(html)
            return html
        except:
            print('连接失败，正在重新发起请求')
            time.sleep(random.randint(10, 15))
            return self.get_html(page)

    def ana_html(self, html):
        soup = BeautifulSoup(html, 'html.parser')
        datelist = soup.find(class_='datelist')
        if datelist == None:
            return None, None
        else:
            a = datelist.find_all('a')
            result = []
            for item in a:
                # print(item)
                result_mid = {}
                result_mid['stockid'] = self.stockid
                result_mid['title'] = item.get_text()
                result_mid['href'] = item['href']
                result_mid['date'] = item.previous_sibling.replace('\n', '').strip()
                # print(result_mid['stockid'])
                # print(result_mid['title'])
                # print(result_mid['href'])
                # print(result_mid['date'])
                # print()
                result.append(result_mid)
            date_curr = result[-1]['date']
            date_curr = datetime.datetime.strptime(date_curr, '%Y-%m-%d') - datetime.timedelta(days=10)
            return result, date_curr

    def write_excel(self, df):
        df = df[self.order]
        df = df.sort_values(by=self.order)
        df.to_excel(self.file, index=False)

    def read_excel(self):
        if os.path.exists(self.file):
            df = pd.read_excel(self.file, dtype=str)
            date_last = df['date'].max()
            date_last = datetime.datetime.strptime(date_last, '%Y-%m-%d')
        else:
            df = pd.DataFrame(columns=self.order)
            date_last = None
        self.result_last = df
        self.date_last = date_last

    def append(self):
        result = self.result_last.append(self.result_curr)
        result = result.drop_duplicates(keep='last')
        return result

    def test(self):
        self.read_excel()
        page = 1
        result = []
        flag = True
        while flag:
            html = self.get_html(page)
            data, date_curr = self.ana_html(html)
            if data != None:
                result.extend(data)
                print('正在爬取公告 股票{} 页码{} 获取记录{}/{}'.format(self.stockid, page, len(data), len(result)))
                time.sleep(random.randint(1, 3))
                page += 1
                if self.date_last != None:
                    if self.date_last > date_curr:
                        flag = False
            else:
                flag = False
        self.result_curr = pd.DataFrame(result)
        result = self.append()
        self.write_excel(result)


if __name__ == '__main__':
    # 测试的代码
    stock = Stock('000002')
    stock.test()
