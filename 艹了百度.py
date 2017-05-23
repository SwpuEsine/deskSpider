import requests
import sys
from bs4 import BeautifulSoup
from functools import reduce
import lxml
import threading
import python爬取招聘信息.parselist as pl
Default_Header = {
'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
'Accept-Encoding':'gzip, deflate, sdch, br',
'Accept-Language': 'zh-CN,zh;q=0.8',
'Cache-Control': 'max-age=0',
'Connection': 'keep-alive',
'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36',
'Cookie':'__cfduid=d2e7362981447e2856cf0f87738c1b0ef1483798173; BDUSS=kVIOVo5R3BVWjZkeTFsMy1sT3BsUDgwOVJyRGNGWlpsbHZ0UWd1blg4aEV1ajlaSVFBQUFBJCQAAAAAAAAAAAEAAADbIto~amF2YdChvas3AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAEQtGFlELRhZd; ispeed_lsm=2; BAIDUID=706EE80398E0B5B73995C3DF617F11EF:FG=1; BIDUPSID=200447D81A437F77273044186605A355; PSTM=1495273452; BD_HOME=1; BD_UPN=12314353; H_PS_645EC=0460wAWsqyJmXm7RN2uWFwTmDVHHGdu4zP9UY3IhgYOfGeC%2BBBASB0EQFGn7kIVEucxl; WWW_ST=1495491620880; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; BDRCVFR[feWj1Vr5u3D]=I67x6TjHwwYf0; BD_CK_SAM=1; PSINO=3; BDSVRTM=156; H_PS_PSSID=1442_21119_17001_21928_22159',
'Upgrade-Insecure-Requests':'1',
'Host':'www.baidu.com',
}
url="https://www.baidu.com/s?ie=utf-8&f=8&rsv_bp=1&rsv_idx=2&tn=baiduhome_pg&wd=%E4%BA%92%E8%81%94%E7%BD%91&rsv_spt=1&oq=requests.exceptions.%2526lt%253Bhunked%2526gt%253Bncoding%2526gt%253Brror&rsv_pq=a4b335640004a255&rsv_t=1f61VvixsjTLXzcHzcWfMkbHoS6PskMIRiSg9WWFI0dnKZSI%2FEPHDnCKG2sqD9YzT%2FjC&rqlang=cn&rsv_enter=1&rsv_sug3=8&rsv_sug1=8&rsv_sug7=100&rsv_sug2=0&inputT=1580&rsv_sug4=1580&rsv_sug=1"
print("url是"+url)
conteng=requests.get(url,
headers=Default_Header).content.decode("utf8")
print(conteng)
#soup.find_all("a", string="Elsie")
newsList=[]
soup=BeautifulSoup(conteng,'lxml')
soup.find()
list=soup.select('div[class="result-op c-container xpath-log"]')
for div in list:
 if div.find("h3").contents[1].contents[1]=='的最新相关信息':
     crow=div.select('div[class="c-row"]')
     for row in crow:
         json = {}
         json['url']=row.a['href']
         json['web_chName']=row.select('span[style="color:#008000"]')[0].string
         json['title']=reduce(lambda x,y:str(x).strip().lstrip('<em>').rstrip("<em>")+str(y).strip().lstrip('<em>').rstrip("<em>"),row.a.contents)
         newsList.append(json)
parseObj=pl.ParseRequset(newsList)
print("初始化完毕")
parseObj.anaylyseRequest(parseObj.list)

