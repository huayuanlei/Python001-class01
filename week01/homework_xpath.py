#获取猫眼电影页面
import requests
import lxml.etree
import pandas as pd

user_agent = 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Mobile Safari/537.36'

header = {'user-agent':user_agent}

myurl = 'https://maoyan.com/films?showType=3'

res = requests.get(myurl,headers=header)

bs_info = lxml.etree.HTML(res.text)

for list in range(1,11):
    name_movie = bs_info.xpath(f'//a[{list}]/div/div[2]/div[1]/text()')
    style_movie = bs_info.xpath(f'//a[{list}]/div/div[2]/div[3]/text()')
    time_movie = bs_info.xpath(f'//a[{list}]/div/div[2]/div[4]/text()')
    #print(name_movie)
    mylist = [
        name_movie,
        style_movie,
        time_movie
    ]
    movie_xpath = pd.DataFrame(data = mylist)
    movie_xpath.to_csv('./movie_xpath.csv', encoding='utf-8', index=False, header=0 ,mode="a")
    print(mylist)



