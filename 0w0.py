import re
import urllib.request
import os
import json
import time

class GetHtml2Json():
    PageI = 0
    mName = ""
    def getHtml(self):
        #print(PageI)
        NameEncode = urllib.parse.quote_plus(self.mName.encode('GB2312'))
        FullUrl = "http://tieba.baidu.com/f/search/ures?kw=&qw=&rn=10&un=" + \
                 NameEncode + "&only_thread=&sm=0&sd=&ed=&pn=" + str(self.PageI)
        #print (FullUrl)
        try:
            Page = urllib.request.urlopen(FullUrl)
            mHtml = Page.read().decode('GBK')
        except:
            raise Exception("Err")

        reStr = r'<div class=\"s_post\"><span class=\"p_title\"><a.*?>(.*?)</a></span>.*?<div class=\"p_content\">(.*?)</div>.*?<font class=\"p_violet\">(.+?)</font>.*?<font class=\"p_green p_date\">(.+?)</font>.*?</div>'
        ReTmp = re.compile(reStr)
        List = re.findall(ReTmp, mHtml)
        return List
        
    def __init__(self, i, Name):
        self.PageI = i
        self.mName = Name

    def getElement(self):
        mFileName = self.mName + '.json'
        mFile = open(mFileName, 'a+')
        mList = self.getHtml()
        print(mList)
        
        for s in mList:
            data={} 
            data["Title"] = s[0]
            data["context"] = s[1]
            data["Tieba"] = s[2]
            data["Time"] = s[3]
            jsonStr = json.dumps(data, ensure_ascii = False, indent=2)
            data.clear()
            mFile.write(jsonStr)
            jsonStr = ""
        mFile.close()

if __name__ == "__main__":
    i = 1
    PageNum = 50
    Name = "叶梦舞鸢"
    while i <= PageNum:
        A = GetHtml2Json(i, Name)
        A.getElement()
        time.sleep(3)
        i += 1


    
