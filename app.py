import re
from downloadImage import download_image
from bs4 import BeautifulSoup
from googlesearch import search
import requests
from flask import Flask,request
from makeVideo import makeVideo
# to search


app = Flask(__name__)

@app.route("/")
def mainApp():
 return "done"
 nameWebSite = request.args.get('name')
 print(request.args.get('limit'))
 limit = int(request.args.get('limit'))
 link = ""
 for j in search(nameWebSite, tld="co.in", num=1, stop=1, pause=1):
    link = j
    print(j)

 html = requests.get(link).content


 soup = BeautifulSoup(html, 'html.parser')

 images = re.findall(r'\bhttps?:\/\/[^\s]+\.jpg|https?:\/\/[^\s]+\.png\b',str(soup))
 print(images)
 for i in range(limit):
    if len(images) > i:
     download_image(images[i],i)

 makeVideo("C:/Users/User/PycharmProjects/devops/images/", "video.mp4")
 return 'done'
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)