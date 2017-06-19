# -*- coding:utf-8 -*-
import urllib2,re
from bs4 import BeautifulSoup

articleUrl = "https://www.qiushibaike.com/textnew/page/%d" #文章地址
commentUrl = "https://www.qiushibaike.com/article/%s" #评论地址
page = 0
Url = articleUrl % page

#获取主页源码
def getContentOrComment(Url):
    user_agent = "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.104 Safari/537.36"#检索获得
    headers = {'User-Agent':user_agent}#浏览器信息
    req = urllib2.Request(url=Url,headers=headers)
    response = urllib2.urlopen(req) #打开网页
    content = response.read()  #获取源码
    #print content
    return content
articlePage = getContentOrComment(Url)
#获取文章内容
soupArticle = BeautifulSoup(articlePage,'html.parser')#解析网页
articleFloor  = 1#楼层
commentFloor  = 1#楼层
for string in soupArticle.find_all(attrs = "article block untagged mb15"):
    commentId = str(string.get('id'))[11:]
    print articleFloor,".",string.find(attrs = "content").get_text().strip()#获取文本
    articleFloor += 1

    #获取评论
    commentPage = getContentOrComment(commentUrl%commentId) #获取详情页源码
    if commentPage is None:
        continue
    soupComment = BeautifulSoup(commentPage,'html.parser')
    for comment in soupComment.find_all(attrs="body"):
        print"   ",commentFloor,"楼回复：",comment.get_text()
        commentFloor += 1