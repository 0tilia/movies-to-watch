import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

response = requests.get(URL)

movie_website = response.text

soup = BeautifulSoup(movie_website, "html.parser")

all_movies = soup.find_all(name="h3", class_="title")

movie_title = [movie.getText() for movie in all_movies]

movies = movie_title[::-1]

with open("movies.txt", mode="w") as file:
    for movie in movies:
        file.write(f"{movie}\n")






