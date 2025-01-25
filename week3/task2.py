import urllib.request as req
import ssl
ssl._create_default_https_context = ssl._create_unverified_context
import bs4 
import csv

def getData(url):
    #建立request物件，附加request headers資訊
    request = req.Request(url, headers={
        "cookie":"over18=1",
        "User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36"
    })
    with req.urlopen(request) as response:
        homepage_data=response.read().decode("utf-8")

    root = bs4.BeautifulSoup(homepage_data,"html.parser")
    titles = root.find_all("div", class_="title")
    score = root.find_all("div", class_="nrec")
    result = []
    for title, nrec in zip(titles, score):
        if title.a != None:               #排除文章被刪除者
            title_text = title.a.string
            title_link = "https://www.ptt.cc"+title.a["href"] 
            #取得標題連結的網頁內資訊
            page_request = req.Request(title_link, headers={
                "cookie":"over18=1",
                "User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36"
            })
            with req.urlopen(page_request) as page_response:
                titlepage_data = page_response.read().decode("utf-8")
                page_data = bs4.BeautifulSoup(titlepage_data,"html.parser")
                page_articles = page_data.find_all("div", class_="article-metaline")
                
                if not page_articles:
                    time_text = " "
                else:
                    for article in page_articles:
                        tag = article.find("span", class_="article-meta-tag")
                        if tag.text == "時間":
                            time_text = article.find("span", class_="article-meta-value").text
                            break
        else:
            title_text = "No title"
            title_link = "None"
        
        if nrec.span != None:     #score不等於0
            score_text = nrec.span.text
        else:
            score_text = "0" 
        if(title_text != "No title"):
            result.append([title_text,score_text,time_text])
       
    #抓取下一頁面的連結
    nextLink=root.find("a", string="‹ 上頁")
    my_dic = {
        "next": nextLink["href"],
        "pageData": result
    }
    return my_dic


pageURL="https://www.ptt.cc/bbs/Lottery/index.html"

collect = []
for i in range(0, 3, 1):
    d = getData(pageURL)
    pageURL = "https://www.ptt.cc"+d["next"]
    pageData = d["pageData"]
    collect = collect + pageData

# print(collect)

# output file in CSV format
with open("article.csv","w",newline="",encoding="utf-8") as article_csv:  
    data=csv.writer(article_csv)
    data.writerows(collect)

print("done")