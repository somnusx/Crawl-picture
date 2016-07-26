import re
import os
import random
import requests
from multiprocessing.dummy import Pool as ThreadPool




def down(url):
    httphead = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko'}
    r = requests.get(url, headers=httphead)
    s = r.text
    urls = re.findall(r"http://ww.+?jpg", s)
    for url in urls:
        r = requests.get(url)
        name = 'picture' +'/' + url.split('/')[-1]
        print(name)
        with open(name,'wb') as code:
            code.write(r.content)


if __name__ == '__main__':
    pool = ThreadPool(4)
    page = []
    if not os.path.exists('picture'):
        os.mkdir('picture')
    for i in range(100,1000):
        new_url = 'http://jandan.net/ooxx/page-' + str(i) + '#comments'
        page.append(new_url)

    results = pool.map(down,page)
    pool.close()
    pool.join()
    

