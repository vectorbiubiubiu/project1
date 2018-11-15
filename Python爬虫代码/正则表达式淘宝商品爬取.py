import requests
import re

#获得页面的函数getHTMLText
def getHTMLText(url):
    try:
        r = requests.get(url,timeout = 30)
        r.raise_for_status()
#将对文本中分析的编码来替换整体的编码
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return""

#对每个获得的页面进行解析，定义函数parsPage,包含列表类型ilt和HTML页面信息（关键）
def parsePage(ilt,html):
    try:
#findall函数返回一个列表，\表示引入的符号，\"表示引入双引号，\:表示引入冒号，\d表示数字0-9，\.表示点字符，
# view_price表示价格前标识，商品价格一般由数字和小数点构成，将其保存在变量plt中
        plt = re.findall(r'\"view_price\"\:\"[\d\.]*\"',html)
#同理，将商品名称保存在变量tit中,*?为最小匹配，取得以最后一个双引号为止的内容
        tlt = re.findall(r'\"raw_title\"\:\".*?\"',html)
        for i in range(len(plt)):
#eval函数去掉双引号或单引号，用split函数（切片）使用冒号来分割字符串，获得键值对的后面部分
            price = eval(plt[i].split(':')[1])
            title = eval(tlt[i].split(':')[1])
            ilt.append([price, title])
    except:
        print("")

#将商品信息输出到页面，打印出来，定义函数
def printGoodsList(ilt):
#定义表的长度，前面长度为4，中间长度为8，最后长度16
    tplt = "{:4}\t{:8}\t{:16}"
    print(tplt.format("序号","价格","商品名称"))
#定义输出信息的接收器count
    count = 0
    for g in ilt:
        count = count +1
#count表明商品的序号，后面的两个是商品的价格和商品的名称
        print(tplt.format(count,g[0],g[1]))



#定义主函数，记录程序运行相关过程
def main():
    goods = '眼影'
#设定爬取深度
    depth = 4
#爬取信息的相关URL
    start_url = 'https://s.taobao.com/search?q='+goods
#输出结果
    infoList = []
#对每一个页面进行单独的访问并处理
    for i in range(depth):
        try:
#每个页面起始的S是44的倍数
            url = start_url + '&s='+str(44*i)
            html = getHTMLText(url)
            parsePage(infoList,html)
        except:
            continue
    printGoodsList(infoList)

main()
