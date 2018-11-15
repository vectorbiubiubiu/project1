import requests
from bs4 import BeautifulSoup
import traceback
import re

def getHTMLText(url,code = 'utf-8'):
    try:
        #r = requests.get(url)
        r = requests.get(url)
        r.raise_for_status()
        #r.encoding = r.apparent_encoding
        #可以手动获得它编码的类型，不用apparent_encoding去动态获得
        r.encoding = code
        return r.text
    except:
        return""
#列表类型和获得股票的网站
def getStockList(lst, stockURL):
    #html = getHTMLText(stockURL)
    #东方财富网采用的是GB2312的编码方式
    html = getHTMLText(stockURL,'GBK')
    soup = BeautifulSoup(html,'html.parser')
    a = soup.find_all('a')
    for i in a:
        try:
            href = i.attrs['href']
            #以s开头，中间是h或者z字符，后面有六个数字
            lst.append(re.findall(r"[s][hz]\d{6}",href)[0])
        except:
            continue


#获得每一支个股的信息，并将其存到一个数据结构
def getStockInfo(lst,stockURL,fpath):
    #增加动态进度条
    count = 0
    for stock in lst:
        #百度的链接加上每个个股的链接形成一个访问个股页面的URL
        url = stockURL + stock + ".html"
        #使用getHTMLText函数来获得这个页面的内容
        html = getHTMLText(url)
        try:
            if html == "":
                continue
            #定义一个字典来存储返回的个股信息
            infoDict = {}
            soup = BeautifulSoup(html,'html.parser')
            stockInfo = soup.find('div',attrs={'class':'stock-bets'})
        #查找股票的名称，股票名称被封装在bets-name属性对应的标签内
            name = stockInfo.find_all(attrs={'class':'bets-name'})[0]
            #将这个信息增加到字典中,用split函数获得股票名称的完整部分
            infoDict.update({'股票名称':name.text.split()[0]})
            #dt标签是股票信息的键的域，dd是值的域,keyList和valueList就是这支股票所有键值对的列表
            keyList = stockInfo.find_all('dt')
            valueList = stockInfo.find_all('dd')
            #对键值对列表进行赋值，将他们还原为键值对，并且存到字典中，可用：字典[key]=val向字典中新增内容
            for i in range(len(keyList)):
                key = keyList[i].text
                val = valueList[i].text
                infoDict[key] = val
                #将相关信息保存在文件里
            with open(fpath,'a',encoding='utf-8')as f:
                f.write(str(infoDict) + '\n')
                #增加进度条，打印当前打印进度的百分比
                count = count + 1
                #\r能将我们打印的字符串的光标提到最前，当前打印的覆盖前面
                print('\r当前速度：{：2f}%'.format(count*100/len(lst)),end='')
        except:
            #用traceback的print_exc获得其中的错误信息
            #traceback.print_exc()
            count = count + 1
            print('\r当前速度:{: 2f}%'.format(count * 100 / len(lst)), end='')
            continue



#包含获得股票URL的链接和获取股票信息的链接的主体部分
def main():
    stock_list_url = 'http://quote.eastmoney.com/stocklist.html'
    stock_info_url = 'https://gupiao.baidu.com/stock'
    output_file = 'D://BaiduStockInfo.txt'
    slist = []
    getStockList(slist,stock_list_url)
    getStockInfo(slist,stock_info_url,output_file)

main()
