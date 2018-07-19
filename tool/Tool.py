import re
import urllib.request
import  os
'''
@Author :7aY
@Data: Create in 2018 3 14
@Version: Demo 1.1
@TODO:爬虫工具类

'''

class ReptileTool:
    
    def getUrlCode(url):
        try:
            headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.8 Safari/537.36','accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8'
               }
                #调用python3库的爬虫方法
            request=urllib.request.Request(url,headers=headers)
            UrlText =urllib.request.urlopen(request,timeout=180).read()#读取返回的网页源代码
            UrlText=UrlText.decode('utf-8',"ignore")#设置编码为utf-8
            return UrlText
        except :
            return 0



        
        
    
    def getFile_name(file_dir):
        file_name=os.listdir(file_dir)
        return file_name
    
    
    
    def getHtmlCode(html_path):
       
        
        html=open(html_path,'r',encoding='utf-8')#打开html文件,设置为可读，编码格式为utf-8
        htmlcont=html.read()#读取源代码
        return htmlcont#返回源代码
        
    '''

@Parameter : 正则表达式，被过滤的信息
@Return :过滤后的信息
获取正则表达式的值

    '''
    
    def filtrateMessage(regular_ex,text):
        message=re.findall(regular_ex,text)
        return message

        


    
        
    
        


        
        
