# 大数据财税与python应用
# 2019-2020年第3学期
# 学号：2019312256
# 姓名：陈祥锡
# 专业：电子商务类19-1


# 请在以下地方编写程序
# 弹幕获取
import requests
import re
import csv
import jieba
import wordcloud


headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36'
}
url = 'https://api.bilibili.com/x/v1/dm/list.so?oid=215927939'
rep = requests.get(url, headers=headers)
html = rep.content.decode('utf-8')

# 解析网页
text = re.compile('<d.*?>(.*?)</d>')
danmu = re.findall(text, html)
print(danmu)

# 保存弹幕
for i in danmu:
    with open('C:/Users/chen/Desktop/弹幕文件.csv', 'a', newline='', encoding='utf-8-sig') as f:
        writer = csv.writer(f)
        danmu = [i]
        writer.writerow(danmu)

# 制作词云图
danmu_text = open('C:/Users/chen/Desktop/弹幕文件.csv', encoding='utf-8')
txt = danmu_text.read()
words = jieba.lcut(txt)
string = " ".join(words)
print(string)
pic = wordcloud.WordCloud(
    width=1000,
    height=1000,
    background_color='white',
    font_path='msyh.ttc',
    scale=15,
    stopwords={' '},
)
pic.generate(string)
pic.to_file('C:/Users/chen/Desktop/1.png')