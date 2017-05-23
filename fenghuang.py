import requests
from bs4 import BeautifulSoup

# Default_Header = {
#     'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#     'Accept-Encoding':'gzip, deflate, sdch',
#     'Accept-Language': 'zh-CN,zh;q=0.8',
#     'Cache-Control': 'max-age=0',
#     'Connection': 'keep-alive',
#     'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36',
#     'Cookie':'prov=cn028; city=028; weather_city=sc_cd; region_ip=110.185.16.x; region_ver=1.2; UM_distinctid=15bbed4fde337d-0260f06b54f724-36465d60-100200-15bbed4fde45ba; __gads=ID=405a204bdc04cc61:T=1493555295:S=ALNI_MYG-lTMaL3WNfAgKlBgy1vCa27Ymw; userid=1493555288359_x9pkif8404; vjuids=1b5619c08.15bbeda13b2.0.2b26306d7ab5b; is_game_v=1; vjlast=1493555615.1495256368.13; afpCT=1; ADEZ_BLOCK_SLOT=FUCKIE; ADEZ_ST=FUCKIE; FTAPI_BLOCK_SLOT=FUCKIE; FTAPI_ST=FUCKIE; HOT_TAG=n; ifengRotator_AP468=0; ifengRotator_Ap2875=1; Hm_lvt_03ee991a65e88f21553ed82a0ddec689=1495256234,1495548112; Hm_lpvt_03ee991a65e88f21553ed82a0ddec689=1495548272; CNZZDATA1257375399=2039941646-1495543981-%7C1495543981; ifengRotator_AP1156=1; ifengRotator_AP4164=0; ADEZ_ASD=1; ADEZ_PVC=1013515-2-j323z4ga; ifengRotator_AP2842=0; ifengRotator_AP1373=0; ifengRotator_AP2865=1; FTAPI_ASD=1; ifengRotator_AP1157=0; Hm_lvt_6b2d710048ee7cec5c9e4731c33e21a2=1495256236,1495548115; Hm_lpvt_6b2d710048ee7cec5c9e4731c33e21a2=1495548278; ifengRotator_ArpAdPro_1954=0; ifengRotator_ArpAdPro_iams1081=3; ifengRotator_Ap2350=0; FTAPI_PVC=1006766-12-j323zh5o',    'Host':'www.baidu.com',
#
# }

def parseFenghuang(json):
    if json:
        fhurl=json['url']
        print(fhurl)
        content = requests.get(fhurl).content.decode("utf8")
        soup=BeautifulSoup(content,"lxml")
        json['title']=soup.find("h1",attrs={"id":"artical_topic"}).string
        resource=soup.find("a",attrs={"itemprop":"isBasedOnUrl"}).string
        comefrom="<p/>"+\
        "< span style = 'font-size:16px;color:#E53333;'><strong>"+"来源"+"</strong>:< / span >"+\
        "< span style = 'font-size:16px;color:#E53333;'><strong>" + resource + "</strong>:< / span >"+"</p>"
        mainContent=soup.find("div",attrs={"id":"main_content"})#找到p
        mainContent.find("p").extract()
        mainContent.find("span").extract()#移除
        json['content']=comefrom+mainContent


if __name__=="__main__":
    print("hello")