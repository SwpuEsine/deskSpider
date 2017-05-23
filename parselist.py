#encode =utf-8
from python爬取招聘信息.fenghuang import parseFenghuang



class ParseRequset(object):
    def __init__(self,list):
        super().__init__()
        self.list=list
    def anaylyseRequest(self,list):
        for i in list:
            if i['web_chName']=='凤凰网':
                parseFenghuang(i)
                print(i)
            elif i['web_chName']=='南海网':
                pass
            elif i['web_chName']=='百度百家':
                pass
            elif i['web_chName']=='中华网':
                pass
            elif i['web_chName']=='新浪财经':
                pass
            elif i['web_chName']=='网易新闻':
                pass
        # json['url'] = row.a['href']
        # json['web_chName'] = row.select('span[style="color:#008000"]')[0].string
        # json['title'


if __name__ =="__main__":
    print("ok")