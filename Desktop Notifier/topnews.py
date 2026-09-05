"""
to ab hum is me request import krenge taki hum website ko response bej paayein as object
import krenge xlm.etree.ElementTree as Et ye kuch hota h jisse hume website ko parse kr payein as a tree

 ~ Phela function
    loadRSS()
        sabse phele ek variable m .get(url) krenge taki us variable me hum request object krenge
        ab variable.ontex retrurn maar do .content bytes m data bhej dega


 ~ doosra function
    parseXMl(rss)


        root=ET.formstring(rss)=> ye create element tree root object
        newsitem=[] => ek empty list banai

        for item in root.findall('./channel/item')

        iske neeche ka kuch to h samaj nhi aaga
        if child.tag == '{https://video.search.yahoo.com/mrss':
                news['media'] = child.attrib['url']
            else:
                news[child.tag] = child.text.encode('utf8')
        newsitems.append(news)

        :return newsitems

 ~ teesra function
    topStories()
        ye h main function
        rss=loadrss()

        parse xml
        newsitems=parseXML(rss)
        return newsitems

now we write a desktop notifier
import time
import notify2
from topnews import topstories

iconpath ="full path of icon"
newsitems=topstoreis()

notify2.init("News notifier)

n=notify2.Notificcation(none,icon=icoonpath)
n.set_urgency(notify.URGENCT_NORMAL

n.set_timeout(10000)


for newsitem in newsitems:

    # update notification data for Notification object
    n.update(newsitem['title'], newsitem['description'])

    # show notification on screen
    n.show()

    # short delay between notifications
    time.sleep(15)
"""
import requests
import xml.etree.ElementTree as ET

# url of news
RSS_FEED_URL = "http://www.hindustantimes.com/rss/topnews/rssfeed.xml"


def loadRSS():
    """
    utility function to load RSS feed
    """

    # create HTTP rewuest response object
    resp = requests.get(RSS_FEED_URL)

    # return response content
    return resp.content


def parseXML(rss):
    """
    utility function to load rss feed
    """

    # create element tree root object
    root = ET.fromstring(rss)

    # create empty list for news items
    newsitems = []

    # iterate news items
    for item in root.findall('./channel/items'):
        news = {}

        # iterate child elements of items
        for child in item:
            # special checking for namespace object content:media
            if child.tag == '{https://video.search.yahoo.com/mrss':
                news['media'] = child.attrib['url']
            else:
                news[child.tag] = child.text.encode('utf8')
        newsitems.append(news)

    return newsitems


def topStories():
    """
    main function to generate and return news items
    """

    # load rss feed
    rss = loadRSS()

    # parse XML
    newsitems = parseXML(rss)
    return newsitems
