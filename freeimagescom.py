from bs4 import BeautifulSoup
import requests
import shutil
hdr = {'User-Agent': 'Mozilla/5.0'}

# storing page into variable
content_html = requests.get('https://www.freeimages.com/',headers=hdr).text
# converting page to soup
soup = BeautifulSoup(content_html,'lxml')

# finding elements with class and tag names
images_list = soup.select('.lazyload')

images_urls = []
for images in images_list:
    images_url = images.attrs['data-src']
    images_urls.append(images_url)

i=1
for url in images_urls:
    response = requests.get(url, stream=True,headers=hdr)
    if response.status_code ==200:
        # downloaing and saving images
        with open(f'images/imgage{i}.jpg','wb') as f:
            response.raw.decode_content = True
            shutil.copyfileobj(response.raw, f)

        i+=1