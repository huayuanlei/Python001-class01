#获取猫眼电影页面

import requests
from bs4 import BeautifulSoup

user_agent = 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Mobile Safari/537.36'

header = {'user-agent':user_agent}

myurl = 'https://maoyan.com/films?showType=3'

res = requests.get(myurl,headers=header)

bs_info = BeautifulSoup(res.text,"html.parser")

div_movies = bs_info.find("div",class_="classic-movies-list")

movie_names = div_movies.find_all("div",class_="title line-ellipsis")
movie_types = div_movies.find_all("div",class_="actors line-ellipsis")
movie_times = div_movies.find_all("div",class_="show-info line-ellipsis")

with open("movies.csv","w",encoding="utf-8") as fout:
    for line in range(10):
        #print(movie_names[line].get_text())
        out_movies = [
            movie_names[line].get_text(),
            movie_types[line].get_text(),
            movie_times[line].get_text()
        ]
        fout.write("\t".join(out_movies)+"\n")
        print(out_movies)

