'''
@author=7aY
@verison=
@Todo(下载Box office mojo的所有网页，包括daily 和 weekend weekly)
@since:2018.1.10
'''
from tool.Tool import ReptileTool
import time
from os import  *

'''
Methond:getYearUrl
Todo(获取BoxOffice mojo 的每一年的URl)
return year url
'''
def getYearUrl():
    yearURL=[]
    # i为URL 中的year 的年份参数
    for i in range(1980,2018):
       # url='http://www.boxofficemojo.com/yearly/chart/?yr=%d&p=.htm',%i
        yearURL.append('http://www.boxofficemojo.com/yearly/chart/?yr=%d&p=.htm'%i)
    return yearURL#返回yearlurl list
'''
Method:getFilmUrl
Todo(获取电影主页的URL)
return 每一个年份的电影url List
'''
def getFilmUrl(yearUrl):
    yearhtmlcode=ReptileTool.getUrlCode(yearUrl)#获取当前年份页面的源代码
    if yearhtmlcode==0:
        return 0
    FirstpageUrl_relink='<b><font size="2"><a href="(.*?)">.*?</a></font></b>'#获取第一页的电影URL正则表达式
    FirstPageUrl=ReptileTool.filtrateMessage(FirstpageUrl_relink,yearhtmlcode)#获取第一页的电影url
    url=[]
    for fu in FirstPageUrl:
        Url='http://www.boxofficemojo.com'+fu
        url.append(Url)
    return url

'''
MeThod:getOtherPageYearUrl
Todo('获取该年份另外的年份页面')
return 年份url
'''
def getOtherPageYearUrl(yearUrl):
    yearhtmlcode = ReptileTool.getUrlCode(yearUrl)  # 获取当前年份页面的源代码
    if yearhtmlcode==0:
        return 0
    otherPage_relink='- <a href="(.*?)">.*?</a>'
    otherPageUrl=ReptileTool.filtrateMessage(otherPage_relink,yearhtmlcode)
    url=set()
    for of in otherPageUrl:
        Url='http://www.boxofficemojo.com'+of
        url.add(Url)

    return url
def DownloadDailyHtml(url,filename,filepath):
    htmlcode=ReptileTool.getUrlCode(url)
    if htmlcode==0:
        return 0
    file=open(r'%s\Daily_%s.html'%(filepath,filename),'w')
    file.write(htmlcode)
    print('DownLoad Daily html')
def DownloadWeekendHtml(url,filename,filepath):
    htmlcode=ReptileTool.getUrlCode(url)
    if htmlcode==0:
        return 0
    file=open(r'%s\Weekend_%s.html'%(filepath,filename),'w')
    file.write(htmlcode)
    print('DownLoad Weekend html')
def DownloadWeeklyHtml(url,filename,filepath):
    htmlcode=ReptileTool.getUrlCode(url)
    path=os.path
    if htmlcode==0:
        return 0
    file=open(r'%s\Weekly_%s.html'%(filepath,filename),'w')
    file.write(htmlcode)
    print('DownLoad Weekly html')
def DownloadForeign(url,filename,filepath):
    htmlcode=ReptileTool.getUrlCode(url)
    if htmlcode==0:
        return 0
    file = open(r'%s\Foreign_%s.html' % (filepath,filename), 'w')
    file.write(htmlcode)
    print('DownLoad Foreign html')

def star(a_weekend_path,a_weekly_path,a_daily_path,foreign_path):
        function = int(input('Function 1:american  '
                     'function2:foreign :'))

        url=getYearUrl()#获取所有年份Url
        print(len(url))
        for yearurl in url:
            filmUrl = []
            otherfilmUrl = []
            print(yearurl)
            otherpageYearUrl=getOtherPageYearUrl(yearurl)#获取除了首页外的其他页面url
            if otherpageYearUrl==0:
                continue

            homepageFilmUrl=getFilmUrl(yearurl)#获取第一页所有电影的url
            if homepageFilmUrl==0:
                continue
            filmUrl.extend(homepageFilmUrl)#放到filmUrl这个list中
            for url in otherpageYearUrl:

                otherUrl=getFilmUrl(url)#获取其他页面电影所有的url
                if otherUrl==0:
                    continue
                filmUrl.extend(otherUrl)#放到这个list里面去

                #print(otherpageYearUrl)
            for url in filmUrl:

                htmlcode=ReptileTool.getUrlCode(url)
                if htmlcode==0:
                    continue
                daily_relink='<li><a href="(.*?)">Daily</a></li>'
                weekend_relink='<li><a href="(.*?)">Weekend</a></li>'
                weekly_relink='<li><a href="(.*?)">Weekly</a></li>'
                foreign_relink='<li><a href="(.*?)">Foreign</a></li>'


                if function==1:
                    locltime = time.strftime("%Y%m%d%H%M%S", time.localtime())
                    d_u = ReptileTool.filtrateMessage(daily_relink, htmlcode)
                    w_u = ReptileTool.filtrateMessage(weekend_relink, htmlcode)
                    wl_u = ReptileTool.filtrateMessage(weekly_relink, htmlcode)



                    if d_u:
                        daily_url='http://www.boxofficemojo.com'+d_u[0]
                        flag=DownloadDailyHtml(daily_url,locltime,a_daily_path)
                        if flag==0:
                            print('error')
                            continue
                    if w_u:
                        weekend_url='http://www.boxofficemojo.com'+w_u[0]
                        flag=DownloadWeekendHtml(weekend_url,locltime,a_weekend_path)
                        if flag==0:
                            print('error')
                            continue
                    if wl_u:
                        weekly_url='http://www.boxofficemojo.com'+wl_u[0]
                        flag=DownloadWeeklyHtml(weekly_url,locltime,a_weekly_path)
                        if flag==0:
                            print('error')
                            continue
                elif function==2:
                        print('star')

                        f_u=ReptileTool.filtrateMessage(foreign_relink, htmlcode)

                        if f_u:
                            foreign_url = 'http://www.boxofficemojo.com' + f_u[0]
                            Homepage=ReptileTool.getUrlCode(foreign_url)
                            if Homepage==0:
                                continue
                            country_relink=r'<tr bgcolor="#f4f4ff"><td><font size="2"><b><a href="(.*?)">.*?</a></b></font></td>'
                            country_url=ReptileTool.filtrateMessage(country_relink,Homepage)
                            if country_url:
                                for url in country_url:
                                    locltime = time.strftime("%Y%m%d%H%M%S", time.localtime())
                                    url='http://www.boxofficemojo.com'+url
                                    print(url)

                                    flag=DownloadForeign(url,locltime)
                                    if flag==0:
                                        continue
                            else:
                                locltime = time.strftime("%Y%m%d%H%M%S", time.localtime())
                                flag=DownloadForeign(foreign_url,locltime,foreign_path)





