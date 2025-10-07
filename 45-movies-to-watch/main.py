from bs4 import BeautifulSoup
import requests

scrape_site = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"


def write_site(site):
    response = requests.get(site)
    with open('website.html', 'w') as file:
        file.write(response.text)


# write_site(scrape_site)

with open('website.html') as f:
    data = f.read()
soup = BeautifulSoup(data, 'html.parser')
movies = soup.find_all(name='h3', class_='title')

movie_li = [movie.get_text() for movie in movies]
movie_li.reverse()
# movies_li = [::-1}  # Another way to reverse a list

with open("movies.txt", "w") as movies_data:
    for movie in movie_li:
        movies_data.write(f'{movie}\n')
