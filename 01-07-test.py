import time
import random

import requests
from bs4 import BeautifulSoup
import pandas as pd


class Stock:
    header = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36'
    }

    def __init__(self, stockid):
        self.stockid = stockid

    def get_html(self, page):
        url = 'https://vip.stock.finance.sina.com.cn/corp/view/vCB_AllBulletin.php?stockid={}&Page={}'.format(
            self.stockid, page)
        # print(url)
        req = requests.get(url, headers=self.header)
        html = req.text
        # with open('000002.html', 'w') as fb:
        #     fb.write(html)
        return html

    def ana_html(self, html):
        soup = BeautifulSoup(html, 'html.parser')
        datelist = soup.find(class_='datelist')
        if datelist == None:
            return None
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
            return result

    def write_excel(self, data):
        df = pd.DataFrame(data)
        order = ['stockid', 'date', 'title', 'href']
        df = df[order]
        df = df.sort_values(by=order)
        file = 'data/{}.xlsx'.format(self.stockid)
        df.to_excel(file, index=False)

    def test(self):
        page = 1
        result = []
        flag = True
        while flag:
            html = self.get_html(page)
            data = self.ana_html(html)
            if data != None:
                result.extend(data)
                print('正在爬取公告 股票{} 页码{} 获取记录{}/{}'.format(self.stockid, page, len(data), len(result)))
                time.sleep(random.randint(1, 3))
                page += 1
            else:
                flag = False

        self.write_excel(result)


if __name__ == '__main__':
    # 测试的代码
    stock = Stock('000002')
    stock.test()
