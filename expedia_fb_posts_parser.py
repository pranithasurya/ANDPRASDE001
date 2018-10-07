from bs4 import BeautifulSoup as soup
from urllib.request import urlopen
import json

my_url =  "https://www.facebook.com/pg/expedia/posts/";

client = urlopen(my_url)
expedia_html = client.read()
client.close()

expedia_soup = soup(expedia_html,"html.parser")
posts =  expedia_soup.find("div",{"id":"pagelet_timeline_main_column"}).findAll("div",{"class":"_4-u2 _4-u8"})

result = []
count =0 

for each in posts:
    if count>=8:
        break

    post = str(each)
    post_html = soup(post, "html.parser")

    pinnedPost = post_html.find("i",{"data-tooltip-content":"Pinned Post"})

    if pinnedPost and 'Pinned Post' in pinnedPost['data-tooltip-content']:
        continue

    timestamp = post_html.find("span",{"class":"timestampContent"})
    message = post_html.find("div",{"data-ad-preview":"message"})
    image = post_html.find("div",{"class":"uiScaledImageContainer"})
    #postLink = post_html.findAll("div",{"class":"_3ekx _29_4"})
    postLinkDetails = post_html.find("div",{"class":"_3n1k"})
    likes = post_html.find("div",{"class":"UFILikeSentenceText"})

    try:
        obj = {}
        if timestamp:
            obj['timestamp'] = timestamp.text
        
        if message:
            obj['message'] = message.get_text().encode('UTF-8').decode()

        if image:
            obj['image'] = image.find('img')['src']

        if postLinkDetails:
            obj['postlink_content'] = postLinkDetails.find('div',{'class':'_6m7 _3bt9'}).get_text().encode('UTF-8').decode()
            obj['postlink'] = postLinkDetails.find('div',{'class':'mbs _6m6 _2cnj _5s6c'}).find('a')['href']

        if likes:
            obj['likes'] = likes.get_text.encode('UTF-8').decode()

        result.append(obj)
        count +=1
    except:
        print("error with this post")


with open('posts.json','w+') as f:
    json.dump(result, f, indent=4)