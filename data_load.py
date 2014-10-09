import urllib.request
import re
import pickle

def count_substring(str):
    length = len(str) 
    found = []
    for i in range(0, length):
        for j in range(i+1, length):
                if str[i] == '/' and str[j]=='/':
                        found.append(str[i+1:j])
                        break
    return found


def visit_url(url, domain):
    global str_set
    global crawler_backlog
    global urlzList
    if(url in crawler_backlog and crawler_backlog[url] == 1):
        return
    else:
        crawler_backlog[url] = 1

    page = urllib.request.urlopen(seed)
    content=page.read()
    content_string = content.decode("utf-8")
    urlzList[url]=content_string
    code=page.getcode()

    regexp_title = re.compile('<title>(?P<title>(.*))</title>')
    regexp_keywords = re.compile('<meta name="keywords" content="(?P<keywords>(.*))" />')
    regexp_url = re.compile(domain+"[/\w+]*")

    result = regexp_title.search(content_string, re.IGNORECASE)
    
    x=count_substring(url)
    for word in x:
            str_set.add(word)
    
        
    for (urls) in re.findall(regexp_url, content_string):
            if(urls  not in crawler_backlog or crawler_backlog[urls] != 1):
                crawler_backlog[urls] = 0
                visit_url(urls, domain)


crawler_backlog = {}
urlzList={}
dict1={}
str_set=set()
seed = "http://www.newhaven.edu/"
def main():
        f=open("web_content",'wb')
        

        crawler_backlog[seed]=0

        visit_url(seed, "www.newhaven.edu")
        
        pickle.dump(urlzList,f)
        f.close()
        #for key,value in urlzList.items():
         #       print(key)
        return str_set



